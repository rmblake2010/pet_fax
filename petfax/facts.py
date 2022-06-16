
from flask import Blueprint, redirect, render_template, request

bp = Blueprint('facts', __name__, url_prefix='/facts')

@bp.route('/', methods=['GET', 'POST'])
def index():
    #return print(request.form)
    if request.method == 'POST':
        print('imhere')
        return render_template('facts_index.html', data=request.form)
    else:
        return render_template('facts/facts_index.html')

@bp.route('/new')
def new_fact():
    return render_template('facts/new_fact.html')