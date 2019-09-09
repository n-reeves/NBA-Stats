function searchSinglePlayer(){
	window.location.href =  document.getElementById('playerField').value;
	
}
function searchTwoPlayer() {
	var urlWindow = window.location + '';
	var urlList = urlWindow.split('/Player/');
	var newURL = urlList[0] + '/twoPlayer/' + document.getElementById('playerField1').value + '&' + document.getElementById('playerField2').value;
	window.location.href = newURL;
	
}


