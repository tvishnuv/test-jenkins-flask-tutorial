from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is Git + Docker + Jenkins CI/CD to Hybrid 0850PM'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
