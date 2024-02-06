from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(100))
    title = db.Column(db.String(100))
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Quote(title='{self.title}', description='{self.description}')>"
