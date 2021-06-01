function hide_panel(id){
	if(!$(id).hasClass("hidden")){
		$(id).addClass("hidden")
	}
}

function show_panel(id){
	if($(id).hasClass("hidden")){
		$(id).removeClass("hidden")
	}
}

var id = "profile_panel";
$(document).ready(function(){ 
	$(".sidebar").click(function() {
		hide_panel("#"+id)
		$(".sidebar").not($(this)).removeClass("active")
		if(!$(this).hasClass("active")){
			$(this).addClass('active');
		}
		id = jQuery(this).attr("id")+"_panel";
		show_panel("#"+id);
	});

})







