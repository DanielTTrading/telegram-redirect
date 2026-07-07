from flask import Flask, request

app = Flask(__name__)

@app.route('/telegram')
def telegram_redirect():
    user_agent = request.headers.get('User-Agent', '').lower()
    
    if 'android' in user_agent:
        store_link = "https://play.google.com/store/apps/details?id=org.telegram.messenger"
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
        </style>
    </head>
    <body>
        <p>Abriendo Telegram...</p>
        <p style="font-size:14px;">Si no tienes la app instalada, se abrirá la tienda automáticamente.</p>
        <a class="btn" href="{store_link}">Descargar Telegram</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)