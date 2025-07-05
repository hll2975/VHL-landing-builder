from flask import Blueprint, request
from app.models import Metric, Landing
from app import db
from datetime import datetime

bp = Blueprint('metrics', __name__)

@bp.route('/metrics/visit/<slug>', methods=['POST'])
def register_visit(slug):
    landing = Landing.query.filter_by(slug=slug).first()
    if landing:
        m = Metric(landing_id=landing.id, action='visit')
        db.session.add(m)
        db.session.commit()
        return {'status': 'ok'}, 200
    return {'error': 'Landing not found'}, 404

@bp.route('/metrics/form/<slug>', methods=['POST'])
def register_form_submit(slug):
    landing = Landing.query.filter_by(slug=slug).first()
    if landing:
        m = Metric(landing_id=landing.id, action='form_submit')
        db.session.add(m)
        db.session.commit()
        return {'status': 'ok'}, 200
    return {'error': 'Landing not found'}, 404
