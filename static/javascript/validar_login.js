function validarLogin() {
    let idAdmin = document.getElementById("ID_admin").value;
    let password = document.getElementById("password").value;

    if (idAdmin === "" || password === ""){
        alert("Por favor, complete todos los campos.")
        return;
    }

    let formData = {
        ID_admin: idAdmin,
        password: password
    }

    enviarFormulario(formData);
}

function enviarFormulario(formData) {

    let baseUrl = document.querySelector("meta[name='base-url']").getAttribute("content");

    fetch(baseUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Error al iniciar sesión.");
        }
        return response.json();
    })
    .then(data => {
        // Manejar la respuesta del servidor si es necesario
        console.log(data);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}