from urllib.parse import urlencode
import qrcode


# Função para criar QR code a partir de uma URL
def criar_qr_code(url, nome_arquivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nome_arquivo)

# Solicita ao usuário para escolher o serviço desejado
servico = input("Escolha o serviço (youtube, twitter, telegram, facebook, instagram, snapchat, zypher, reditt, twitch, whatsapp, google, github, linkedin, ): ").lower()

# Solicita ao usuário para inserir os dados
dados = {
    'nome': input("Insira o nome: "),
    'idade': input("Insira a idade: "),
    'cidade': input("Insira a cidade: "),
}

# Variáveis para os diferentes serviços
url_bases = {
    'youtube': 'https://www.youtube.com/',
    'twitter': 'https://twitter.com/',
    'telegram': 'https://web.telegram.org/',
    'facebook': 'https://www.facebook.com/',
    'instagram': 'https://www.instagram.com/',
    'snapchat': 'https://www.snapchat.com/',
    'zypher': 'https://www.zypher.com/',
    'reddit': 'https://www.reddit.com/',
    'twitch': 'https://www.twitch.tv/',
    'whatsapp': 'https://web.whatsapp.com/',
    # Adicione mais serviços conforme necessário
}

# Verifica se o serviço escolhido existe nas opções
if servico in url_bases:
    url_base = url_bases[servico]
else:
    print("Serviço não reconhecido. Usando URL padrão.")
    url_base = 'https://exemplo.com/'

# Transforma os dados em uma URL
url_formatada = urlencode(dados)
url_final = url_base + 'pagina?' + url_formatada

# Cria o QR code com a URL
nome_arquivo_qr_code = 'qr_code.png'
criar_qr_code(url_final, nome_arquivo_qr_code)

# Exibe informações para o usuário
print(f"URL gerada: {url_final}")
print(f"QR code gerado e salvo como {nome_arquivo_qr_code}")
#creador kaka 

