# Chatbot PY

Aplicação web Flask com interface em português e busca de respostas no backend.

## Executar localmente

```powershell
python -m pip install -r requirements.txt
python Chabot_backend.py
```

Abra <http://127.0.0.1:5000/> no navegador.

## Estrutura

```text
.
├── Chabot_backend.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── app.js
    └── media/
        └── Animation_Start.mp4
```

Ao acessar `/`, a introdução tenta reproduzir automaticamente, sem áudio e em modo
inline, os dois segundos iniciais de `Animation_Start.mp4` e então redireciona para
`/chat/`. Se o navegador bloquear a reprodução, é possível iniciá-la por um botão; se
o arquivo não carregar, outro botão permite continuar sem o vídeo. A página principal
também pode ser acessada diretamente em `/chat/`.
