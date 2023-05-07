from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path


invoice_paths = glob.glob("invoices/*.xlsx")

for filepath in invoice_paths:
    df = pd.read_excel(filepath, 'Sheet 1')
    filename = Path(filepath).stem
    invoice_no, date = filename.split(sep='-')

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=0, h=16, txt=f"Invoice no.{invoice_no}", ln=1)
    pdf.cell(w=0, h=12, txt=f"Date: {date}")

    pdf.output(f"PDFs/Output-{invoice_no}.pdf")

