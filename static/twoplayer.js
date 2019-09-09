function searchTwoPlayer(){
	window.location.href =  document.getElementById('playerField1').value + '&' + document.getElementById('playerField2').value;
	
}
function searchSinglePlayer() {
	var urlWindow = window.location + '';
	var urlList = urlWindow.split('/twoPlayer/');
	var newURL = urlList[0] + '/Player/' + document.getElementById('playerField').value;
	window.location.href = newURL;
	
}
