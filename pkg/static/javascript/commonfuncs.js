$(document).ready(function(){
    $("#show").on({
        click: function(){
            $("#password").attr("type","text")
        },
        mouseleave: function() {
            $("#password").attr("type","password")
        }
    });
});

function goBack() {
    window.history.back();
}

//Bootstrap tooltip starts
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });
//Bootstrap tooltip ends