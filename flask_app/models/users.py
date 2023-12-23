#Importar la conexión con la BD
from flask_app.config.mysqlconnection import connectToMySQL
#Importación de Expresiones Regulares
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email
#Importación de flash para desplegar mensajes
from flask import flash 

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('esquema_citas').query_db(query, form)
        return result 
    
    #Validación de información
    @staticmethod
    def validate_user(form):
        is_valid = True
        #Validamos que nombre y apellido tengan al menos 2 caracteres
        if len(form['first_name']) < 2:
            flash('Nombre debe tener al menos 2 caracteres', 'register')
            is_valid = False
        
        if len(form['last_name']) < 2:
            flash('Apellido debe tener al menos 2 caracteres', 'register')
            is_valid = False
        
        #Validamos que el password tenga al menos 6 caracteres
        if len(form['password']) < 6:
            flash('Contraseña debe tener al menos 6 caracteres', 'register')
            is_valid = False
        
        #Validamos que el correo no este registrado previamente
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('esquema_citas').query_db(query, form)
        if len(results) >=1:
            flash('E-mail registrado previamente', 'register')
            is_valid = False
        
        #Verificamos que las contraseñas coincidan
        if form['password'] != form['confirm']:
            flash('Contraseñas no coinciden', 'register')
            is_valid = False
        
        #Verificamos que el email tenga el formato correcto -> Expresiones Regulares
        if not EMAIL_REGEX.match(form['email']):
            flash('E-mail inválido', 'register')
            is_valid = False
        
        return is_valid
    
    @classmethod
    def get_by_email(cls, form):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('esquema_citas').query_db(query, form)
        if len(result) < 1:
            return False
        else:
            user = cls(result[0])
            return user

    @classmethod
    def get_by_id(cls, form):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_citas').query_db(query, form)
        user = cls(result[0])
        return user