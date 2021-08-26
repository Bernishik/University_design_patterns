from flask import Flask, render_template, redirect
from WebClient import WebClient
from config import Config
from forms import SendForm
from models import db, Post

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SendForm()
    if form.validate_on_submit():
        name = form.name.data
        last_name = form.lastname.data
        age = form.age.data
        txt = form.txt.data
        web_client = WebClient()
        web_client.create_attachment()
        web_client.upload(name, last_name, age, txt)
        return redirect('/send')
    return render_template("index.html", form=form)


@app.route("/send")
def send():
    return render_template("send.html", )


if __name__ == '__main__':
    app.run()
