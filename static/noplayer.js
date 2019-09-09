function searchTwoPlayer() {
	var urlWindow = window.location + '';
	var urlList = urlWindow.split('/');
	var urlBase = urlList[0] + '//' + urlList[2] +'';
	var newURL = urlBase+ '/twoPlayer/' + document.getElementById('playerField1').value + '&' + document.getElementById('playerField2').value;
	window.location.href = newURL;
}
function searchSinglePlayer() {
	var urlWindow = window.location + '';
	var urlList = urlWindow.split('/');
	var urlBase = urlList[0] + '//' + urlList[2] +'';
	var newURL = urlBase+ '/Player/' + document.getElementById('playerField').value;
	window.location.href = newURL;
}