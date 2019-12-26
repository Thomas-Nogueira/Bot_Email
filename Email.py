tradutor
from flask import Flask
from flask_mail import Mail, Message
import csv
import os
app = Flask(__name__)

def sendEmail(recipient):
    mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',      #Email server
        "MAIL_USE_TLS": False,            #Transport Layer Security
        "MAIL_USE_SSL": True,             #Secure Sockets Layer
        "MAIL_PORT": 465,                 #For using SSL
        "MAIL_USERNAME": 'EMAIL',         #Location for entering sender email
        "MAIL_PASSWORD": 'SENHA DO EMAIL' #Location to enter sender email password
    }
    app.config.update(mail_settings)
    mail = Mail(app)

    if __name__ == '__main__':
        with app.app_context():
            msg = Message(sender=app.config.get("MAIL_USERNAME"),recipients=[recipient])
            msg.subject = " MESSAGE TITLE "
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
                    <img src="https://static.significados.com.br/foto/paisagem-natural-significados.jpg" alt= "Boas Festas">
                </td>
            </tr>

    </table>
    </table>

    </body>
    </html>

    """
            mail.send(msg)

# FOR EMAILS LIMITED SHIPPING USE THE BELOW FUNCTION.
#                       \|/             

# STORE AND LIST ARRAY OF RECIPIENTS
list_emails = ['EMAIL RECIPIENT', 'EMAIL RECIPIENT']

for email in list_emails:
    sendEmail(email)

# FOR EMAILS UNLIMITED SHIPPING USE THE FUNCTION BELOW. 
#                       \|/ 
# UNCOMPRESSED FUNCTION.

# LOAD CSV FILE DATA AND READ ALL EMAILS THAT ARE CONTAINED IN THE FILE FOR AUTOMATED SENDING MESSAGES.
# file = open('file.csv')
# list_emails = csv.reader(file)
# for recipients in list_emails:
#    sendEmail(recipients[0])
#    print(recipients)

        	
