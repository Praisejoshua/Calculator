from package import db

class Database(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    expression = db.Column(db.String(100), nullable = False)
    result = db.Column(db.String(100), nullable = False)

