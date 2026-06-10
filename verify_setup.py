from pathlib import Path

import fitz
import matplotlib
import numpy
import openpyxl
import pandas as pd
import tqdm
from IPython.display import display


root = Path(__file__).resolve().parent
notebook = root / "PDF-countier.ipynb"
dictionary = root / "term_dictionary.xlsx"
pdf_dir = root / "PDF"

missing = [path.name for path in [notebook, dictionary, pdf_dir] if not path.exists()]
if missing:
    raise SystemExit(f"Missing required paths: {', '.join(missing)}")

pdf_files = sorted(pdf_dir.glob("*.pdf"))
if not pdf_files:
    raise SystemExit("PDF directory does not contain PDF files")

with fitz.open(pdf_files[0]) as doc:
    first_pdf_pages = len(doc)

terms = pd.read_excel(dictionary, sheet_name="terms", dtype=str).fillna("")
required_columns = {"level", "label", "aliases"}
missing_columns = required_columns - set(terms.columns)
if missing_columns:
    raise SystemExit(f"Missing dictionary columns: {', '.join(sorted(missing_columns))}")

nonempty_terms = int(((terms["level"] != "") & (terms["label"] != "")).sum())

print("Setup check passed")
print(f"PDF files: {len(pdf_files)}")
print(f"Dictionary terms: {nonempty_terms}")
print(f"First PDF pages: {first_pdf_pages}")
