function getUser() {
    name = document.getElementById('nameQR').value;
    console.log(name);
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
$(document).on("change", '#nameQR', function (e) {
    var dir = $("#nameQR option:selected").data("qr")
    if (dir == "") {
        $("#dirQR").attr("alt", "Este usuario aun no tiene código QR")
    } else {
        $("#dirQR").attr("src", "/static/accounts/login/" + dir)
    }

});
function generarQR() {
    var dir = $("#nameQR option:selected").data("qr")
    if (dir = true) {
        const csrftoken = getCookie('csrftoken')
        nombre = $("#nameQR option:selected").val()
        casa = $("#nameQR option:selected").data("casa")
        id = $("#nameQR option:selected").attr("id")
        $.ajax({
            type: "POST",
            dataType: 'json',
            headers: { 'X-CSRFToken': csrftoken },
            url: "http://localhost:8000/newQR/",
            data: { nombre: nombre,
                    casa: casa ,
                    id: id}
        }).done(function (data) {
            console.log(data)
            location.reload()
        });
    } else {
        alert("Este usuario ya tiene un código asignado")
    }
    

    // var name = document.getElementById('nameQR').value;
    // const csrftoken = getCookie('csrftoken');
    // $.ajax({
    //     type: "POST",
    //     dataType: 'json',
    //     headers: { 'X-CSRFToken': csrftoken },
    //     url: "http://localhost:8000/newQR/",
    //     data: { data: name }
    // }).done(function (o) {
    //     print("Se ejecuto bien")
    // });
}
