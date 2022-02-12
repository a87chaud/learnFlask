from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLAlchemy_DATABASE_URI'] = os.environ.get("DATABASE_URL")
@app.route("/")

def index():
    return render_template("index.html")

    
if __name__ == "main":
    app.run(debug=True)