from app import app, db

from datetime import datetime


class CentOps(db.Model):
    __tablename__ = 'centops'

    id = db.Column(db.Integer, primary_key=True)
    ustanova = db.Column(db.String, nullable=False)
    intervencija = db.Column(db.String, nullable=False)
    cekanje = db.Column(db.Integer, nullable=False)
    broj = db.Column(db.Integer, nullable=False)
    datum  = db.Column(db.DateTime, nullable=False)
    datum_scr = db.Column(db.DateTime, nullable=False)
    rok = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.id)
