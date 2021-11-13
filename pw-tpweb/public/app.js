function openNav() {
    document.getElementById("mobile__menu").style.width = "100%";
}
function closeNav() {
    document.getElementById("mobile__menu").style.width = "0";
}
$(document).ready(function(){
    $(".owl-carousel").owlCarousel(
    {
        nav:true,
        margin:10,
        dots:false,
        Responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:5,
            }
        }
    }
    );
});