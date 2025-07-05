from . import db
from datetime import datetime

class Landing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    theme = db.Column(db.String(50), nullable=False)
    fields = db.Column(db.JSON, nullable=False)  # Título, descripción, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    landing_id = db.Column(db.Integer, db.ForeignKey('landing.id'), nullable=False)
    action = db.Column(db.String(20))  # 'visit' o 'form_submit'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
