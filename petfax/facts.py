from flask import Blueprint, render_template

bp = Blueprint('facts', __name__, url_prefix='/facts')

@bp.route('/')
def index():
    return 'facts index page!'

@bp.route('/new')
def new_fact():
    return render_template('new_fact.html')