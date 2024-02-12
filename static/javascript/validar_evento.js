function validarEvento() {
    let nombreEvento = document.getElementById("nombreEvento").Value;
    let descripcionEvento = document.getElementById("descripcionEvento").value;
    let lugar = document.getElementById("lugar").value;
    let fecha = document.getElementById("fecha").value;
    let imagenes = document.getElementById("imagenes").files;

    if (nombreEvento === "" || descripcionEvento === "" || lugar === "" || fecha === "" || imagenes.length === 0) {
        alert("Por favor, complete todos los campos obligatorios.");
        return false;
    }

    let formData = new FormData();
    formData.append("nombreEvento", nombreEvento);
    formData.append("descripcionEvento", descripcionEvento);
    formData.append("lugar", lugar);
    formData.append("fecha", fecha);
    for (let i = 0; i < imagenes.length; i++) {
        formData.append("imagenes", imagenes[i]);
    }

    fetch('/crear_evento', {
        method: 'POST',
        body: formData
    })

    .then(response => {
        if (!response.ok) {
            throw new Error('Error al crear el evento.');
        }
        return response.json();
    })
}