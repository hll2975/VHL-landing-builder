from flask import Blueprint, render_template, abort
from app.models import Landing

bp = Blueprint('render', __name__)

@bp.route('/<slug>')
def view_landing(slug):
    landing = Landing.query.filter_by(slug=slug).first()
    if not landing:
        abort(404)
    
    return render_template(
        f"themes/{landing.theme}.html",
        title=landing.fields['title'],
        description=landing.fields['description']
    )
