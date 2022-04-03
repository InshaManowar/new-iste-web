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

})(jQuery);