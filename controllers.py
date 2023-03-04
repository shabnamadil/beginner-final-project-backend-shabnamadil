from flask import render_template, request, redirect, url_for

from app import app
from models import Product, Color, Category, Contact, Newsletter, User, Favorites, Size, Price, Detailed, Review, All
from forms import ContactForm, NewsLetterForm, RegisterForm, LoginForm, FavoriteForm, RemoveForm, SearchForm, ReviewForm
from werkzeug.security import generate_password_hash
from datetime import datetime

from flask_login import login_user, login_required, logout_user, current_user

@app.context_processor
def layout():
    all = All.query.all()
    product = Product.query.all()
    try:
        favorites = Favorites.query.filter_by(name=current_user.full_name).count()
    except:
        favorites = Favorites.query.all()

    category = Category.query.all()
    detailed = Detailed.query.all()
    color = Color.query.all()
    size = Size.query.all()
    price = Price.query.all()
    news = NewsLetterForm()
    search = SearchForm()
    return dict(news = news, favoritess = favorites, category = category, detailed = detailed,  search = search, product = product, color = color, size = size, price = price, all = all)


@app.route('/', methods = ['GET', 'POST'])
def shop():
    product = Product.query.all()
    count = len(product)
    if request.method == 'POST':
        search = SearchForm(request.form)
        news = NewsLetterForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product = Product.query.filter(Product.name.contains(k)).all()
            count = len(product)
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
            return redirect (url_for('shop'))
    return render_template ('shop.html', product = product, count = count)


@app.route('/filter/color/<string:name>', methods = ['GET', 'POST'])
def filter_color(name):
    product1= Color.query.filter_by(color_name = name).first().product_color
    count = len(product1)
    if request.method == 'POST':
        search = SearchForm(request.form)
        news = NewsLetterForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product1 = Product.query.filter(Product.name.contains(k)).all()
            count = len(product1)
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
            return redirect (url_for('shop'))
    return render_template ('shop.html',  product = product1, count = count)


@app.route('/filter/all/<string:name>', methods = ['GET', 'POST'])
def filter_all(name):
    product1= All.query.filter_by(name = name).first().all_product_name
    count = len(product1)
    if request.method == 'POST':
        search = SearchForm(request.form)
        news = NewsLetterForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product1 = Product.query.filter(Product.name.contains(k)).all()
            count = len(product1)
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
            return redirect (url_for('shop'))
    return render_template ('shop.html',  product = product1, count = count)


@app.route('/filter/size/<string:name>', methods = ['GET', 'POST'])
def filter_size(name):
    product2= Size.query.filter_by(size_name = name).first().product_size
    count = len(product2)
    if request.method == 'POST':
        search = SearchForm(request.form)
        news = NewsLetterForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product2 = Product.query.filter(Product.name.contains(k)).all()
            count = len(product2)
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
            return redirect (url_for('shop'))
    return render_template ('shop.html', product = product2, count = count)


@app.route('/filter/price/<string:name>', methods = ['GET', 'POST'])
def filter_price(name):
    product3= Price.query.filter_by(price_name = name).first().product_price
    count = len(product3)
    print(product3)
    if request.method == 'POST':
        search = SearchForm(request.form)
        news = NewsLetterForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product3 = Product.query.filter(Product.name.contains(k)).all()
            count = len(product3)
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
            return redirect (url_for('shop'))
    return render_template ('shop.html', product = product3, count = count)


@app.route('/filter/category/<int:id>', methods = ['GET', 'POST'])
def filter_category(id):
    product4 = Category.query.filter_by(id = id).first().category
    count = len(product4)
    if request.method == 'POST':
        search = SearchForm(request.form)
        news = NewsLetterForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product4 = Product.query.filter(Product.name.contains(k)).all()
            count = len(product4)
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
            return redirect (url_for('shop'))
    return render_template ('shop.html', product = product4, count = count)


@app.route('/filter/category/detail/<int:id>', methods = ['GET', 'POST'])
def filter_category_detail(id):
    product5 = Detailed.query.filter_by(id = id).first().detailed_category
    count = len(product5)
    if request.method == 'POST':
        search = SearchForm(request.form)
        news = NewsLetterForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product5 = Product.query.filter(Product.name.contains(k)).all()
            count = len(product5)
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
            return redirect (url_for('shop'))
    return render_template ('shop.html', product = product5, count = count)


