from flask import Flask,request,jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

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

@app.route('/send_emails',methods=['POST'])
def send_emails():
    data=request.get_json();
    recipients = [data['email']]
    subject = 'Contact Form details from Devesh Mehta'
    text_body = 'Dear '+data['name']+',Thanks for contacting me.'
    html_body = '<div style="font-size: 20px;"><div>Dear '+data['name']+',</div><p>     \tThanks for contacting me. I hope you would liked my portfolio. Details regarding contact form is given here. I\'ll contact you soon regarding the same.</p><table cellspacing="20px"><tr><td>Name:</td><td>'+data['name']+'</td></tr><tr><td>Organization:</td><td>'+data['org']+'</td></tr><tr><td>Email:</td><td>'+data['email']+'</td></tr><tr><td>Phone:</td><td>'+data['phone']+'</td></tr><tr><td>Query:</td><td>'+data['msg']+'</td></tr></table><p>I\'ll try to reply as soon as possible. Again thanks to visit my portfolio website.</p><div>Devesh Chetan Mehta</div></div>'
    # table='<table cellspacing="20px"><tr><td>Name:</td><td>'+data['name']+'</td></tr><tr><td>Organization:</td><td>'+data['org']+'</td></tr><tr><td>Email:</td><td>'+data['email']+'</td></tr><tr><td>Phone:</td><td>'+data['phone']+'</td></tr><tr><td>Query:</td><td>'+data['msg']+'</td></tr></table>'

    send_email(subject, recipients, text_body, html_body)
    send_email('Portfolio Form Detail', 'devesh1217@yahoo.com', text_body, html_body)
    
    return jsonify(data)
