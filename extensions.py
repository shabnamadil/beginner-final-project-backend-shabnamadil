from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


from app import app
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
admin = Admin(app)

from models import *
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Color, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Detailed, db.session))
admin.add_view(ModelView(Contact, db.session))
admin.add_view(ModelView(Newsletter, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Favorites, db.session))
admin.add_view(ModelView(Size, db.session))
admin.add_view(ModelView(Price, db.session))
admin.add_view(ModelView(Review, db.session))
admin.add_view(ModelView(All, db.session))
                             
