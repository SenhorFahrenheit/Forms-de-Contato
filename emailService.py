from flask import Flask
from flask_mail import Mail, Message
from config import Config  # Importa a configuração

# Inicializando o app e o Mail
app = Flask(__name__)
app.config.from_object(Config)  # Carrega configurações do config.py
mail = Mail(app)

def send_email(subject, recipient, body):
    """Função para enviar um e-mail."""
    try:
        with app.app_context():  # Garante que estamos no contexto do Flask
            msg = Message(
                subject=subject,
                sender=app.config.get('MAIL_USERNAME'),  # Evita erro se a variável não existir
                recipients=[recipient]
            )
            msg.body = body  # Define o corpo do e-mail

            mail.send(msg)  # Envia o e-mail
        
        return "E-mail enviado com sucesso!"
    except Exception as e:
        return f"Erro ao enviar o e-mail: {e}"
