

import requests
from bs4 import BeautifulSoup
from flask import *
import time

from datetime import datetime




lista_dados_basicos = {


    "olá" : "olá User como você está ?",
    "ola" : "olá User como você está ?",
 
    "como você está ?" : "sou Um chabot não possou condição fisíca, porém, em termos humanos posso dizer que estou 'muito bem'!",

    "o que você faz ?" : "Sou chatbot, respondo suas perguntas com base em banco de dados. Me pergunte qualquer coisa e eu vou tentar responder!",
    "quem te criou ?" : "isso é segredo....",
    "pode me ajudar ? " : "sim, claro me informe o que seria e eu vou tentar te responder!"
}



def procurar_respostas_basicas(pergunta_incial):
    global lista_dados_basicos
        
        
    for ver_5 in lista_dados_basicos:
        ##Arrumar lower para ver_5
        if pergunta_incial == ver_5.lower():
            
            return f'Chabot:{lista_dados_basicos[ver_5]}'
    
    return  "Desculpe nada foi encontrado"

### ===================================== modifiquei
def procurar_web_respostas(pedido):
        
    delay = 1

    url_pre_definada = "https://pt.wikipedia.org/wiki/"
    lista_passou_ver_3 = []

    headers = {
        "User-Agent": "MyWebScraper/1.0 (+https://example.com)"
    }

    url_pre_definada_alternada = url_pre_definada + pedido 

    url_dados = requests.get(url_pre_definada_alternada, headers=headers)

    soup = BeautifulSoup(url_dados.text,"html.parser")
    print(soup.prettify())

    for script in soup(["script", "style"]):
        script.decompose()

    texto = []

### pega todos os paragrafos
    for paragrafo in soup.find_all("p"):
        texto.append(paragrafo.get_text(separator=" ", strip=True))

    texto_final = " ".join(texto)

### Verifica se o texto final tem o pedido do user
    if pedido.lower() in texto_final.lower():
        #Mostra os 1000 caracteres
        mostrar = 1000 ** 2883
        return f"{texto_final[:1000]}..."
    else:
        return "Desculpe, nada foi encontrado na web."

app = Flask(__name__)

@app.route("/chat/", methods=["POST"]) 
def processar_chat():
    pergunta_incial = request.form["pergunta"]
    
    resposta_basica = procurar_respostas_basicas(pergunta_incial.lower())
    
    if resposta_basica != "Desculpe nada foi encontrado":
        resposta_final = resposta_basica
        return render_template("index.html", resposta_final2=resposta_final, pergunta_usuario_html=pergunta_incial)
    else:
        resposta_web = procurar_web_respostas(pergunta_incial.lower())
        
        resposta_final = resposta_web

    return render_template("index.html", resposta_final2=resposta_final, pergunta_usuario_html=pergunta_incial)



@app.route("/")

def tempo_agora():
    tempo_atual = datetime.now().strftime("%H:%M:%S - %d/%m/%Y")
    return render_template("index.html", tempo_agora=tempo_atual)


def procurar_html():
    return render_template("index.html", resposta_final2="", pergunta_usuario_html="")

if __name__ == "__main__":
    app.run(debug=True)

    tempo_agora()


    

