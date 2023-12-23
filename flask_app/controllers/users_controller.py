from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from datetime import datetime

#Importamos todos los modelos
from flask_app.models.users import User
from flask_app.models.appointments import Appointment

#Importación de BCrypt -> Encriptar la contraseña
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    #Validación de la información
    if not User.validate_user(request.form):
        return redirect('/')    
    
    #Encriptación de la contraseña
    pass_encrypt = bcrypt.generate_password_hash(request.form['password'])
    form = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pass_encrypt
    }

    id = User.save(form) #Recibo a cambio el ID del nuevo usuario
    session['user_id'] = id #Guardamos en sesión el identificador del usuario
    return redirect('/success')
    
#Ruta success solo de bienvenida
@app.route('/success')
def success():
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')

    form = {"id": session['user_id']}
    user = User.get_by_id(form)
    return render_template('success.html', user=user)

@app.route('/appointments')
def appointments():
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    form = {"id": session['user_id']}
    user = User.get_by_id(form)

    appointments = Appointment.get_all()

    return render_template('appointments.html', user=user, appointments=appointments, now=datetime.now)

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash('E-mail no registrado', 'login')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password incorrecto', 'login')
        return redirect('/')
    
    session['user_id'] = user.id
    return redirect('/success')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')