$(document).ready(function(){
	if(window.location.href == (window.location.origin + "/")){
		$(window).scroll(function() {
			var scrollPosition = $(window).scrollTop();
			if (scrollPosition > 190){
				$("#masthead").slideUp( "slow", function(){
					$("#branding").fadeIn();
					$("#menu").css("display", "inline-block");
				});
			}
		});
	} else {
		$("#masthead").hide();
		$("#branding").fadeIn();
		$("#menu").css("display", "inline-block");
	}
});