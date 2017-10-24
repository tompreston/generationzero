var Masthead = {
	show_masthead: true,
	hidden: false,
	hiding: false,
};

/* hide the masthead */
Masthead.hide = function() {
	$("#masthead_container").slideUp({
		duration: 'slow',
		start: function(){
			$("#branding").fadeIn();
			/* prevent scrolling
			*/
		},
		done: function () {
			/* reenable scrolling
			*/
			Masthead.hidden = true;
			$('body').removeClass('stop-scrolling');
			console.log("DONE");
		}
	});
};

Masthead.scroll = function() {
	var scrollPosition = $(window).scrollTop();
	console.log("scrollPosition "+scrollPosition+" hidden "+Masthead.hidden);
	if (scrollPosition > 2){
		if (!Masthead.hidden) {
			window.scrollTo(0, 0);
			$('body').addClass('stop-scrolling');
			if (!Masthead.hiding) {
				Masthead.hide();
			}
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

