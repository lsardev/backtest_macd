import PyPDF2
import os
from showpdf import generate_pdf

def merge_pdf(arquivo_saida, *arquivos_entrada):
    
    pdf_merger = PyPDF2.PdfMerger()

    for arquivo in arquivos_entrada:
        with open(arquivo, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(arquivo_saida, 'wb') as pdf_output:
        pdf_merger.write(pdf_output)

def create_paste_years(ticker):
    if __name__ == "__main__":

        pdfs_list = []
        for year in range(2018, 2023):
            pdf_year = generate_pdf("{}-{}".format(ticker, year), ticker, year)
            pdfs_list.append(pdf_year)

        pasta_pdf = "pdfs"

        file1 = pdfs_list[0]
        file2 = pdfs_list[1]
        file3 = pdfs_list[2]
        file4 = pdfs_list[3]
        file5 = pdfs_list[4]

        print(file1)

        road1 = os.path.join(pasta_pdf, file1)
        road2 = os.path.join(pasta_pdf, file2)
        road3 = os.path.join(pasta_pdf, file3)
        road4 = os.path.join(pasta_pdf, file4)
        road5 = os.path.join(pasta_pdf, file5)

        pdfs_full = 'pdfs_2018-2022'
        exit_file = "{}_2018-2020.pdf".format(ticker)

        path_exit_file = os.path.join(pdfs_full, exit_file)

        merge_pdf(path_exit_file, road1, road2, road3, road4, road5)

create_paste_years("VALE3")

