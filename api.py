import psycopg2
import flask
from flask import render_template, jsonify
import json
import sys

database = "reevesn"
user = "reevesn"
password = "happy556eye"

app = flask.Flask(__name__)


@app.route('/')    #Starting URL brings you to the homepage
def index():
    return render_template('home.html')


@app.route('/Search/<input>')  #Queries the database and returns the matching players
def search_bar(input):         # as someone is writing in their query
    results = get_players(input)
    return json.dumps(results)


@app.route('/Player/<player>') #Takes user to stats of player matching their query. Note if there are multiple
def one_player_search(player): #matching players, then the page is the alphabetically first matching player.
    player = player.replace('_', ' ')

    player_info = get_players(player)

    if len(player_info) == 0 or player == "":                   #If there is no matching player, then user is taken to no results page
        return render_template('noplayer.html')
    else:
        stats = get_seasons(player_info)
        return render_template('singleplayer.html', stats=stats, player_info=player_info[0])


#routes to no result with no input
@app.route('/Player/')
def one_player_no_input():
    return render_template('noplayer.html')


#renders Read me page
@app.route('/ReadMe')
def info():
    return render_template('read.html')


#Takes user to comparison page of two players matching their query.
@app.route('/twoPlayer/<player1>&<player2>')
def two_player_search(player1, player2):
    player1_info = get_players(player1)
    player2_info = get_players(player2)
    #If either of query has no matching player, then user taken to no results page
    if len(player2_info) == 0 or len(player1_info) == 0:
        return render_template('noplayer.html')

    else:
        player1_stats = get_seasons(player1_info)
        player2_stats = get_seasons(player2_info)
        #Second check for missing Player Info
        if len(player2_stats) == 0 or len(player1_stats) == 0:
            return render_template('noplayer.html')
        print(player2_stats)
        return render_template('twoplayer.html', player1_info=player1_info[0], player2_info=player2_info[0],
                           stats1=player1_stats, stats2=player2_stats)


#renders no result page if no entry in one of the fields
@app.route('/twoPlayer/&')
def two_player_no_input1():
    return render_template('noplayer.html')


@app.route('/twoPlayer/<player>&')
def two_player_no_input2(player):
    return render_template('noplayer.html')


@app.route('/twoPlayer/&<player>')
def two_player_no_input3(player):
    return render_template('noplayer.html')

#For an inputed player, returns a list of dictionaries corresponding to every season they played
def get_seasons(player_info):
    end_year = player_info[0]['end_year']
    start_year = player_info[0]['start_year']
    player = player_info[0]['player_name']
    stats_full = get_player_stats(player)
    stats = []

    for season in stats_full:
        year = season['year']
        if year <= end_year and year >= start_year:
            stats.append(season)
    return stats

def get_players(name):
    '''
    Returns a list of dictionaries that correspond to players with a name given by the user.

    EX:
    [{'end_year': 2018, 'player_name': 'LeBron James', 'start_year': 2004, 'height': 6-8, 'weight':220, ,birthday:
    ,"college":""}]

    '''
    if not isinstance(name,str):
        raise TypeError
    connection = psycopg2.connect(database=database, user=user, password=password)
    cursor = connection.cursor()
    name = '%' + name + '%'
    query = ''' SELECT * FROM players
                WHERE  UPPER(players.player_name) LIKE UPPER(%s)'''
    cursor.execute(query, (name,))
    players = []
    for row in cursor:
        players.append({"player_name": row[1], "start_year":row[2], "end_year" : row[3], "height": row[5], "weight": row[6],
                        "birthday": row[7], "college": row[8], 'start_season':("%s-%s"%(row[2]-1,row[2])), 'end_season':("%s-%s"%(row[3]-1,row[3]))})
    connection.close()

    return players


def get_player_stats(name):
    #Note this function's parameter will always be the name resulting from a get players Query
    #So we don't need to worry about substrings or Upper vs lower case and extra symbols
    '''
    Returns an array of statistics gathered over one season for a given player name. Seasons are stored in dictionaries in the format
        {'year', name:,'position', 'age','team','games_played','minutes_played','field_goal_pct',
        'three_pt_pct','ft_pct','orb','drb','assists','steals','blocks','turnovers','pf', 'pts'}
    EX:
        [{'assists': 308, 'field_goal_pct': 0.52, 'minutes_played': 2136, 'blocks': 48, 'position': 'PF', 'orb': 153,
        'age': 30, 'Alvan Adams%': 'Alvan Adams', 'pf': 254, 'team': 'PHO', 'games_played': 82, 'ft_pct': 0.883,
        'three_pt_pct': None, 'pts': 1202, 'steals': 115, 'year': 1985, 'turnovers': 197, 'drb': 347},
        {'assists': 324, 'field_goal_pct': 0.502, 'minutes_played': 2005, 'blocks': 46, 'position': 'C', 'orb': 148,
        'age': 31, 'Alvan Adams%': 'Alvan Adams', 'pf': 272, 'team': 'PHO', 'games_played': 78, 'ft_pct': 0.783,
        'three_pt_pct': 0.0, 'pts': 841, 'steals': 103, 'year': 1986, 'turnovers': 206, 'drb': 329}, {'assists': 223,
        'field_goal_pct': 0.503, 'minutes_played': 1690, 'blocks': 37, 'position': 'C', 'orb': 91, 'age': 32,
        'Alvan Adams%': 'Alvan Adams', 'pf': 207, 'team': 'PHO', 'games_played': 68, 'ft_pct': 0.788,
        'three_pt_pct': 0.0, 'pts': 756, 'steals': 62, 'year': 1987, 'turnovers': 139, 'drb': 247},
        {'assists': 183, 'field_goal_pct': 0.496, 'minutes_played': 1646, 'blocks': 41, 'position': 'C', 'orb': 118,
        'age': 33, 'Alvan Adams%': 'Alvan Adams', 'pf': 245, 'team': 'PHO', 'games_played': 82, 'ft_pct': 0.844,
        'three_pt_pct': 0.5, 'pts': 611, 'steals': 82, 'year': 1988, 'turnovers': 140, 'drb': 247}]

    '''
    if not isinstance(name,str):
        raise TypeError
    name = name + '%'
    connection = psycopg2.connect(database=database, user=user, password=password)
    cursor = connection.cursor()
    query = '''        SELECT * FROM stats
                       WHERE stats.name LIKE %s'''
    stats = []

    cursor.execute(query, (name,))

    for row in cursor:
        season = {'year':row[1], 'season':("%s-%s"%(row[1]-1,row[1])), "name" :row[2],'position':row[3], 'age':row[4],'team':row[5],'games_played':row[6],
                  'minutes_played':round(row[7]/row[6],1),'field_goal_pct':row[8], 'three_pt_pct':row[9],'ft_pct':row[10],
                  'orb':round(row[11]/row[6],1), 'drb':round(row[12]/row[6],1),'assists':round(row[13]/row[6],1),
                  'steals':round(row[14]/row[6],1),'blocks':round(row[15]/row[6], 1), 'turnovers':round(row[16]/row[6],1),'pf':round(row[17]/row[6],1),
                  'pts':round(row[18]/row[6],1), 'rebounds': round((row[11]+row[12])/row[6],1)}
        stats.append(season)
    connection.close()
    return stats


if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) != 3:
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
