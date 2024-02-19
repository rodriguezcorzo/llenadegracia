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

    fetch('/inicio_de_sesion', {
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
        if (!data.ok) {
         alert(data.error);
         return;
      }
      window.location.href = data.redirect_url
      })
    .catch(error => {
        console.error("Error:", error);
    });
}