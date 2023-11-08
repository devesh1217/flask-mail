from flask import Flask,request
from flask_mail import Mail, Message
app=Flask(__name__)

@app.route('/')
def api():
    return 'devesh mehta'

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Use the appropriate port for your email provider
app.config['MAIL_USE_TLS'] = True  # Use TLS for security
app.config['MAIL_USE_SSL'] = False  # Don't use SSL if you're using TLS
app.config['MAIL_USERNAME'] = 'u22cs035@coed.svnit.ac.in'
app.config['MAIL_PASSWORD'] = 'medphquozgeiijlt'

mail = Mail(app)

def send_email(subject, recipients, text_body, html_body=None):
    msg = Message(subject, sender='u22cs035@coed.svnit.ac.in', recipients=recipients)
    msg.body = text_body
    if html_body:
        msg.html = html_body
    mail.send(msg)

@app.route('/send_emails')
def send_emails():
    data=request.get_json();
    recipients = [data['email']]
    subject = 'Dear '+data['name']+', Thanks to conatact.'
    text_body = 'This is a test email from Flask-Mail.'
    html_body = '<p>Dear '+data['name']+', Thanks to conatact.<br><h1>Devesh</h1></p><p>'+data['msg']+'</p>'
    
    send_email(subject, recipients, text_body, html_body)
    
    return 


if __name__ == '__main__':
    app.run()