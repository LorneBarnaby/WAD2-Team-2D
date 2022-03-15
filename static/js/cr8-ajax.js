$(document).ready(function() {
	$('#openbtn').click(function() {
		
		$.get('/cr8/generate_prizes/',

			function(data) {
				
				var prize = JSON.parse(data);

				// $('#cr8-box-container')
				
				$('#prizeName').html(prize.prizeName);
				$('#prizeImage').attr("src", prize.prizeImg);
				$('#openbtn').hide();
				$('#currency').html("Currency: "+updated_currency);
				
			})
	});
});