from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    content = db.Column(db.String(255))

    def __init__(self, title, content):
        self.title = title
        self.content = content
