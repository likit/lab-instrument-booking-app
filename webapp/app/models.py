import copy
from werkzeug.security import generate_password_hash, check_password_hash
from . import mongo
from . import login_manager

class User():
    def __init__(self, email):
        self.email = email

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email

    def __repr__(self):
        return '<User email: %r>' % self.email


@login_manager.user_loader
def load_user(email):
    user = mongo.db.users.find_one({'email': email})

    # if no users found, try searching in admin db
    if user is None:
        return None
        # admin = mongo.db.admins.find_one({'email': email})
        # if not admin:
        #     return None
        # else:
        #     return Customer(admin['email'])
    else:
        return User(user['email'])
