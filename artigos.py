import requests, random
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas

arquivo = open('lista.txt','r')
lista = []

def GerarArtigo():
	global arquivo,lista
	numero = random.randint(0,106)

	for linha in arquivo:
		lista.append(linha)

	link = 'https://pt.wikipedia.org/wiki/'+ lista[numero].strip()
	re = requests.get(link)
	soup = BeautifulSoup(re.text,'html.parser')
	titulo = soup.find(id="firstHeading")
	print(titulo.text)
	texto = soup.find(id="bodyContent")
	pdf = canvas.Canvas('artigos/'+titulo.text+'.pdf')
	y = 800
	pdf.drawString(100,y, str(titulo.text))

	textoLinha = ""
	contador = 0
	for letra in texto.text:
		textoLinha = textoLinha +  letra
		if contador >= 87:
			contador = 0
			y -= 20
			pdf.drawString(10,y,textoLinha)
			textoLinha = ""
		if y <= 20:
			pdf.showPage()
			y = 800
		contador +=1
	pdf.save()

GerarArtigo()


