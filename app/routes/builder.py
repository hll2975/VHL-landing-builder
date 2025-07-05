from flask import Blueprint, render_template

bp = Blueprint('builder', __name__)

@bp.route('/')
def home():
    return render_template('base.html')
