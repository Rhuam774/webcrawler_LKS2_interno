import re
import requests
from os import system
def L():
    try:
        system("clear")
    except:
        None
def lg():
    print('\n*******************************webC2******************************\n')
#=====================================================================================================
L()
lg()
print('Digite o numero correnpondente a sua necessidade:')
escolha1 = input('\n1 - Encontrar diretorios(se tiver)\n2 - Encontrar subdominios e links contidos na paginas\n\ndigite um numero:')
L()
lg()
url = input("digite a URL:")
lg()
L()
pagina = requests.get(url).text
arquivo = open("texto.txt","w+")
arquivo.write(pagina)
arquivo.close()
texto = open("texto.txt","r")
texto_links = open("links1.txt", "w")
try:
    if escolha1 == '1':
        for lin in texto:
            links = re.findall(r"\w+\/[\w-]*.[\w\/-]*.\w+", lin)
            if len(links) == 0:
                None
            else:
                links = str(links)
                fil_links1 = links.replace("'", "")
                fil_links2 = fil_links1.replace("[", "")
                fil_links3 = fil_links2.replace("]", "")
                fil_links4 = fil_links3.replace(",", "\n")
                fil_links5 = fil_links4.replace(" ", "")
                texto_links.write(fil_links5+'\n') 
                print(fil_links5)
    elif escolha1 == '2':
        for lin in texto:
            links = re.findall(r"http[\w*://.-]+", lin)
            if len(links) == 0:
                None
            else:
                links = str(links)
                fil_links1 = links.replace("'", "")
                fil_links2 = fil_links1.replace("[", "")
                fil_links3 = fil_links2.replace("]", "")
                fil_links4 = fil_links3.replace(",", "\n")
                fil_links5 = fil_links4.replace(" ", "")
                texto_links.write(fil_links5+'\n') 
                print(fil_links5)
except Exception as erro:
    print(f'erro: {erro}')
