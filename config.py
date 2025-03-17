import os

class Config:
    SECRET_KEY = os.urandom(24)  # Necessário para segurança, pode ser qualquer valor
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'seu_email@gmail.com'  # Substitua com seu e-mail
    MAIL_PASSWORD = 'sua_senha'  # Substitua com sua senha ou senha do app (se necessário)
