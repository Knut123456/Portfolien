from flask import render_template, Flask
app = Flask(__name__)

@app.route('/Knut sin nettside')
def index():
    return render_template('index.html')

@app.route('/Knut sin nettside/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/Knut sin nettside/CV')
def portfolio():
    return render_template('portfolio.html')


if __name__ == '__main__':
    app.run(debug=True)
