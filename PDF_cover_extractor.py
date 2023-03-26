from pdf2image import convert_from_bytes
from PyPDF2 import PdfWriter, PdfReader
import io
import argparse

# Set up command-line argument parser
parser = argparse.ArgumentParser(
    description='Extract cover photo from PDF file.')
parser.add_argument('input_files',
                    type=str,
                    nargs='+',
                    help='PDF file names to extract cover photos from')
args = parser.parse_args()

# Loop over input files
for input_file in args.input_files:
    print("Extracting cover photo from {}...".format(input_file))

    # Open input PDF file and extract first page
    pdf_reader = PdfReader(input_file)
    first_page = pdf_reader.pages[0]

    # Create output PDF writer and add first page
    pdf_writer = PdfWriter()
    pdf_writer.add_page(first_page)

    # Write output PDF data to memory buffer
    buffer = io.BytesIO()
    pdf_writer.write(buffer)

    # Convert output PDF data to image and save as PNG file
    images = convert_from_bytes(buffer.getvalue())
    output_file = input_file[:-4] + ".png"
    images[0].save(output_file)

    # Print confirmation message
    print("Done, your cover photo has been saved as {}".format(output_file))

    # Close memory buffer
    buffer.close()
