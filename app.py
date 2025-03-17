from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        Email = {
            'remetente': request.form['nome'],
            'destinatario': request.form['email'],
            'mensagem': request.form['mensagem'],
        }
        return Email
if __name__ == '__main__':
    app.run(debug=True)
