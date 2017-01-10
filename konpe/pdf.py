import logging
import config
#TODO tidy up imports later

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
#A4 297x210


class GeneratePDF:
    def __init__(self):
        self.canvas = canvas.Canvas("tournament_draws.pdf", pagesize=A4)
    def generate(self):
        self.canvas.setFont("Helvetica", 10)
        self.canvas.drawString(2*cm,28*cm,"Hello World")
        self.canvas.showPage
        self.canvas.save()

if __name__ == '__main__':
    G = GeneratePDF()
    G.generate()
