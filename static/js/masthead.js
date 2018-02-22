var Masthead = {};

/**
 * Returns opacity value based on scrollPosition and mastheadHeight. Currently
 * returns opacity from 0->1 for final 50% of scroll
 */
Masthead.get_opacity = function(scrollPosition, mastheadHeight) {
	var start = mastheadHeight / 2;
	var end = mastheadHeight;
	if (scrollPosition < start) {
		return 0;
	} else if (scrollPosition > end) {
		return 1;
	} else {
		return (scrollPosition - start) / (end - start);
	}
};

/**
 * Set the opacity of the elements we are interested in.
 */
Masthead.set_elm_opacity = function(opacity) {
	$("#branding, #menu-burger-control").css("opacity", ""+opacity);
};

/**
 * Hide the masthead element when we scroll past it.
 */
Masthead.scroll = function() {
	var scrollPosition = $(window).scrollTop();
	var mastheadHeight = $('#masthead').outerHeight(true);

	// only show the small branding and burger control later
	var opacity = Masthead.get_opacity(scrollPosition, mastheadHeight);
	Masthead.set_elm_opacity(opacity);

	// after we go past the masthead, hide it and turn off this logic
	if (scrollPosition > mastheadHeight) {
		$("#masthead").hide();
		window.scrollTo(0, 0);
		$(window).off("scroll");
	}
};

$(document).ready(function() {
	// if we're on the home page and not on a mobile device
	var show_masthead =
		window.location.href == (window.location.origin + "/") &&
		$('#masthead').css('display') != 'none';

	if (show_masthead) {
		$(window).scroll(Masthead.scroll);
	} else {
		$("#masthead").hide();
		Masthead.set_elm_opacity(1);
	}
});

