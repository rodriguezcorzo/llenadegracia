function validarYEnviar() {
    // Obtener los datos del formulario
    let nombre = document.getElementById("nombre").value;
    let cedula = document.getElementById("cedula").value;
    let correo = document.getElementById("correo").value;
    let celular = document.getElementById("celular").value;
    let profesion = document.getElementById("profesion").value;

    // Validar los datos según tus criterios (puedes agregar más validaciones)
    if (nombre === "" || cedula === "" || correo === "" || celular === "") {
        alert("Por favor, complete todos los campos obligatorios.");
        return;
    }

    // Crear un objeto JSON con los datos del formulario
    let formData = {
        nombre: nombre,
        cedula: cedula,
        correo: correo,
        celular: celular,
        profesion: profesion
    };

    // Convertir el objeto a una cadena JSON
    let jsonData = JSON.stringify(formData);

    // Enviar la cadena JSON al backend (puedes usar AJAX o Fetch para esto)
    // Aquí solo se mostrará en la consola para demostración
    alert(jsonData);
}