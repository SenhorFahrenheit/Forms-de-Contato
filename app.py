from flask import Flask, render_template

# Inicializa a aplicação Flask
app = Flask(__name__)

# Rota principal
def index():
    return render_template("index.html")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    app.run(debug=True)
