import pdfplumber
def pdf_extraction(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text_code = ""
        for page in pdf.pages:
            text = page.extract_text()
            text_code += text
    return text_code



if __name__ =='__main__':
    with open('text3.txt','w') as file:
        data=pdf_extraction('output\Maulana-Azad-National-Institute-of-TechnologyMore-DetailsClose-\pdf\document.pdf')
        file.write(data)