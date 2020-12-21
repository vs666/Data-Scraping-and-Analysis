from tabula import read_pdf

fn = input('Enter filename : ')
df = read_pdf(fn,pages="all",guess=True,multiple_tables=True,)
print(df)