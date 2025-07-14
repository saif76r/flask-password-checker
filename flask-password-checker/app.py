
from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])
    if length < 6:
        strength = "Very Weak"
    elif length < 8:
        strength = "Weak"
    elif score >= 3 and length >= 8:
        strength = "Strong"
    else:
        strength = "Medium"

    return strength

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    password = ''
    if request.method == 'POST':
        password = request.form.get('password', '')
        strength = check_password_strength(password)
    return render_template('index.html', strength=strength, password=password)

if __name__ == '__main__':
    app.run(debug=True)
