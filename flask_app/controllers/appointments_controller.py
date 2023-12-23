from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

from flask_app.models.users import User
from flask_app.models.appointments import Appointment

@app.route('/appointment/add')
def new_appointment():
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')

    return render_template('add.html')

@app.route('/appointment/create', methods=['POST'])
def create_appointment():
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')

    if not  Appointment.validate_appointment(request.form):
        return redirect('/appointment/add')

    Appointment.save(request.form)
    return redirect('/appointments')

@app.route('/appointment/edit/<int:id>')
def edit_appointment(id):
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')

    diccionario = {"id": id}
    appointment = Appointment.get_by_id(diccionario)
    #Evitar que se editen otras tareas via url
    if appointment.status != 'Pendiente':
        flash('No puedes editar esta tarea', 'appointment_edit_error')
        return redirect('/appointments')

    return render_template('edit.html', appointment=appointment)

@app.route('/appointment/update', methods=['POST'])
def update_appointment():
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    if not  Appointment.validate_appointment(request.form):
        return redirect('/appointment/edit/'+request.form['id'])
    Appointment.update(request.form)
    return redirect('/appointments')

@app.route('/appointment/delete/<int:id>')
def delete_appointment(id):
    if 'user_id' not in session:
        flash('Favor de iniciar sesión', 'not_in_session')
        return redirect('/')
    form = {"id": id}
    Appointment.delete(form)
    return redirect('/appointments')