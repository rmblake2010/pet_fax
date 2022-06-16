from flask import Blueprint, render_template 
import json

#acessing json object
pets = json.load(open('pets.json'))


bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets) 

#Having to subtract one to get desired pet id, not sure why
@bp.route('/<int:pet_id>')
def pet_id(pet_id):
    # return f'{pets[pet_id]} ---- req pet id: {pet_id}'
    return render_template('pets/show.html', pet=pets[pet_id-1])
    
