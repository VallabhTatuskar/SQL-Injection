from flask import Flask, render_template, request
import requests
import hashlib

app = Flask(__name__, template_folder='templates', static_folder='static')

def check_if_pwned(email):
    sha1_hash = hashlib.sha1(email.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]

    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    if response.status_code != 200:
        raise Exception("Error fetching data from Have I Been Pwned API.")

    hashes = response.text.splitlines()
    for line in hashes:
        h, count = line.split(':')
        if h == sha1_hash[5:]:
            return True, count
    return False, 0

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        pwned, count = check_if_pwned(email)
        return render_template('result.html', email=email, pwned=pwned, count=count)
    return render_template('index.html')

@app.route('/how-it-works')
def how_it_works():
    return render_template('how-it-works.html')

@app.route('/data')
def data():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)