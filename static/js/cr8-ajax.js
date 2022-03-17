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
	
	$('.claimbtns').click(function() {
		
		var achievementIdVar;
		achievementIdVar = $(this).attr('data-achievementid');
		
		
		$.get('/cr8/claim_achievement/',
			{'achievement_id':achievementIdVar},
			function(data) {
				
				var achievement = JSON.parse(data);
				
				var claimButtons
				claimButtons = document.getElementsByClassName("claimbtns");
				
				for (var i=0; i<claimButtons.length;i++) {
						if (claimButtons[i].getAttribute('data-achievementid') == achievementIdVar) {
							if (achievement.criteriaIsMet == "True") {
								claimButtons[i].innerHTML = "Claimed: " + achievement.achievementName;
							} else {
								claimButtons[i].innerHTML = "Criteria not met!";	
							}
						}
				}

				
				
			});
			
			
	});
	
	$('.sellbtns').click(function() {
		
		var prizeIdVar;
		prizeIdVar = $(this).attr('data-prizeid');
		
		
		$.get('/cr8/sell_prize/',
			{'prize_id':prizeIdVar},
			function(data) {
				
				var prize = JSON.parse(data);
				
				var claimButtons;
				claimButtons = document.getElementsByClassName("sellbtns");
				
				for (var i=0; i<claimButtons.length;i++) {
						if (claimButtons[i].getAttribute('data-prizeid') == prizeIdVar) {
							claimButtons[i].innerHTML = "Sold for " + prize.prizeValue;
						}
				}
			
			$('#usercurrency').html(prize.updated_currency);
			$('#' + prizeIdVar).hide();
			
				
			});
			
			
	});
	
	
});

// stub function for selling prizes
$('.sellable').click(function(){
    alert(this.id);
});