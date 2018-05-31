$(document).ready(function () {
    $('#close-nav').click(function () {
        document.getElementById("primary-nav").style.width = "0";
    })
    $('#open-nav').click(function () {
        document.getElementById("primary-nav").style.width = "250px";
    })
    $(function () {
        $('a[href*=#]').on('click', function (e) {
            e.preventDefault();
            $('html, body').animate({
                scrollTop: $($(this).attr('href')).offset().top
            }, 500, 'linear');
        });
    });
})