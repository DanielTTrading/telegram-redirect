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
          window.location.href = "tg://resolve?domain=Jptactical_bot";
          setTimeout(function() {
            window.location.href = "https://t.me/Jptactical_bot";
          }, 1500);
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
            p { color: #aaa; }
            .manual {
                margin-top: 30px;
                font-size: 14px;
                color: #888;
            }
            .manual b { color: #2AABEE; }
        </style>
    </head>
    <body>
        <p>Abriendo Telegram...</p>
        <div class="manual">
            ¿No abrió? Abre tu app de Telegram y busca:<br>
            <b>@Jptactical_bot</b>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)