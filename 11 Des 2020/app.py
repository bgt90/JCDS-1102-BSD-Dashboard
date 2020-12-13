from flask import Flask, render_template

app= Flask(__name__)

# @app.route('/') #home
# def home():
#     return('Hello, BSD!')

@app.route('/', methods=['GET','POST'])
def home():
    return render_template("home.html") 

# @app.route('/about', methods=['GET','POST'])
# def about():
#     return 'Selamat Belajar Data Science'

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/dataset', methods=['GET','POST'])
def dataset():
    return render_template('dataset.html')

if __name__ == '__main__':
    app.run(debug=True)

