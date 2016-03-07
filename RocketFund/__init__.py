from flask import Flask, render_template
from flask.ext.sqlalchemy import sqlalchemy 
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.route("/")
def hello():
    return render_template("index.html")