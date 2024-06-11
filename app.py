from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    heart_rate = request.form['heart_rate']
    blood_pressure = request.form['blood_pressure']
    temperature = request.form['temperature']
    
    return render_template('result.html', heart_rate=heart_rate, blood_pressure=blood_pressure, temperature=temperature)

if __name__ == '__main__':
    app.run(debug=True)
