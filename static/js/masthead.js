$(document).ready(function(){
	if(window.location.href == (window.location.origin + "/")){
		setTimeout(function(){ 		
			$("#masthead").slideUp( "slow", function(){
				$("#branding").css("display", "inline-block");
				$("#menu").css("display", "inline-block");
			});
		}, 1000);
	} else {
		$("#masthead").hide();
		$("#branding").css("display", "inline-block");
		$("#menu").css("display", "inline-block");
	}
});