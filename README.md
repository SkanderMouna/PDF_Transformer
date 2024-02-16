# PDF Transformer

## Overview

This Python project is designed to enhance the usability of lecture PDFs provided by the university. It takes a PDF file as input, groups every three pages together, and adds a stripped line as a background. This modified PDF can be seamlessly integrated into note-taking apps like GoodNotes, allowing ample space for additional comments.

## Features

- Splits the input PDF into sets of three pages.
- Adds a stripped line background for better note-taking.
- Resizes pages for improved integration with note-taking apps.
- Utilizes the PyMuPDF library for PDF manipulation.

## Usage

1. Ensure you have Python installed on your machine.
2. Install the required library by running: `pip install PyMuPDF`.
3. Place the PDF file you want to process in the same directory as `main.py` and name it `input.pdf`.
4. Run the script: `python main.py`.
5. Find the transformed PDF as `output.pdf` in the same directory.

## Note

This project is a personal solution to enhance the usability of lecture materials. It may require adjustments depending on the structure of your PDFs.

Enjoy a more interactive note-taking experience!
