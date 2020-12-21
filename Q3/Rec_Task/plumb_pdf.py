import pdfplumber


pdf = pdfplumber.open("a6b29367-f3b7-4fb1-a2d0-077477eac1d9.pdf")
page = pdf.pages[0]
tab = page.extract_table()

print(tab)