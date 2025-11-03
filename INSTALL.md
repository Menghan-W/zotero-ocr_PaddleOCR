# Quick Installation Guide

This guide will help you quickly set up Zotero OCR with PaddleOCR.

## Installation Method 1: Using Pixi (Recommended)

Pixi automatically manages all Python dependencies in an isolated project environment.

### Step 1: Install Pixi

**Linux/macOS:**
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

**Windows (PowerShell):**
```powershell
iwr -useb https://pixi.sh/install.ps1 | iex
```

**Verify installation:**
```bash
pixi --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/Menghan-W/zotero-ocr_PaddleOCR.git
cd zotero-ocr_PaddleOCR
```

### Step 3: Install All Dependencies

```bash
pixi install
```

This command will:
- Install Python 3.7+ automatically
- Install PaddleOCR and all its dependencies
- Install img2pdf for PDF output
- Create an isolated environment in `.pixi/envs/default/`

### Step 4: Install pdftoppm

#### Windows
Download Poppler tools from: http://blog.alivate.com.au/poppler-windows/
Extract and add the `bin` folder to your system PATH.

#### Linux (Debian/Ubuntu)
```bash
sudo apt-get install poppler-utils
```

#### Linux (CentOS/Fedora)
```bash
sudo yum install poppler-utils
```

#### macOS
```bash
brew install poppler
```

### Step 5: Install the Plugin

1. Download the latest XPI file from:
   https://github.com/Menghan-W/zotero-ocr_PaddleOCR/releases

2. In Zotero:
   - **Zotero 7**: Tools → Plugins → Drag the XPI file
   - **Zotero 6**: Tools → Add-ons → Drag the XPI file → Restart Zotero

### Step 6: Configure

Go to Zotero → Settings (or Tools → Zotero OCR Preferences)

Set the paths:
- **Python Path**: 
  - Linux/Mac: `<project-dir>/.pixi/envs/default/bin/python`
  - Windows: `<project-dir>\.pixi\envs\default\python.exe`
  - Replace `<project-dir>` with the full path to your cloned repository
- **PaddleOCR Wrapper Path**: `<project-dir>/src/paddleocr_wrapper.py`
- **pdftoppm Path**: Usually auto-detected

**Language Settings:**
- Default is "ch" (Chinese and English)
- Change to "en" for English only, "japan" for Japanese, etc.

### Step 7: Test It!

1. Select a PDF in Zotero
2. Right-click → "OCR selected PDF(s)"
3. Wait for processing (first run may download models)
4. Check the output attachments!

---

## Installation Method 2: Manual Setup

### Step 1: Install Python

Download and install Python 3.7 or later from https://www.python.org/downloads/

**Verify installation:**
```bash
python --version
# or
python3 --version
```

### Step 2: Install PaddleOCR

Open a terminal/command prompt and run:

```bash
pip install paddleocr
```

**Optional (for PDF output):**
```bash
pip install img2pdf
```

### Step 3: Install pdftoppm

#### Windows
Download Poppler tools from: http://blog.alivate.com.au/poppler-windows/
Extract and add the `bin` folder to your system PATH.

#### Linux (Debian/Ubuntu)
```bash
sudo apt-get install poppler-utils
```

#### Linux (CentOS/Fedora)
```bash
sudo yum install poppler-utils
```

#### macOS
```bash
brew install poppler
```

### Step 4: Download the Wrapper Script

1. Download `paddleocr_wrapper.py` from:
   https://github.com/Menghan-W/zotero-ocr_PaddleOCR/blob/main/src/paddleocr_wrapper.py

2. Place it in one of these locations:
   - **Recommended**: Your Zotero data directory
     - Find it: Zotero → Preferences → Advanced → Files and Folders → "Show Data Directory"
   - Alternative locations:
     - `/usr/local/bin/` (Linux/Mac)
     - `C:\Program Files\Zotero\` (Windows)

### Step 5: Install the Plugin

1. Download the latest XPI file from:
   https://github.com/Menghan-W/zotero-ocr_PaddleOCR/releases

2. In Zotero:
   - **Zotero 7**: Tools → Plugins → Drag the XPI file
   - **Zotero 6**: Tools → Add-ons → Drag the XPI file → Restart Zotero

### Step 6: Configure (if needed)

Go to Zotero → Settings (or Tools → Zotero OCR Preferences)

If paths are not auto-detected, set:
- **Python Path**: Path to your Python executable (e.g., `python3` or `C:\Python3\python.exe`)
- **PaddleOCR Wrapper Path**: Full path to `paddleocr_wrapper.py`
- **pdftoppm Path**: Path to pdftoppm (usually auto-detected)

**Language Settings:**
- Default is "ch" (Chinese and English)
- Change to "en" for English only, "japan" for Japanese, etc.

### Step 7: Test It!

1. Select a PDF in Zotero
2. Right-click → "OCR selected PDF(s)"
3. Wait for processing (first run may download models)
4. Check the output attachments!

---

## Troubleshooting

### Using Pixi

#### "pixi: command not found"
- Make sure Pixi is installed correctly
- Restart your terminal/shell after installation
- Verify with: `pixi --version`

#### Dependencies not working
- Run `pixi install` again in the project directory
- Make sure you're using the Python from `.pixi/envs/default/`

### Manual Installation

#### "No Python executable found"
- Make sure Python is installed and in your PATH
- Try specifying the full path in preferences

#### "PaddleOCR wrapper script not found"
- Verify you placed `paddleocr_wrapper.py` in the correct location
- Set the path manually in preferences

#### "PaddleOCR not installed"
- Run: `pip install paddleocr`
- Make sure you're using the same Python that Zotero is finding

### General Issues

#### First run is slow
- PaddleOCR downloads models on first use (normal behavior)
- Subsequent runs will be faster

#### OCR results are poor
- Try different language settings
- Adjust output DPI (300 is default, try 400-600 for better quality)
- Make sure the PDF quality is good

## Getting Help

- Issues: https://github.com/Menghan-W/zotero-ocr_PaddleOCR/issues
- PaddleOCR docs: https://github.com/PaddlePaddle/PaddleOCR
- Original plugin: https://github.com/UB-Mannheim/zotero-ocr

## Success!

You're now ready to use Zotero OCR with PaddleOCR! 🎉

Enjoy better OCR accuracy, especially for Chinese, Japanese, and Korean documents!
