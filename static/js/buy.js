/*
window.onload = function() {
   if (window.jQuery) {
      alert('jQuery is loaded');
   } else {
      alert('jQuery is not loaded');
  }
}*/

$(document).ready(function(){
	$("#range").val(0);
	$("#value").val(parseFloat(0.00).toFixed(2));
	$("#units").val(0);
	$("#yow").click(function(){

		alert("jjj")
		alert($("#price").html().replace("Price: ",""))
	})
	$('#range').on('input change', function(){
		let price = parseFloat($("#price").html().replace("Price: ",""));
		
    	$('#value').val(($(this).val()*price).toFixed(2))
    	$('#units').val($(this).val())
    });
    $("#units").on('input change', function(){
    	let price = parseFloat($("#price").html().replace("Price: ",""));
    	$('#value').val(($(this).val()*price).toFixed(2))
    })

})