//Función para cambiar nombre según el texto que se ingrese

function editProfile() {
    var name = document.querySelector ("#name");
    var input = document.querySelector ("#newname");

    if(input.value == "") {
        name.innerText = "Jane Doe";
    } else {
        name.innerText = input.value;
    }
}

//Función para eliminar el elemento de la lista que contiene el boton reject

function reject(event) {
    var listItem = event.target.parentNode.parentNode; //selecciona el "abuelo"
    var crnumber = document.querySelector("#cr-number"); 
    var cr = parseInt(crnumber.innerText);    //obtiene el numero de request actual
    
    listItem.parentNode.removeChild(listItem); //remueve el item de la lista
    cr--;                                     //disminuye el numero de solicitudes
    crnumber.innerText = cr;
}

//Función para aumentar el numero de conexiones al aceptar una solicitud

function accept() {
    var listItem = event.target.parentNode.parentNode; //selecciona el "abuelo"
    var connumber = document.querySelector("#con-number");
    var conx = parseInt(connumber.innerText); //obtiene el numero de connections actual
    var crnumber = document.querySelector("#cr-number");
    var cr = parseInt(crnumber.innerText); //obtiene el numero de request actual

    listItem.parentNode.removeChild(listItem); //remueve el item de la lista
    cr--;                                     //disminuye el numero de solicitudes
    crnumber.innerText = cr;
    conx++;                                   //aumenta el numero de conexiones
    connumber.innerText = conx;
}