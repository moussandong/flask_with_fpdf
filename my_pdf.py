#!/usr/bin/python
from flask import Flask, redirect, url_for, request
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

@moussaWebApp.route('/',methods = ['POST', 'GET'])
def home():
	if request.method == 'POST':
		text = request.form['text']
		return redirect(url_for('success',text = text))
	else:
		text = request.args.get('text')
		return redirect(url_for('success',text = text))

if __name__ == '__main__':
	moussaWebApp.run(debug = True)
