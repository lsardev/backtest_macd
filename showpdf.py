import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from get_price_graphic import show_price_graphic
from get_graphic_history import get_trade_history
from return_pct import get_pct_year

def generate_pdf(output_file, ticker, year):

    pdf_folder = "pdfs"
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    output_path = os.path.join(pdf_folder, output_file + ".pdf")
    doc = SimpleDocTemplate(output_path, pagesize=letter)


    #centralizando paragrafo
    def draw_centered_string(c, text, y):
        width = c.stringWidth(text, "Helvetica", 12)
        x = (letter[0] - width) / 2
        c.drawString(x, y, text)

    c = canvas.Canvas(output_path)

    #Título do texto
    paragraph_text = "Análise da estratégia MACD na ação {} no ano {}".format(ticker, year)
    draw_centered_string(c, paragraph_text, 800)

    #Imagem
    caminho_arquivo = show_price_graphic(ticker, year)
    c.drawImage(caminho_arquivo, 100, 400, width=400, height=300)    

    #Todos os trades
    c.setFont("Helvetica", 12)
    c.drawString(100, 300, "Trades realizados nos sinais:")
    all_trades = get_trade_history(ticker, year)

    height = 280

    c.setFont("Helvetica", 9)
    for trade in all_trades:
        compra = trade[0]
        venda = trade[1]
        pct = trade[2]

        string = "Comprado a {:.2f}, vendido a {:.2f} - Porcentagem {:.2f}%".format(compra, venda, pct)

        c.drawString(100, height, string)
        height -= 20

    pct = get_pct_year(ticker, year)

    c.setFont("Helvetica", 12)
    c.drawString(100, height-20, "Crescimento anual de {}: {}".format(year, pct))

    c.save()


generate_pdf("pdf_example_26", "VALE3", "2022")