$(document).ready(function(){
	// if we're on the home page and not on a mobile device
	if(window.location.href == (window.location.origin + "/") &&
			$('#masthead').css('display') != 'none') {
		$(window).scroll(function() {
			var scrollPosition = $(window).scrollTop();
			if (scrollPosition > 190){
				$("#masthead").slideUp({
					duration: 'slow',
					start: function(){
						$("#branding").fadeIn();
					}
				});
			}
		});
	} else {
		$("#masthead").hide();
		$("#branding").show();
	}
});