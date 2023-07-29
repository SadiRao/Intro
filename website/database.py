from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), nullable=False)
    message = db.Column(db.String, nullable=False)
    def __repr__(self):
        self.fid = self.id[self.currentQ]
        return f"User(id={self.fid!r}, email={self.email!r}, message={self.message!r})"
    
