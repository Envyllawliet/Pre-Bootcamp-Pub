console.log("Página cargada");

function cerrar_sesion() {
    alert("Cerrando Sesión");
    console.log("Se cerró la sesión del usuario");
}

//this -> es elemento que llama a mi función con el que interactuamos
function cambiar_texto(elemento_this) {
    elemento_this.innerText = "Otro texto";
}

function mouse_dentro(elemento_imagen) {
    elemento_imagen.src = "assets/images/todd-s.jpg";
}

function mouse_fuera(elemento_imagen) {
    elemento_imagen.src = "assets/images/jane-m.jpg"
}

function eliminar(elemento) {
    elemento.remove();
}

var clicks_profile = 0;
function hicimos_click(elemento) {
    clicks_profile++;
    alert(`Hemos hecho clics: `+clicks_profile);
    elemento.style.color = "purple";
}

//background-color -> backgroundColor