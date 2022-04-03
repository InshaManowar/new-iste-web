(function($){
    'use stict';
    var browserWindow = $(window);

    // :: 1.0 Preloader Active Code
    browserWindow.on('load', function () {
      $('.message1').remove();
      $('.loading').remove();
      $('.logo_iste').addClass("zoom");
        $('.preload').fadeOut('slow', function () {
            $(this).remove();
        });
    });

    if($.fn.owlCarousel){
    var owl = $('.owl-carousel');
    owl.owlCarousel({
    animateOut: 'fadeOut',
    autoplay:true,
    dots: false,
    smartSpeed: 1000,
    center: true,
    autoplayTimeout:5000,   
    autoplayHoverPause:true,
      margin: 10,
      nav: true,
      loop: true,
      navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
      responsive: {
        0: {
          items: 1
        },
        600: {
          items: 2
        },
        1000: {
          items: 3
        }
      }
    });

    }
    

})(jQuery);