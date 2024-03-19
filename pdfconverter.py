from fpdf import FPDF

def writepdf():
    title=input('Enter Title: ')
    body=input('Enter Text: ')
    filename=input('Enter Filename to Save: ')
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial','B',20)
    pdf.cell(w=0,h=10,txt=title,ln=1,align='C')
    pdf.set_font('Arial',size=15)
    pdf.multi_cell(w=200,h=10,txt=body,align='L')
    pdf.output(filename)
    print('Completed Successfully...')

def convertpdf():
    filename1=input('Enter Text Filename: ')
    filename2=input('Enter Filename to Save PDF: ')
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial',size=15)
    with open(filename1,'r') as file:
        for line in file:
            pdf.cell(200,10,txt=line,ln=1,align='L')
    pdf.output(filename2)
    print('Completed Successfully...')

try:
    print('1.Write to PDF\n2.Convert to PDF')
    choice=int(input('Enter your Choice: '))
    if choice==1:
        writepdf()
    elif choice==2:
        convertpdf()
    else:
        print('Invalid Choice...')
except:
    print('Invalid Input...')