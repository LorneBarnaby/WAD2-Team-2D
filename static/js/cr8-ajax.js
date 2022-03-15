$(document).ready(function() {
	$('#openbtn').click(function() {
		
		$.get('/cr8/generate_prizes/',

			function(data) {
				
				var prize = JSON.parse(data);
				
				$('#prizeName').html(prize.prizeName);
				$('#prizeImage').attr("src", prize.prizeImg);
				$('#openbtn').hide();
				
			})
	});
});