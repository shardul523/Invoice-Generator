from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

invoice_paths = glob.glob("invoices/*.xlsx")

for filepath in invoice_paths:
    df = pd.read_excel(filepath, 'Sheet 1')
    total_price = df['total_price'].sum()

    filename = Path(filepath).stem
    invoice_no, date = filename.split(sep='-')

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=0, h=16, txt=f"Invoice no.{invoice_no}", ln=1)
    pdf.cell(w=0, h=12, txt=f"Date: {date}", ln=1)

    pdf.ln(10)

    width = round(190 / len(df.columns))
    curr_width = width

    pdf.set_font(family="Times", size=10, style='B')

    # Add table headers
    for col in df.columns:
        col_name = col.replace('_', ' ').title()
        pdf.cell(w=width, h=8, txt=col_name, border=True, align='C')
        curr_width += width

    pdf.ln(8)

    # Add table rows

    pdf.set_font(family="Times", size=8)

    for i, row in df.iterrows():
        for col in df.columns:
            pdf.cell(w=width, h=8, txt=str(row[col]), border=True, align='C')
        pdf.ln(8)

    # Add last row for total price

    for _ in range(len(df.columns) - 1):
        pdf.cell(w=width, h=8, txt='', border=True)

    pdf.cell(w=width, h=8, txt=str(total_price), align='C', border=True, ln=1)

    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=0, h=8, txt=f"The total price is {total_price}")

    pdf.output(f"PDFs/Output-{invoice_no}.pdf")
