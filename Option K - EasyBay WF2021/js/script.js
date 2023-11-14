function cookies() {
    var message = document.querySelector("#message");

    message.remove();
}

function cartStatus() {
    alert("Your Cart is empty!");
}

function hoverIn(elemento_imagen){
    elemento_imagen.src = "images/succulents-2.jpg";
}

function hoverOut(elemento_imagen) {
    elemento_imagen.src = "images/succulents-1.jpg";
}