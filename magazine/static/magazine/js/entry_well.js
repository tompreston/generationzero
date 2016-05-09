/**
 * JS for entry wells
 */
var EntryWell = {};


$(document).ready(function () {
    EntryWell.masonry_grid = $('.grid').masonry({
        columnWidth: '.grid-sizer',
        gutter: '.gutter-sizer',
        itemSelector: '.grid-item',
        percentPosition: true
    });

    $('.entry-well')
    .mouseenter(function() {
        $(this).find('.entry-well-header').show();
    })
    .mouseleave(function() {
        $(this).find('.entry-well-header').hide();
    });
});
