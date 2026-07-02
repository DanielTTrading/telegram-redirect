from flask import Flask

app = Flask(__name__)

@app.route('/telegram')
def telegram_redirect():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Abrir Telegram</title>
        <script>
          window.location.href = "https://t.me/Jptactical_bot";
        </script>
        <style>
            body {
                font-family: -apple-system, sans-serif;
                background: #1a1a2e;
                color: white;
                text-align: center;
                padding: 40px 20px;
                margin: 0;
            }
            h2 {
                margin-bottom: 10px;
            }
            p {
                color: #aaa;
                margin-bottom: 30px;
            }
            .btn {
                display: block;
                background: #2AABEE;
                color: white;
                text-decoration: none;
                padding: 16px;
                border-radius: 12px;
                margin: 12px auto;
                max-width: 320px;
                font-weight: bold;
                font-size: 16px;
            }
            .btn.secondary {
                background: #333;
            }
            .manual {
                margin-top: 30px;
                font-size: 14px;
                color: #888;
            }
            .manual b {
                color: #2AABEE;
            }
        </style>
    </head>
    <body>
        <h2>Abriendo Telegram...</h2>
        <p>Si no abre automáticamente, elige una opción:</p>

        <a class="btn" href="https://t.me/Jptactical_bot">Abrir en Telegram</a>
        <a class="btn secondary" href="https://web.telegram.org/k/#@Jptactical_bot">Abrir en Telegram Web</a>

        <div class="manual">
            ¿Sigue sin funcionar? Abre tu app de Telegram y busca:<br>
            <b>@Jptactical_bot</b>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)