@app.route('/detail/<int:id>', methods = ['GET', 'POST'])
def detail(id):
    detail = Product.query.filter_by(id=id).first()
    favorite = FavoriteForm()
    comment = ReviewForm()
    commentmain = Review.query.all()
    if request.method == 'POST':
        comment = ReviewForm(request.form)
        favorite = FavoriteForm(request.form)
        search = SearchForm(request.form)
        news = NewsLetterForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product8 = Product.query.filter(Product.name.contains(k)).all()
            count = len(product8)
            return render_template('shop.html', product = product8, count = count)
        if favorite.validate_on_submit():
            try:
                    favorite2 = Favorites(
                        product_name = detail.name, 
                        price = detail.new_price, 
                        image = detail.image_url 
                        
                    )
                    favorite2.user_id = current_user.id
                    favorite2.name = current_user.full_name
                    favorite2.save()
                
            except:
                pass
                return redirect(url_for('favorite'))
        if comment.validate_on_submit():
            review2= Review(
                Reviews = comment.review.data, 
                date = datetime.today().strftime('%d %b %Y' ),
                

            )
            review2.product_id = id
            review2.full_name = current_user.full_name
            review2.save()
            return redirect (url_for('detail', id=id))
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
            return redirect (url_for('detail', id=id)) 
     
    return render_template ('detail.html', detail = detail,  favorite = favorite, comment = comment, commentmain = commentmain)


@app.route('/contact', methods = ['GET', 'POST'])
def connection():
    contact = ContactForm()
    if request.method == 'POST':
        search = SearchForm(request.form)
        news = NewsLetterForm(request.form)
        contact = ContactForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product9 = Product.query.filter(Product.name.contains(k)).all()
            count = len(product9)
            return render_template('shop.html', product = product9, count = count)
        if contact.validate_on_submit():
            contact2 = Contact(
                name = contact.name.data,
                email = contact.email.data,
                subject = contact.subject.data,
                message = contact.message.data
            )
            contact2.save()
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
        return redirect (url_for('connection')) 
    return render_template ('contact.html', contact = contact)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    register = RegisterForm()
    count = 2
    if request.method == 'POST':
        search = SearchForm(request.form)
        register = RegisterForm(request.form)
        news = NewsLetterForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product9 = Product.query.filter(Product.name.contains(k)).all()
            count = len(product9)
            return render_template('shop.html', product = product9, count = count)
        if register.validate_on_submit():
            user = User(
                full_name = register.full_name.data,
                email = register.email.data, 
                password = generate_password_hash(register.password.data)
            )
            user.save()
            return redirect(url_for('login'))
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
            return redirect (url_for('register')) 
    return render_template ('register.html', register = register, count = count)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    login = LoginForm()
    count = 2
    if request.method == 'POST':
        search = SearchForm(request.form)
        login = LoginForm(request.form)
        news = NewsLetterForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product9 = Product.query.filter(Product.name.contains(k)).all()
            count = len(product9)
            return render_template('shop.html', product = product9, count = count)
        if login.validate_on_submit():
            print('valid')
            logged_user = User.query.filter_by(email = login.email.data).first()
            if logged_user and logged_user.check_password(login.password.data):
                  login_user(logged_user)
                  print('logged')
                  return redirect (url_for('shop'))
            else:
                print('no logged')
                return redirect (url_for('login')) 
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
            return redirect (url_for('login'))     
    return render_template ('login.html', login = login, count = count)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/favorite', methods = ['GET', 'POST'])
@login_required
def favorite():
    count = 2
    if request.method == 'POST':
        search = SearchForm(request.form)
        news = NewsLetterForm(request.form)
        if search.validate_on_submit():
            k = search.searchword.data
            product9 = Product.query.filter(Product.name.contains(k)).all()
            count = len(product9)
            return render_template('shop.html', product = product9, count = count)
        if news.validate_on_submit():
            newsletter = Newsletter(
                name = news.name.data,
                email = news.email.data
            )
            newsletter.save()
        return redirect (url_for('favorite')) 
    favorites = Favorites.query.filter_by(name = current_user.full_name, user_id = current_user.id)

    return render_template ('favorites.html', favorites = favorites, count = count)


@app.route('/favorite/<int:id>')
def favorite_remove(id):
        
        fav = Favorites.query.filter_by(id = id).first()
        
        fav.delete()                
        return redirect(url_for('favorite'))