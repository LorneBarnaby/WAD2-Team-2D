$(document).ready(function() {
	$('#openbtn').click(function() {
		
		$.get('/cr8/generate_prizes/',

			function(data) {
				
				var prize = JSON.parse(data);

				
				$('#prizeName').html(prize.prizeName);
				$('#prizeImage').attr("src", prize.prizeImg).attr("style", "height:250px; width:auto");
				$('#openbtntext').html("RE-ROLL");
				$('#currency').html("Currency: "+prize.updated_currency);
				
			})
	});
	
	$('#claimbtn').click(function() {
		
		var achievementIdVar;
		achievementIdVar = $(this).attr('data-achievementid');
		
		
		$.get('/cr8/claim_achievement/',
			{'achievement_id':achievementIdVar},
			function(data) {
				
				var achievement = JSON.parse(data);

				$('#claimbtntext').html("Claimed: " + achievement.achievementName);
				
			})
	});
	
	
});

// stub function for selling prizes
$('.sellable').click(function(){
    alert(this.id);
});