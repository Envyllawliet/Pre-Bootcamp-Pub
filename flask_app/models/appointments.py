from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

class Appointment:

    def __init__(self, data):
        self.id = data['id']
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        #JOIN
        self.first_name = data['first_name']
        self.last_name = data['last_name']

    @staticmethod
    def validate_appointment(form):
        is_valid = True

        if form['task'] == '':
            flash('El campo tarea no puede estar vacio', 'appointments')
            is_valid = False
        #Cinturon negro 2
        if form['date'] == '':
            flash('Ingresa una fecha', 'appointments')
            is_valid = False
        else:
            fecha_cita = datetime.strptime(form['date'], '%Y-%m-%d')
            hoy = datetime.now()
            if hoy > fecha_cita:
                flash('No puede ser una fecha pasada', 'appointments')
                is_valid = False
        return is_valid

    @classmethod
    def save(cls, form):
        query = "INSERT INTO appointments (task, date, status, user_id) VALUES (%(task)s, %(date)s, %(status)s, %(user_id)s)"
        result = connectToMySQL('esquema_citas').query_db(query, form)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT appointments.*, users.first_name, users.last_name FROM appointments JOIN users ON user_id = users.id"
        results = connectToMySQL('esquema_citas').query_db(query)
        appointments = []
        for appointment in results:
            appointments.append(cls(appointment))
        return appointments

    @classmethod
    def get_by_id(cls, form):
        query = "SELECT appointments.*, users.first_name, users.last_name FROM appointments JOIN users ON user_id = users.id WHERE appointments.id = %(id)s"
        result = connectToMySQL('esquema_citas').query_db(query, form)
        appointment = cls(result[0])
        return appointment

    @classmethod
    def update(cls, form):
        query = "UPDATE appointments SET task=%(task)s, date=%(date)s, status=%(status)s WHERE id=%(id)s"
        result = connectToMySQL('esquema_citas').query_db(query, form)
        return result

    @classmethod
    def delete(cls, form):
        query = "DELETE FROM appointments WHERE id = %(id)s"
        result = connectToMySQL('esquema_citas').query_db(query, form)
        return result