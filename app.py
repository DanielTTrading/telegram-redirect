from flask import Flask

app = Flask(__name__)

@app.route('/telegram')
def telegram_redirect():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <script>
          window.location.href = "tg://resolve?domain=Jptactical_bot";
        </script>
    </head>
    <body></body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)