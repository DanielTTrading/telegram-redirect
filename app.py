from flask import Flask, request

app = Flask(__name__)

@app.route('/telegram')
def telegram_redirect():
    user_agent = request.headers.get('User-Agent', '').lower()
    
    if 'android' in user_agent:
        # Intenta pasar el bot como "referrer" para que Telegram lo lea al abrir por primera vez
        store_link = "https://play.google.com/store/apps/details?id=org.telegram.messenger&referrer=Jptactical_bot"
    elif 'iphone' in user_agent or 'ipad' in user_agent:
        store_link = "https://apps.apple.com/app/telegram-messenger/id686449807"
    else:
        store_link = "https://telegram.org/dl"
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Abrir Telegram</title>
        <script>
          window.location.href = "tg://resolve?domain=Jptactical_bot";
          setTimeout(function() {{
            window.location.href = "{store_link}";
          }}, 1500);
        </script>
        <style>
            body {{
                font-family: -apple-system, sans-serif;
                background: #1a1a2e;
                color: white;
                text-align: center;
                padding: 40px 20px;
                margin: 0;
            }}
            p {{ color: #aaa; }}
            .btn {{
                display: block;
                background: #2AABEE;
                color: white;
                text-decoration: none;
                padding: 16px;
                border-radius: 12px;
                margin: 20px auto;
                max-width: 320px;
                font-weight: bold;
            }}
            .steps {{
                text-align: left;
                background: #25253d;
                padding: 20px;
                border-radius: 12px;
                margin-top: 30px;
                max-width: 320px;
                margin-left: auto;
                margin-right: auto;
                font-size: 14px;
                line-height: 1.8;
            }}
            .steps b {{ color: #2AABEE; }}
        </style>
    </head>
    <body>
        <p>Abriendo Telegram...</p>
        <p style="font-size:14px;">Si no tienes la app instalada, se abrirá la tienda automáticamente.</p>
        <a class="btn" href="{store_link}">Descargar Telegram</a>

        <div class="steps">
            <b>¿Ya instalaste Telegram y no llegaste al bot?</b><br><br>
            1. Abre la app de Telegram<br>
            2. Toca la lupa (buscar)<br>
            3. Escribe: <b>@Jptactical_bot</b><br>
            4. Toca el bot y dale "Iniciar"
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)