# Zotero OCR (PaddleOCR Edition)

This is a fork of [Zotero OCR](https://github.com/UB-Mannheim/zotero-ocr) adapted to use [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) instead of Tesseract OCR.

## Why PaddleOCR?

PaddleOCR is a practical ultra-lightweight OCR system developed by Baidu, offering:
- **Better multilingual support**, especially for Chinese, Japanese, and Korean
- **State-of-the-art accuracy** with PP-OCRv3/v4 models
- **Flexible deployment** options (CPU/GPU)
- **Easy installation** via pip

## Key Differences from Original Plugin

- **OCR Engine**: Uses PaddleOCR instead of Tesseract
- **Installation**: Requires Python and PaddleOCR installation
- **Default Language**: Changed to "ch" (Chinese/English) instead of "eng"
- **Wrapper Script**: Includes a Python wrapper script to bridge PaddleOCR with Zotero

---

This Zotero plugin adds the functionality to perform an OCR for the PDFs selected in Zotero.
It can add a new PDF including the recognized text, a note with the recognized text only, and HTML (hOCR) file(s).
**PaddleOCR** is used for the text recognition itself.


## Prerequisites

### Option 1: Using Pixi (Recommended)

[Pixi](https://pixi.sh/) is a modern package manager that handles all Python dependencies automatically in an isolated project environment.

1. **Install Pixi** (one-time setup):
   ```bash
   # Linux/macOS
   curl -fsSL https://pixi.sh/install.sh | bash
   
   # Windows (PowerShell)
   iwr -useb https://pixi.sh/install.ps1 | iex
   ```

2. **Install dependencies** (in the project directory):
   ```bash
   pixi install
   ```

   This automatically installs Python, PaddleOCR, img2pdf, and all required dependencies in an isolated environment.

3. **Install pdftoppm**:
   - For Windows: Download from http://blog.alivate.com.au/poppler-windows/
   - For Linux: `sudo apt-get install poppler-utils` (Debian/Ubuntu) or `sudo yum install poppler-utils` (CentOS/Fedora)
   - For Mac: `brew install poppler`

### Option 2: Manual Installation

- **Python 3.7+** is installed
- **PaddleOCR** is installed via pip:
  ```bash
  pip install paddleocr
  ```
  - For GPU support (optional): Install PaddlePaddle GPU version first
  - For PDF output support (optional):
    ```bash
    pip install img2pdf
    ```
- `pdftoppm` from the Poppler tools is installed
  - For Windows: Download from http://blog.alivate.com.au/poppler-windows/
  - For Linux: `sudo apt-get install poppler-utils` (Debian/Ubuntu) or `sudo yum install poppler-utils` (CentOS/Fedora)
  - For Mac: `brew install poppler`

---

Zotero must be installed using one of the officially supported methods https://www.zotero.org/support/installation#how_do_i_install_zotero. Flatpak/Snap/Appimage and similar set-ups are not supported: Zotero-OCR will not work with them in general, as such architectures prevent it from accessing the Python, PaddleOCR, and pdftoppm tools. Skilled users might get them to work on their own machines but we cannot help with that.


## Installation

To install the extension:

### Option 1: Using Pixi (Recommended)

1. **Install Pixi** (if not already installed):
   ```bash
   # Linux/macOS
   curl -fsSL https://pixi.sh/install.sh | bash
   
   # Windows (PowerShell)
   iwr -useb https://pixi.sh/install.ps1 | iex
   ```

2. **Clone or download this repository**:
   ```bash
   git clone https://github.com/Menghan-W/zotero-ocr_PaddleOCR.git
   cd zotero-ocr_PaddleOCR
   ```

3. **Install all dependencies**:
   ```bash
   pixi install
   ```

4. **Install pdftoppm** (see Prerequisites section above)

5. **Configure Zotero plugin**:
   - Download the XPI file of the [latest release](https://github.com/Menghan-W/zotero-ocr_PaddleOCR/releases).
   - In Zotero:
     - **Zotero 7**: Tools → Plugins → Drag the .xpi onto the Plugins Manager window
     - **Zotero 6**: Tools → Add-ons → Drag the .xpi onto the Add-ons window → Restart Zotero
   - In plugin settings:
     - **Python Path**: Set to `<project-dir>/.pixi/envs/default/bin/python` (Linux/Mac) or `<project-dir>\.pixi\envs\default\python.exe` (Windows)
     - **PaddleOCR Wrapper Path**: Set to `<project-dir>/src/paddleocr_wrapper.py`
     - **pdftoppm Path**: Usually auto-detected

### Option 2: Manual Installation

1. **Install prerequisites:**
   - Install Python 3.7+ from https://www.python.org/downloads/
   - Install PaddleOCR: `pip install paddleocr`
   - (Optional) For PDF output: `pip install img2pdf`
   - Install pdftoppm (see Prerequisites section above)

2. **Install the wrapper script:**
   - Download `paddleocr_wrapper.py` from the [plugin repository](https://github.com/Menghan-W/zotero-ocr_PaddleOCR/blob/main/src/paddleocr_wrapper.py)
   - Place it in one of these locations:
     - Your Zotero data directory (find it in Zotero → Preferences → Advanced → Files and Folders)
     - `/usr/local/bin/` (Linux/Mac)
     - `C:\Program Files\Zotero\` (Windows)
   - Or place it anywhere and set the path in the plugin preferences

3. **Install the plugin:**
   - Download the XPI file of the [latest release](https://github.com/Menghan-W/zotero-ocr_PaddleOCR/releases).
   - Install the XPI depending on your Zotero version:

#### Zotero 7 users
* In Zotero, go to Tools → Plugins and drag the .xpi onto the Plugins Manager window.
* Possibly, adjust the paths to Python, PaddleOCR wrapper script, and pdftoppm in the Zotero OCR section of the Zotero settings.

#### Zotero 6 users

* In Zotero, go to Tools → Add-ons and drag the .xpi onto the Add-ons window.
* Possibly, adjust the paths to Python, PaddleOCR wrapper script, and pdftoppm in the add-on options.
* Restart Zotero to activate Zotero OCR.

Zotero 7 was officially released in August 2024, with important changes over Zotero 6. Support for version 6 will stop at some point in the near future, please consider upgrading.


## Configuration

The configuration can be accessed under Zotero → Settings (Zotero 7) or Tools → Zotero OCR Preferences (Zotero 6).

By default, the fields for the paths to Python, PaddleOCR wrapper script, and pdftoppm are empty, which means that standard locations are searched. If that does not work, then you should locate the tools on your local machine and enter the full paths.

**Important settings:**
- **Python Path**: Leave empty to auto-detect, or specify the full path to your Python executable
- **PaddleOCR Wrapper Path**: The path to `paddleocr_wrapper.py` (see Installation section)
- **pdftoppm Path**: Leave empty to auto-detect, or specify the full path

The default language/script to use with PaddleOCR is "ch" (Chinese and English). You can change it to other supported languages like "en" (English only), "fr" (French), "german", "japan" (Japanese), "korean", etc. See [PaddleOCR documentation](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_en/multi_languages_en.md) for a full list of supported languages.

The user may:
* modify the output DPI (by default: 300)
* choose to add the new PDFs as normal attachments or as linked files. Starting with Zotero-OCR 0.8.0, the default is normal attachments, due to some drawbacks with linked files (not possible in group libraries, unwanted files remaining when a user moves attachments to the Trash...).


![Zotero OCR Preferences](./screenshots/Zotero-OCR-Preferences.png)

Moreover, these options are saved as Zotero preferences variables, which are also available through the [Config Editor](https://www.zotero.org/support/preferences/advanced).


## Zotero OCR for beginners

You can start Zotero OCR using the context menu for your PDF in Zotero:

![Start the plugin](./screenshots/pdfselection.png)

The plugin will take some time to process your PDF (one single page can take several seconds), be patient. If your PDF didn't have a parent item (https://www.zotero.org/support/kb/library_items), Zotero OCR will immediately create one to ensure that its output file will be clearly associated with your PDF. The parent item is where you can enter proper metadata for your PDF, which will facilitate proper Zotero citations if you need them.

After processing, Zotero OCR will attach its output files to the parent item. Using the default settings, you will obtain:
* HTML attachments for the first 5 pages of the PDF (listed as page-1, page-2, etc.). This is mostly useful to verify that PaddleOCR has been executed properly.
* A copy of your original PDF with `.ocr` added to the name. This is the final output.


![It worked!](./screenshots/after-ocr.png)

The default Zotero OCR settings are intended to facilitate troubleshooting, and you might prefer to save some space. When you feel confident that everything is working, you may change your Zotero OCR settings to produce fewer intermediate files and attachments:
* HTML/hocr files and intermediate images can be unselected without any risk.
* Overwriting the initial PDF with the output can be convenient, in particular it will usually ensure that the attachment with a text layer will be the main one for your Zotero reference. However, you might lose your PDF if something goes wrong (possible, even if unlikely) - caution is advised.


## Development, build and release

Regular users do not need to read this section.

Developers can build a new extension file by running `./build.sh [VERSION]`.
It will ask for a version if no version was given on the command line.
Then in Zotero install the newly created `.xpi`-file. as described in the Installation section.

If any error occurs then you will see more details in the `Help`, `Report Error...` dialog. For some debugging messages you can activate in Zotero the debugging in the `Help`, `Debug Output Logging`.

For a new release, run the script `release.sh`.
It runs the `build.sh` script, commits the code changes for the new release and adds a tag.
Push the updated local master branch and the tag to GitHub.
Then publish a [new release on GitHub](https://github.com/UB-Mannheim/zotero-ocr/releases/new) and attach the `.xpi` file there.


## License

Zotero OCR is free and Open Source software.
The source code is released under [GNU Affero General Public License v3](LICENSE).
