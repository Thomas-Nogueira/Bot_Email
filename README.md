# Bot for Email

According to [Wikipedia](https://pt.wikipedia.org/wiki/Flask_(framework_web)), **Flask** is a small web framework written in Python based on the WSGI Werkzeug library and the Jinja2 library. Flask is available under the terms of the BSD License.

To run this example you need to install [Flask framework](https://flask-ptbr.readthedocs.io/en/latest/installation.html).
```
$ pip install Flask
```
#### This example was based on the article [How to Send Emails with Python](https://medium.com/@sagarsharma4244/how-to-send-emails-using-python-4293dacc57d9) by SAGAR SHARMA.

In this article I will show you a brief explanation of how to use a bot to send emails to different recipients using the python language in conjunction with the Flask framework.

- First of all you need to import libraries to use python's built-in functions.

````
from flask import Flask
from flask_mail import Mail, Message
import csv
import os
````
- Then the necessary information will be added to connect the mail server via smtp and use the sender data information to send the 'login and password' messages.

```
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',      #Email server
        "MAIL_USE_TLS": False,            #Transport Layer Security
        "MAIL_USE_SSL": True,             #Secure Sockets Layer
        "MAIL_PORT": 465,                 #For using SSL
        "MAIL_USERNAME": 'EMAIL',         #Location for entering sender email
        "MAIL_PASSWORD": 'SENHA DO EMAIL' #Location to enter sender email password
}
```
- Creates a variable that receives the information from the sender and the(s) Recipient(s).
```
msg = Message(sender=app.config.get("MAIL_USERNAME"),recipients=[recipient])
```
- Create a variable that stores and then lists an array of recipients for sending messages.

```
list_emails = ['EMAIL DESTINATÁRIO', 'EMAIL DESTINATÁRIO']

for email in list_emails:
    sendEmail(email)
```
- Create a variable that reads csv files and stores information, and then lists an array of recipients for sending messages.

``` 
file = open('file.csv')
list_emails = csv.reader(file)
for recipients in list_emails:
    sendEmail(recipients[0])
        print(recipients)
```



