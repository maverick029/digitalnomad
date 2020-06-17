from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = "maverick029"

@app.route("/")
def root():
    return render_template('HomePage.html')

@app.route("/home")
def home():
    return render_template('HomePage.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/science")
def science():
    return render_template('science.html')

@app.route("/gaming")
def gaming():
    return render_template('gaming.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
