from flask import Flask
from flask_mail import Mail, Message
import csv
import os
app = Flask(__name__)

def enviarEmail(destinatario):
    mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com', 
        "MAIL_USE_TLS": False, #Transport Layer Security
        "MAIL_USE_SSL": True,  #Secure Sockets Layer
        "MAIL_PORT": 465,        #For using SSL
        "MAIL_USERNAME": 'EMAIL',
        "MAIL_PASSWORD": 'SENHA DO EMAIL'
    }
    app.config.update(mail_settings)
    mail = Mail(app)

    if __name__ == '__main__':
        with app.app_context():
            msg = Message(sender=app.config.get("MAIL_USERNAME"),recipients=[destinatario])
            msg.subject = " TÍTULO DA MENSAGEM "
            msg.html =  """   
            
    <!DOCTYPE html>
    <html>
    <head>
        <title>Email Template</title>
        <link href="https://fonts.googleapis.com/css?family=Niramit" rel="stylesheet">
        <style>
            .paragraph{
        font-family: 'Niramit', sans-serif;
        font-style: 50px

    }
    .button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }

    .button3 {background-color: #f44336;} /* Red */ 

        </style>
     
    </head>
    <body style="margin: 0; ">
        
        <table align="center" border="0" cellpadding="20" cellspacing="0" >
            <tr><td>
        <table align="center" border="0" cellspacing="0" width="300">
            <tr>
                <td align="center">   
                    <img src="https://a-static.mlcdn.com.br/618x463/quadro-decorativo-canvas-p-salas-quartos-escritorios-paisagem-por-do-sol-i-incasa-design/incasadesign/cv0093pab/e15259fcdb2c77531ccea6d5e799ef5c.jpg" alt= "Boas Festas">
                </td>
            </tr>

    </table>
    </table>

    </body>
    </html>

    """
            mail.send(msg)

# FUNÇÃO QUE ENVIA UM ARRAY DE DESTINATÁRIO
lista_emails = ['EMAIL DESTINATÁRIO', 'EMAIL DESTINATÁRIO']
#'joao.dvlp@gmail.com','joao.victor@omnicontract.kinghost.net', 
for email in lista_emails:
    enviarEmail(email)

# CARREGA OS DADOS DO ARQUIVO CSV
# arquivo = open('emails_crn_enviados.csv')

# lista_emails = csv.reader(arquivo)

# for destinatario in lista_emails:
#    enviarEmail(destinatario[0])
#    print(destinatario)

        	
