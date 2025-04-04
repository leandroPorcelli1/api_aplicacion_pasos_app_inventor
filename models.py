from database import db
from datetime import date, time

class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    pasos = db.Column(db.Integer, nullable=False)
    tiempo = db.Column(db.Integer, nullable=False)
    velocidad = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "fecha": self.fecha.isoformat(),
            "pasos": self.pasos,
            "tiempo": self.tiempo,
            "velocidad": self.velocidad
        }
