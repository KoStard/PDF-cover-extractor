# PDF Cover Extractor

This Python script extracts the first page of one or more PDF files and saves it as a PNG image file with the same name as the input PDF file.

## Before you run the script

- You need Python 3.x
- `sudo apt-get install poppler-utils`
- If you want to use a virtual environment (optional): `python3 -m venv venv` and `source venv/bin/activate`
- `pip install -r requirements.txt`

## Usage

To extract the cover photo from a PDF file, run the script with the file name as an argument:

```
python PDF_cover_extractor.py input_file.pdf
```

To extract the cover photos from multiple PDF files, provide the file names as multiple arguments:

```
python PDF_cover_extractor.py input_file1.pdf input_file2.pdf input_file3.pdf
```

The script will extract the first page of each PDF file and save it as a PNG image file with the same name as the input PDF file, but with the `.png` file extension.

## Acknowledgements

This script uses the `pdf2image` package to convert PDF pages to images and the `PyPDF2` package to read input PDF files and write output PDF files. It also uses the `argparse` module to parse command-line arguments.

## License

This script is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed.
