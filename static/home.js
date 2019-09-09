

//Basic Search Functions for Buttons
function searchSinglePlayer(){
	window.location.href = window.location + 'Player/' + document.getElementById('playerField').value;
}

function searchTwoPlayer() {
	window.location.href = window.location + 'twoPlayer/' + document.getElementById('playerField1').value + '&' + document.getElementById('playerField2').value;
}


//functions that populate dropdown search preview for single player search
function searchCallBack(results) {
  var players = results;
  var max = Math.min(3,players.length);
  var listContents = '';
  
  for (var i = 0; i < max; i++) {
	var nameList = players[i]['player_name'].split(' ');
	var name = nameList[0] + '_' + nameList[1];
	var link = window.location + 'Player/' + name;
	var bar = ' ' + players[i]['player_name'] + ' (' + players[i]['start_year'] + '-' + players[i]['end_year'] + ')'
    listContents += '<li><a href = ' + link + ' >' + bar + '</a></li>';
                               
  }
  var searchUL = document.getElementById('searchUL');
  searchUL.innerHTML = listContents;
}

function onChangeSearch() {
  var url = window.location +'Search/' + document.getElementById('playerField').value;
  var xhp = new XMLHttpRequest();
  xhp.open('get', url);
  xhp.onreadystatechange = function() {
    if (xhp.readyState == 4 && xhp.status == 200) {
      searchCallBack(JSON.parse(xhp.response));
    }
  }
  xhp.send();
}

//functions that populate drop down search for first input
function fillSearch1(name) {
	var name = name;
	console.log(name);
	var nameList = name.split('_');
	var search = nameList[0] + ' ' + nameList[1];
	var playerField1 = document.getElementById('playerField1');
	playerField1.value = search;
}

function searchCallBackTwoPlayer1(results) {
  var players = results;
  var max = Math.min(3,players.length);
  var listContents = '';
  for (var i = 0; i < max; i++) {
	var bar = ' ' + players[i]['player_name'] + ' (' + players[i]['start_year'] + '-' + players[i]['end_year'] + ')';
	var nameList = players[i]['player_name'].split(' ');
	var name = nameList[0] + '_' +nameList[1];
    listContents += '<li id ="' + name +'" onclick="fillSearch1(this.id)">' + bar + '</li>';
	
  }
  var searchUL1 = document.getElementById('searchUL1');
  searchUL1.innerHTML = listContents;
}


//functions that populate drop down for second input for two player search
function onChangeSearchTwoPlayer1() {
  var url = window.location +'Search/' + document.getElementById('playerField1').value;
  var xhp = new XMLHttpRequest();
  xhp.open('get', url);
  xhp.onreadystatechange = function() {
    if (xhp.readyState == 4 && xhp.status == 200) {
      searchCallBackTwoPlayer1(JSON.parse(xhp.response));
    }
  }
  xhp.send();
}

function fillSearch2(name) {
	var name = name;
	console.log(name);
	var nameList = name.split('_');
	var search = nameList[0] + ' ' + nameList[1];
	var playerField2 = document.getElementById('playerField2');
	playerField2.value = search;
}

function searchCallBackTwoPlayer2(results) {
  var players = results;
  var max = Math.min(3,players.length);
  var listContents = '';
  for (var i = 0; i < max; i++) {
	var bar = ' ' + players[i]['player_name'] + ' (' + players[i]['start_year'] + '-' + players[i]['end_year'] + ')';
	var nameList = players[i]['player_name'].split(' ');
	var name = nameList[0] + '_' +nameList[1];
    listContents += '<li id ="' + name +'" onclick="fillSearch2(this.id)">' + bar + '</li>';
	
  }
  var searchUL2 = document.getElementById('searchUL2');
  searchUL2.innerHTML = listContents;

}


function onChangeSearchTwoPlayer2() {
  var url = window.location +'Search/' + document.getElementById('playerField2').value;
  var xhp = new XMLHttpRequest();
  xhp.open('get', url);
  xhp.onreadystatechange = function() {
    if (xhp.readyState == 4 && xhp.status == 200) {
      searchCallBackTwoPlayer2(JSON.parse(xhp.response));
    }
  }
  xhp.send();
}

