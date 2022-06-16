from flask import Flask
from flask_migrate import Migrate

#app factory 
def create_app():
    app = Flask(__name__)

    #database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Jailbird2@localhost:5000/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'

    #Registering pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)
    # Registering facts blueprint
    from . import facts
    app.register_blueprint(facts.bp)
    
    return app 