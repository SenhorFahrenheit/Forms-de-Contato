from flask import Flask, request, render_template    
from emailService import send_email

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        email_data = {
            'sender': request.form['nome'],
            'recipient': request.form['email'],
            'message': request.form['mensagem'],
            'subject': request.form['assunto']
        }


        # Enviar o e-mail
        resultado = send_email(
            subject=email_data['subject'],
            recipient=email_data['recipient'],
            body=email_data['message']
        )
        if resultado == 'E-mail enviado com sucesso!':
            return render_template("success.html")
        else:
            return render_template("error.html")
        
if __name__ == '__main__':
    app.run(debug=True)
