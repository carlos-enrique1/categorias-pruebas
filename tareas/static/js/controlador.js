/**
    Esta funcion se ocupa de cargar la categoria adecuada
*/
function categoriaSeleccionada() {
    var selecion = document.getElementById("categ");
    if (selecion.options[selecion.selectedIndex].text == "Todas") {
        window.location.href = "{% url 'listaTareas' %}"
    } else {
        window.location.href = selecion.value;
    }
}