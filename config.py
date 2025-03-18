import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.urandom(24)  # Necessário para segurança, pode ser qualquer valor
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME") 
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
