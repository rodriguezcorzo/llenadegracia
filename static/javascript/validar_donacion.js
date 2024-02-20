function validarDonacion() {
    let nombre = document.getElementById("nombre").value;
    let apellido = document.getElementById("apellido").value;
    let cedula = document.getElementById("cedula").value;
    let correo = document.getElementById("correo").value;
    let celular = document.getElementById("celular").value;
    let direccion = document.getElementById("direccion").value;
    let descripcionDonacion = document.getElementById("descripcionDonacion").value;

    if (nombre === "" ||apellido === "" || cedula === "" || correo === "" || celular === "" || direccion === "" || descripcionDonacion === "") {
        alert("Por favor, complete todos los campos.");
        return;
    }

    let formData = {
        nombre: nombre,
        apellido: apellido,
        cedula: cedula,
        correo: correo,
        celular: celular,
        direccion: direccion,
        descripcionDonacion: descripcionDonacion
    };

    enviarDonacion(formData);
}

function enviarDonacion(formData) {
    fetch('/formulario_donacion', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Error al enviar la donación.");
        }
        return response.json();
    })
    .then(data => {
        if (!data.ok) {
            alert(data.error);
            return;
        }
        window.location.href = data.redirect_url;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}