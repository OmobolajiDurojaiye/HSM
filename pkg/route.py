from flask import Flask, render_template, url_for, redirect, request, session, flash, jsonify
from pkg import app
from pkg.models import db, CustomerContactMessage

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



@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        new_message = CustomerContactMessage(name=name, email=email, messagebody=message)

        try:
            db.session.add(new_message)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Message sent successfully'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Error occurred while sending the message. Please try again later.'})
    else:
        return render_template('index.html')   
    
@app.route('/login/', methods=['POST', 'GET'])
def login():
    return render_template('user/login.html')