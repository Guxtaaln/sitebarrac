from flask import Flask;

app = Flask(__name__)

@app.route('/')
def index():
    return ''' sitebarra.c ("index.html")
        <html>
            <head>
                <title>Olá, caro amigo!</title>  <!-- Título na aba -->
            </head>
            <body>
                <h1>Olá, caro amigo!</h1>  <!-- Saudação na página -->
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)


