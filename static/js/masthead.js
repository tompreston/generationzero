var Masthead = {
	show_masthead: true,
	hidden: false,
};

/* hide the masthead */
Masthead.hide = function() {
	$("#masthead").slideUp({
		duration: 'slow',
		start: function(){
			$("#branding").fadeIn();
			/* prevent scrolling */
			$('html, body').css({
				overflow: 'hidden',
				height: '100%'
			});
		},
		done: function () {
			/* reenable scrolling */
			$('html, body').css({
				overflow: 'auto',
				height: 'auto'
			});
		}
	});
};

Masthead.scroll = function() {
	var scrollPosition = $(window).scrollTop();
	if (scrollPosition > 2){
		if (!Masthead.hidden) {
			Masthead.hide();
			Masthead.hidden = true;
		}
	}
};

$(document).ready(function(){
	// if we're on the home page and not on a mobile device
	var show_masthead =
		window.location.href == (window.location.origin + "/") &&
		$('#masthead').css('display') != 'none';

	if (show_masthead) {
		$(window).scroll(Masthead.scroll);
	} else {
		$("#masthead").hide();
		$("#branding").show();
	}
});

