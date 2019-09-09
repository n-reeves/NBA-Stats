import psycopg2
import flask
from flask import render_template, jsonify
import json
import sys

# Import database configuration

database="reevesn"
user="reevesn"
password="happy556eye"


# Start Flask server
app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def searchBar(name):
    players

@app.route('/authorViewer')
def authorViewer():
    return render_template('authorViewer.html')

@app.route('/viewAuthor/<last_name>')
def viewAuthor(last_name):
    books = get_books_for_author_from_db(last_name)
    return render_template('author.html',
                           last_name=last_name,
                           books=books)

@app.route('/booksBy/<last_name>')
def get_books_for_author(last_name):
    books = get_books_for_author_from_db(last_name)
    return json.dumps(books)

def get_books_for_author_from_db(last_name):
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        cursor = connection.cursor()
        query = '''SELECT books.title, books.publication_year
                   FROM books, authors, books_authors
                   WHERE books.id=books_authors.book_id
                   AND authors.id=books_authors.author_id
                   AND authors.last_name = %s'''
        cursor.execute(query, (last_name,))
        books = []
        for row in cursor:
            books.append({'title': row[0], 'year': row[1]})
        connection.close() # TODO: can I move this?
        return books
    except Exception as e:
        print(e)
        return [{'title': 'The Ghost Seer', 'year': 1789},
                {'title': 'On the Aesthetic Education of Man', 'year': 1794}]

if __name__=='__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
