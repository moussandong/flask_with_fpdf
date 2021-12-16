#!/usr/bin/python
import os
from flask import Flask, redirect, url_for, request, make_response
from fpdf import FPDF

moussaWebApp = Flask(__name__)
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)


@moussaWebApp.route('/success/<text>')
def success(text):
	pdf.cell(200, 10, txt =text,
		ln = 1, align = 'C')
	pdf.output("my_text_to_pdf.pdf")
	return 'ton texte est : %s' % text

@moussaWebApp.route('/')
def home():
	return "Bienvenue vous êtes à l'acceuil"

@moussaWebApp.route('/download-pdf',methods = ['POST', 'GET'])
def download_pdf():
	if request.method == 'POST':
		text = request.form['text']
		return redirect(url_for('success',text = text))
	else:
		text = request.args.get('text')
		return redirect(url_for('success',text = text))


@moussaWebApp.route('/jpg_to_pdf/<name>')
def jpg_to_pdf(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(os.path.join(os.getcwd(), name + '.jpg'), 50, 50)
    response = make_response(pdf.output(dest='S').encode('latin-1'))
    response.headers.set('Content-Disposition', 'attachment', filename=name + '.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response

if __name__ == '__main__':
	moussaWebApp.run(debug = True)
