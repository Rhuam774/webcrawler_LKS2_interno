import re
import requests

#pagina = requests.get("siteExemple.com").text
#arquivo = open("texto.txt","w+")
#arquivo.write(pagina)
#arquivo.close()
texto = open("texto.txt","r")
texto_links = open("links1.txt", "w")
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

        texto_links.write(fil_links5) 
        print(fil_links5)