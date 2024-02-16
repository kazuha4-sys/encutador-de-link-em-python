import pyshorteners


link = input("Insira o link: ")
encutador = pyshorteners.Shortener(links=link)

print(encutador.tinyurl.short(link))
#creador kaka

