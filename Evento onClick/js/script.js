function loginLogout(elemento_this) {
    if (elemento_this.innerText === "Login") {
        elemento_this.innerText = "Logout";
    } else {
        elemento_this.innerText = "Login";
    }
}

function addDef(elemento_this) {
    elemento_this.remove();
}

var likes1 = 13;
function meGusta1() {
    likes1++;
    var elemento_numero = document.querySelector("#likedef1");
    elemento_numero.innerText = likes1;
    Swal.fire({
        title: 'Ninja was liked',
        timer: 500,
        showConfirmButton: false
    });
}

var likes2 = 37;
function meGusta2() {
    likes2++;
    var elemento_numero = document.querySelector ("#likedef2");
    elemento_numero.innerText = likes2;
    Swal.fire({
        title: 'Ninja was liked',
        timer: 500,
        showConfirmButton: false
    });
}