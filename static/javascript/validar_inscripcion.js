function validarYEnviar() {
    // Obtener los datos del formulario
    let nombre = document.getElementById("nombre").value;
    let cedula = document.getElementById("cedula").value;
    let correo = document.getElementById("correo").value;
    let celular = document.getElementById("celular").value;
    let profesion = document.getElementById("profesion").value;

    // Validar los datos
    if (nombre === "" || cedula === "" || correo === "" || celular === "") {
        alert("Por favor, complete todos los campos obligatorios.");
        return;
    }

    // Crea un objeto JSON con los datos del formulario
    let formData = {
        nombre: nombre,
        cedula: cedula,
        correo: correo,
        celular: celular,
        profesion: profesion
    };

    // Convertir el objeto a una cadena JSON
    let jsonData = JSON.stringify(formData);

    console.log(jsonData);
}