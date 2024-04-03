from flask import Flask, render_template, url_for, redirect, request, session, flash, jsonify
from pkg import app
from pkg.models import db, CustomerContactMessage, User
from werkzeug.security import generate_password_hash, check_password_hash

# 404 errorhandler
@app.errorhandler(404)
def not_found_error(error):
    return render_template('page404.html')


# Image provider
@app.route('/image')
def get_image():
    image_url = url_for('static', filename='images/welcome-image (2).png')
    image_url2 = url_for('static', filename='images/welcome-image (1).png')
    image_url3 = url_for('static', filename='images/welcome-image (4).png')
    return jsonify(image=image_url, image2=image_url2, image3=image_url3)



@app.route('/index')
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    

@app.route('/about/')
def about():
    return render_template('user/about.html')

@app.route('/contact/')
def contact():
    return render_template('user/contact.html')

# @app.route('/customer/signup/', methods=['GET', 'POST'])
# def customer_signup():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('password')
        
#         if not (username and email and password):
#             flash('Please fill out all the fields.')
#             return redirect(url_for('customer_signup')) 

#         existing_participant = User.query.filter_by(email=email).first()
#         if existing_participant:
#             flash('Email already exists. Please choose a different email.')
#             return redirect(url_for('customer_signup')) 
        
#         hashed_password = generate_password_hash(password)
        
#         new_user = User(username=username, email=email, password=hashed_password, role='customer')
        
#         db.session.add(new_user)
#         db.session.commit()
        
#         flash('Account created successfully! Please log in.')
#         return redirect(url_for('customer_login'))
    
#     return render_template('user/customer_signup.html')

# @app.route('/service_provider/signup/', methods=['GET', 'POST'])
# def service_provider_signup():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('password')
        
#         if not (username and email and password):
#             flash('Please fill out all the fields.')
#             return redirect(url_for('service_provider_signup')) 

#         existing_participant = User.query.filter_by(email=email).first()
#         if existing_participant:
#             flash('Email already exists. Please choose a different email.')
#             return redirect(url_for('service_provider_signup')) 
        
#         hashed_password = generate_password_hash(password)
        
#         new_user = User(username=username, email=email, password=hashed_password, role='service provider')
        
#         db.session.add(new_user)
#         db.session.commit()
        
#         flash('Account created successfully! Please log in.')
#         return redirect(url_for('service_provider_login'))
    
#     return render_template('user/service_provider_signup.html')
    
# @app.route('/login/', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
        
#         user = User.query.filter_by(email=email).first()

#         if user:
#             saved_pwd = user.password
#             if check_password_hash(saved_pwd, password):
#                 session['user_id'] = user.id
                
#                 if user.role == 'service provider':
#                     return redirect(url_for('service_provider_dashboard'))
#                 elif user.role == 'customer':
#                     return redirect(url_for('customer_dashboard'))      
#             else:
#                 flash('Incorrect email or password. Please try again.')
#         else:
#             flash('Incorrect credentials. Please try again.')
#     return render_template('user/login.html')



@app.route('/customer/signup/', methods=['GET', 'POST'])
def customer_signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not (username and email and password):
            flash('Please fill out all the fields.')
            return redirect(url_for('customer_signup')) 

        existing_participant = User.query.filter_by(email=email).first()
        if existing_participant:
            flash('Email already exists. Please choose a different email.')
            return redirect(url_for('customer_signup')) 
        
        new_user = User(username=username, email=email, password=password, role='customer')
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please log in.')
        return redirect(url_for('customer_login'))
    
    return render_template('user/customer_signup.html')

@app.route('/service_provider/signup/', methods=['GET', 'POST'])
def service_provider_signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not (username and email and password):
            flash('Please fill out all the fields.')
            return redirect(url_for('service_provider_signup')) 

        existing_participant = User.query.filter_by(email=email).first()
        if existing_participant:
            flash('Email already exists. Please choose a different email.')
            return redirect(url_for('service_provider_signup')) 
        
        new_user = User(username=username, email=email, password=password, role='service provider')
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please log in.')
        return redirect(url_for('service_provider_login'))
    
    return render_template('user/service_provider_signup.html')

@app.route('/service_provider/login/', methods=['POST', 'GET'])
def service_provider_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email, role='service provider', password=password).first()

        if user:
            session['user_id'] = user.id
            flash('Login Successful!')
            return redirect(url_for('service_provider_dashboard'))
        else:
            flash('Incorrect email or password. Please try again.')
    return render_template('user/service_provider_login.html')

@app.route('/customer/login/', methods=['POST', 'GET'])
def customer_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email, role='customer', password=password).first()

        if user:
            session['user_id'] = user.id
            flash('Login Successful!')
            return redirect(url_for('customer_dashboard'))
        else:
            flash('Incorrect email or password. Please try again.')
    return render_template('user/customer_login.html')

# @app.route('/service_provider/login/', methods=['POST', 'GET'])
# def service_provider_login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
        
#         user = User.query.filter_by(email=email, role='service provider').first()

#         if user:
#             saved_pwd = user.password
#             if check_password_hash(saved_pwd, password):
#                 session['user_id'] = user.id
#                 flash('Login Successful!')
#                 return redirect(url_for('service_provider_dashboard'))
#             else:
#                 flash('Incorrect email or password. Please try again.')
#         else:
#             flash('No user found with this email.')
#     return render_template('user/service_provider_login.html')


# @app.route('/customer/login/', methods=['POST', 'GET'])
# def customer_login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
        
#         user = User.query.filter_by(email=email, role='customer').first()

#         if user:
#             saved_pwd = user.password
#             if check_password_hash(saved_pwd, password):
#                 session['user_id'] = user.id
#                 flash('Login Successful!')
#                 return redirect(url_for('customer_dashboard'))
#             else:
#                 flash('Incorrect email or password. Please try again.')
#         else:
#             flash('No user found with this email.')
#     return render_template('user/customer_login.html')


@app.route('/service_provider/dashboard/')
def service_provider_dashboard():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.filter_by(id=user_id).first()
        if user:
            return render_template('service_provider/landing_page.html', user=user)
        else:
            flash('User not found.')
            return redirect(url_for('service_provider_login'))
    else:
        flash('You need to login first.')
        return redirect(url_for('service_provider_login'))
    

@app.route('/service_provider/profile/')
def service_provider_profile():
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.query.filter_by(id=user_id).first()
        if user:
            return render_template('service_provider/profile.html', user=user)
        else:
            flash('User not found.')
            return redirect(url_for('service_provider_login'))
    else:
        flash('You need to login first.')
        return redirect(url_for('service_provider_login'))
    






@app.route('/customer/dashboard/')
def customer_dashboard():
    if 'user_id' in session:
        user_id = session['user_id']
        return render_template('customer/landing_page.html', user_id=user_id)
    else:
        flash('You need to login first.')
        return redirect(url_for('customer_login'))
    

@app.route('/customer/logout/')
def customer_logout():
    session.pop('user_id', None)
    flash('You have been logged out successfully.')
    return redirect(url_for('customer_login'))

@app.route('/service_provider/logout/')
def service_provider_logout():
    session.pop('user_id', None)
    flash('You have been logged out successfully.')
    return redirect(url_for('service_provider_login'))