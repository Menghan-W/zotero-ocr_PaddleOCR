# Changes from Original Zotero OCR Plugin

## Version 1.0.0 - PaddleOCR Adaptation

This document summarizes the changes made to adapt the Zotero OCR plugin to use PaddleOCR instead of Tesseract.

### Major Changes

#### 1. OCR Engine
- **Before**: Tesseract OCR
- **After**: PaddleOCR (Python-based)
- **Impact**: Better accuracy for Chinese, Japanese, and Korean languages; easier installation via pip

#### 2. Installation Requirements
- **Added**: Python 3.7+ requirement
- **Added**: PaddleOCR Python package (`pip install paddleocr`)
- **Added**: Optional img2pdf for PDF generation (`pip install img2pdf`)
- **Removed**: Tesseract OCR binary requirement
- **Kept**: pdftoppm requirement (still needed for PDF to image conversion)

#### 3. New Components
- **`paddleocr_wrapper.py`**: A Python script that bridges PaddleOCR with Zotero's JavaScript environment
  - Mimics Tesseract's command-line interface
  - Handles image list processing
  - Generates text, hOCR, and PDF outputs
  - Maps Tesseract language codes to PaddleOCR equivalents

#### 4. Configuration Changes
- **Removed**: `zoteroocr.ocrPath` (Tesseract path)
- **Added**: `zoteroocr.pythonPath` (Python executable path)
- **Added**: `zoteroocr.ocrWrapperPath` (Path to paddleocr_wrapper.py)
- **Changed**: Default language from 'eng' to 'ch' (Chinese/English)

#### 5. User Interface Updates
- Updated preference labels to reference PaddleOCR instead of Tesseract
- Added configuration field for Python path
- Added configuration field for wrapper script path
- Updated help text and descriptions

#### 6. Language Support
- Default language changed to 'ch' (Chinese and English combined)
- Language code mapping:
  - `eng` → `en` (English only)
  - `chi_sim` → `ch` (Simplified Chinese)
  - `chi_tra` → `chinese_cht` (Traditional Chinese)
  - `jpn` → `japan` (Japanese)
  - `kor` → `korean` (Korean)
  - And more...

### Technical Implementation Details

#### File Changes
1. **`src/zotero-ocr.js`**:
   - Replaced Tesseract detection with Python detection
   - Added wrapper script path resolution
   - Modified OCR command execution to use Python with wrapper script
   - Updated language code validation

2. **`src/prefs.xhtml`**:
   - Updated UI labels and descriptions
   - Added Python and wrapper script path fields
   - Removed Tesseract-specific references

3. **`src/defaults/preferences/defaults.js`**:
   - Changed default language from 'eng' to 'ch'

4. **`src/manifest.json`**:
   - Updated plugin name to "Zotero OCR (PaddleOCR)"
   - Changed version to 1.0.0
   - Updated author attribution
   - Changed plugin ID to avoid conflicts with original plugin

5. **`README.md`**:
   - Added PaddleOCR introduction and benefits
   - Updated installation instructions
   - Updated configuration documentation
   - Removed Tesseract-specific content

### Backward Compatibility

This version is **NOT** backward compatible with the original Tesseract-based plugin due to:
- Different OCR engine requirements
- Changed preference keys
- Different plugin ID

Users switching from the original plugin will need to:
1. Uninstall the original plugin
2. Install Python and PaddleOCR
3. Install this version
4. Reconfigure settings (paths and language preferences)

### Known Limitations

1. **PDF Output**: The wrapper script uses img2pdf for PDF generation, which creates image-based PDFs. For searchable PDFs with embedded text layers, additional work may be needed.

2. **First-time Setup**: Users must manually download and place the `paddleocr_wrapper.py` script in an accessible location (unlike the original plugin where Tesseract could be auto-detected in standard locations).

3. **PSM Mode**: The Page Segmentation Mode setting is kept for compatibility but is not used by PaddleOCR.

### Benefits of PaddleOCR

1. **Better CJK Support**: Significantly improved accuracy for Chinese, Japanese, and Korean texts
2. **Modern Architecture**: Based on deep learning models (PP-OCRv3/v4)
3. **Easy Installation**: Simple pip installation without system dependencies
4. **Active Development**: Regularly updated by Baidu with latest research
5. **Flexible**: Works with both CPU and GPU

### Migration Guide

For users migrating from the original Tesseract-based plugin:

1. **Uninstall** the original Zotero OCR plugin
2. **Install Python 3.7+** if not already installed
3. **Install PaddleOCR**: 
   ```bash
   pip install paddleocr
   ```
4. **Download** `paddleocr_wrapper.py` from the repository
5. **Place** the wrapper script in your Zotero data directory
6. **Install** this plugin's XPI file
7. **Configure** the paths in Zotero OCR preferences if auto-detection fails
8. **Test** with a sample PDF

### Support

For issues specific to this PaddleOCR adaptation, please report them at:
https://github.com/Menghan-W/zotero-ocr_PaddleOCR/issues

For general Zotero OCR functionality inherited from the original plugin, refer to:
https://github.com/UB-Mannheim/zotero-ocr
