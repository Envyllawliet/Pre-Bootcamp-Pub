function loading() {
    Swal.fire({
        title: 'Loading weather report...',
        timer: 2000,
        showConfirmButton: true
    });
}

function cookies() {
    var message = document.querySelector("#message");

    message.remove();
}

function temp() {
    var select = document.querySelector("#grades");
    var option = select.value;
    
    var hot = document.querySelectorAll(".hot");
    var cold = document.querySelectorAll(".cold");
    
    hot.forEach(function(element) {
        var temperature = parseFloat(element.textContent);
        if (option == "°F") {
            var fahrenheit = Math.round((temperature * 9/5) + 32);
            element.textContent = fahrenheit + "°";
        } else {
            var celsius = Math.round((temperature - 32) * 5/9);
            element.textContent = celsius + "°";
        }
    });
    
    cold.forEach(function(element) {
        var temperature = parseFloat(element.textContent);
        if (option == "°F") {
            var fahrenheit = Math.round((temperature * 9/5) + 32);
            element.textContent = fahrenheit + "°";
        } else {
            var celsius = Math.round((temperature - 32) * 5/9);
            element.textContent = celsius + "°";
        }
    });
}


