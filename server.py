#Importar la app
from flask_app import app

#Importar controladores (pueden ser más de uno)
from flask_app.controllers import users_controller, appointments_controller

#Ejecución de app
if __name__ == "__main__":
    app.run(debug=True)