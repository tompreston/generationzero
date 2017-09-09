/**
 * JS for entry wells
 */
var EntryWell = {
	slide_opts: {duration: 300, easing: 'swing'},
};


$(document).ready(function () {
    EntryWell.masonry_grid = $('.grid').masonry({
        columnWidth: '.grid-sizer',
        gutter: '.gutter-sizer',
        itemSelector: '.grid-item',
        percentPosition: true
    });

    $('.entry-well')
    .mouseenter(function() {
        $(this).find('.entry-well-header').slideDown(EntryWell.slide_opts);
    })
    .mouseleave(function() {
        $(this).find('.entry-well-header').slideUp(EntryWell.slide_opts);
    });

    // init Masonry
    var $grid = $('.grid').masonry({
      itemSelector: '.grid_item',
      transitionDuration: 0
    });

    // layout Masonry after each image loads
    $grid.imagesLoaded().progress(function() {
      $grid.masonry('layout');
    });

});
