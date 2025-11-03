#!/usr/bin/env python3
"""
PaddleOCR Wrapper Script
Mimics Tesseract CLI interface for compatibility with Zotero OCR plugin
Usage: python paddleocr_wrapper.py <image_list_file> <output_base> --psm <mode> -l <lang> <output_types>
"""

import sys
import os
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Error: Insufficient arguments", file=sys.stderr)
        sys.exit(1)
    
    try:
        from paddleocr import PaddleOCR
    except ImportError:
        print("Error: PaddleOCR not installed. Please install with: pip install paddleocr", file=sys.stderr)
        sys.exit(1)
    
    # Parse arguments
    image_list_file = sys.argv[1]
    output_base = sys.argv[2]
    
    # Parse optional arguments
    lang = 'ch'  # default to Chinese/English
    psm_mode = '3'  # not used for PaddleOCR, but kept for compatibility
    output_types = []
    
    i = 3
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '-l' and i + 1 < len(sys.argv):
            lang = sys.argv[i + 1]
            i += 2
        elif arg == '--psm' and i + 1 < len(sys.argv):
            psm_mode = sys.argv[i + 1]
            i += 2
        else:
            output_types.append(arg)
            i += 1
    
    # Map language codes from Tesseract to PaddleOCR
    lang_map = {
        'eng': 'en',
        'chi_sim': 'ch',
        'chi_tra': 'chinese_cht',
        'jpn': 'japan',
        'kor': 'korean',
        'fra': 'fr',
        'deu': 'german',
        'ita': 'it',
        'rus': 'ru',
        'spa': 'spanish',
        'por': 'portuguese',
    }
    
    paddle_lang = lang_map.get(lang, lang)
    
    # Read image list
    with open(image_list_file, 'r') as f:
        image_files = [line.strip() for line in f if line.strip()]
    
    if not image_files:
        print("Error: No images found in list file", file=sys.stderr)
        sys.exit(1)
    
    # Initialize PaddleOCR
    # Use CPU by default for compatibility
    ocr = PaddleOCR(use_angle_cls=True, lang=paddle_lang, use_gpu=False, 
                    show_log=False, use_space_char=True)
    
    # Process images
    all_text = []
    all_hocr = []
    page_num = 0
    
    for idx, img_path in enumerate(image_files):
        print(f"Page {idx} : Processing {img_path}", flush=True)
        
        if not os.path.exists(img_path):
            print(f"Warning: Image file not found: {img_path}", file=sys.stderr)
            continue
        
        try:
            result = ocr.ocr(img_path, cls=True)
            
            if result and result[0]:
                page_text = []
                for line in result[0]:
                    if line and len(line) >= 2:
                        text = line[1][0]  # Extract text from result
                        page_text.append(text)
                
                all_text.extend(page_text)
                
                # Generate hOCR format if requested
                if 'hocr' in output_types:
                    img_name = os.path.basename(img_path)
                    hocr_content = generate_hocr(result[0], img_name, page_num)
                    all_hocr.append(hocr_content)
                
                page_num += 1
        except Exception as e:
            print(f"Error processing {img_path}: {str(e)}", file=sys.stderr)
            continue
    
    # Write text output
    if 'txt' in output_types:
        txt_file = output_base + '.txt'
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(all_text))
    
    # Write hOCR output
    if 'hocr' in output_types:
        hocr_file = output_base + '.hocr'
        with open(hocr_file, 'w', encoding='utf-8') as f:
            f.write(generate_full_hocr(all_hocr, image_files))
    
    # For PDF output, we'll generate it from images using img2pdf
    if 'pdf' in output_types:
        try:
            import img2pdf
            from PIL import Image
            
            pdf_file = output_base + '.pdf'
            
            # Convert images to PDF with text layer
            # Since PaddleOCR doesn't directly generate PDF, we create a simple image PDF
            # For a proper searchable PDF, we'd need to use a PDF library to add text layer
            
            # For now, create a simple image-based PDF
            with open(pdf_file, 'wb') as f:
                # Filter valid image paths
                valid_images = [img for img in image_files if os.path.exists(img)]
                if valid_images:
                    f.write(img2pdf.convert(valid_images))
        except ImportError:
            print("Warning: img2pdf not installed. PDF output skipped. Install with: pip install img2pdf", file=sys.stderr)
        except Exception as e:
            print(f"Error generating PDF: {str(e)}", file=sys.stderr)


def generate_hocr(result, img_name, page_num):
    """Generate hOCR content for a single page"""
    lines = []
    
    for idx, line in enumerate(result):
        if line and len(line) >= 2:
            bbox = line[0]  # [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
            text = line[1][0]
            confidence = line[1][1] if len(line[1]) > 1 else 1.0
            
            # Convert bbox to hOCR format (left, top, right, bottom)
            x_coords = [point[0] for point in bbox]
            y_coords = [point[1] for point in bbox]
            left = int(min(x_coords))
            top = int(min(y_coords))
            right = int(max(x_coords))
            bottom = int(max(y_coords))
            
            hocr_line = f'    <span class="ocr_line" id="line_{page_num}_{idx}" title="bbox {left} {top} {right} {bottom}; x_wconf {int(confidence * 100)}">{text}</span>\n'
            lines.append(hocr_line)
    
    return ''.join(lines)


def generate_full_hocr(page_contents, image_files):
    """Generate complete hOCR document"""
    hocr_header = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<title></title>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta name="ocr-system" content="PaddleOCR" />
<meta name="ocr-capabilities" content="ocr_page ocr_carea ocr_par ocr_line ocrx_word" />
</head>
<body>
"""
    
    hocr_body = []
    for idx, (content, img_file) in enumerate(zip(page_contents, image_files)):
        img_name = os.path.basename(img_file)
        page_div = f"""<div class='ocr_page' id='page_{idx}' title='image "{img_name}"'>
{content}</div>
"""
        hocr_body.append(page_div)
    
    hocr_footer = "</body>\n</html>"
    
    return hocr_header + ''.join(hocr_body) + hocr_footer


if __name__ == '__main__':
    main()
