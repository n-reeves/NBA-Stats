function authorCallback(json) {
  var books = json;

  var tableContents = '<tr><th>Title</th><th>Year</th></tr>';
  for (var i = 0; i < books.length; i++) {
    tableContents += '<tr><td>'
                  + books[i]['title']
                  + '</td><td>'
                  + books[i]['year']
                  + '</td></tr>';
  }

  var bookTable = document.getElementById('bookTable');
  bookTable.innerHTML = tableContents;
}

function onGetBooks() {
  var url = '/booksBy/' + document.getElementById('authorField').value;
  var xhp = new XMLHttpRequest();
  xhp.open('get', url);

  xhp.onreadystatechange = function() {
    if (xhp.readyState == 4 && xhp.status == 200) {
      authorCallback(JSON.parse(xhp.response));
    }
  }

  xhp.send();
}
