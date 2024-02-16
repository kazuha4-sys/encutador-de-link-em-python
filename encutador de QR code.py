import qrcode as qrc
import pyshorteners

# Adiciona o qrcode com o pyshortener
link = input("Insira o link: ")

# Encurta o link usando o pyshorteners
encurtador = pyshorteners.Shortener()
encurtado = encurtador.tinyurl.short(link)

# Cria o QRCode com o link encurtado
qr = qrc.QRCode(version=1, box_size=10, border=4)
qr.add_data(encurtado)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("youtube2.png")

print("Encurtador: ", encurtado)
#Creador Kaka
