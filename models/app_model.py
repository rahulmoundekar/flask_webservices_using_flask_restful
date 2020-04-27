from db.db import db
from flask_restful_swagger import swagger


@swagger.model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            'name': self.name,
            'email': self.email,
            'contact': self.contact,
            'id': self.id,
        }
