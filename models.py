from extensions import db, login_manager

from flask_login import UserMixin

from werkzeug.security import check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Product(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(40), unique = True)
    price = db.Column(db.Integer(), nullable = False)
    new_price = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.Text(), nullable = False)
    image_url = db.Column(db.String(250), nullable = False)
    color_id = db.Column(db.Integer(), db.ForeignKey('color.id'), nullable = False)
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'))
    size_id = db.Column(db.Integer(), db.ForeignKey('size.id'))
    price_id = db.Column(db.Integer(), db.ForeignKey('price.id'))
    detail_category_id = db.Column(db.Integer(), db.ForeignKey('detailed.id'))
    all_product_id= db.Column(db.Integer(), db.ForeignKey('all.id'))
    comment = db.relationship('Review', backref='comment')


    def __repr__(self) :
        return self.name
    
    def __init__(self, name, price, new_price, description, image_url, size_id, color_id, category_id, detail_category_id, all_product_id):
        self.name = name
        self.price = price
        self.new_price = new_price
        self.description = description
        self.image_url = image_url
        self.size_id = size_id
        self.color = color_id
        self.category_id = category_id
        self.detail_category_id = detail_category_id
        self.all_product_id = all_product_id

    def save(self):
        db.session.add(self)
        db.session.commit()

class Color(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    color_name = db.Column(db.String(40), unique = True, nullable = False)
    in_stock = db.Column(db.Integer(), nullable = False)
    product_color = db.relationship('Product', backref='product_color')

    def __repr__(self) :
        return self.color_name
    
    def __init__(self, color_name, in_stock):
        self.in_stock = in_stock
        self.color_name = color_name

    def save(self):
        db.session.add(self)
        db.session.commit()


class All(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(40), unique = True, nullable = False)
    in_stock = db.Column(db.Integer(), nullable = False)
    all_product_name = db.relationship('Product', backref='all_product_name')

    def __repr__(self) :
        return self.name
    
    def __init__(self, color_name, in_stock):
        self.in_stock = in_stock
        self.color_name = color_name

    def save(self):
        db.session.add(self)
        db.session.commit()

class Category(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(40), unique = True, nullable = False)
    category= db.relationship('Product', backref='category')

    def __repr__(self) :
        return self.name
    
    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

class Detailed(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(40), unique = True, nullable = False)
    detailed_category = db.relationship('Product', backref='detailed_category')

    def __repr__(self) :
        return self.name
    
    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()


class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    subject = db.Column(db.String(20), nullable = False)
    message = db.Column(db.String(255), nullable = False)

    def __repr__(self) :
        return self.name
    
    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def save(self):
        db.session.add(self)
        db.session.commit()


class Newsletter(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False)

    def __repr__(self) :
        return self.name
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        db.session.add(self)
        db.session.commit()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    full_name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    user_fav = db.relationship('Favorites', backref='user_fav')

    def __repr__(self) :
        return self.full_name
    
    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Favorites(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    image =  db.Column(db.String(40), nullable = False)
    product_name = db.Column(db.String(40), unique = True, nullable = False)
    price = db.Column(db.Integer(), nullable = False)
    name = db.Column(db.String(20), nullable = False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    

    def __repr__(self) :
        return self.product_name
    
    def __init__(self, product_name, price, image):
        self.product_name = product_name
        self.price = price
        self.image = image


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
class Size(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    size_name = db.Column(db.String(40), unique = True, nullable = False)
    in_stock = db.Column(db.Integer())
    product_size = db.relationship('Product', backref='product_size')

    def __repr__(self) :
        return self.size_name
    
    def __init__(self, size_name, in_stock):
        self.in_stock = in_stock
        self.size_name = size_name

    def save(self):
        db.session.add(self)
        db.session.commit()


class Price(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    price_name = db.Column(db.String(40), unique = True, nullable = False)
    in_stock = db.Column(db.Integer(), nullable = False)
    product_price = db.relationship('Product', backref='product_price')

    def __repr__(self) :
        return self.price_name
    
    def __init__(self, price_name, in_stock):
        self.price_name = price_name
        self.in_stock = in_stock

    def save(self):
        db.session.add(self)
        db.session.commit()

class Review(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Reviews = db.Column(db.Text(), nullable = False)
    date = db.Column(db.String(20), nullable = False)
    full_name = db.Column(db.String(20), nullable = False)
    product_id = db.Column(db.Integer(), db.ForeignKey('product.id'))

    def __repr__(self) :
        return self.Reviews
    
    def __init__(self, Reviews, date):
        self.Reviews = Reviews
        self.date = date

    def save(self):
        db.session.add(self)
        db.session.commit()
