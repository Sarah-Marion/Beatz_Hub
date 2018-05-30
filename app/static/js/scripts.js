$(document).ready(function () {
    $('#close-nav').click(function () {
        document.getElementById("primary-nav").style.width = "0";
    })
    $('#open-nav').click(function(){
        document.getElementById("primary-nav").style.width = "250px";
    })
})