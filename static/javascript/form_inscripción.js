// Obtén todos los elementos con la clase "secundario-btn"
let buttons = document.getElementsByClassName("secundario-btn");

// Itera sobre la lista de botones y agrega el evento de clic a cada uno
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function() {
        window.location.href = "../../templates/form_inscripcion.html";
    });
}