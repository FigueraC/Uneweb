function toggleUpdateForm(id) {
    var updateForm = document.getElementById('update-form-' + id);
    updateForm.style.display = 'block';
    cargarDatosTabla(); 
}

function cargarDatos() {
    fetch('/obtener-datos/')
        .then(response => response.json())
        .then(datos => {
            console.log(datos);
        })
        .catch(error => {
            console.error('Error al obtener los datos:', error);
        });
}
