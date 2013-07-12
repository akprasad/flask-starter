from flask import Blueprint, render_template

bp = Blueprint('{0}', __name__)

@bp.route('/')
def index():
    return render_template('{0}/index.html')
