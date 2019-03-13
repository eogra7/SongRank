import shelve
import random
from bottle import route, run, template, static_file, post, request


mean_elo = 1500
elo_width = 400
k_factor = 64





class Song:
    __lastId = 1

    def __init__(self, name):
        self.name = name
        self.elo = 1500
        self.id = Song.__lastId
        Song.__lastId += 1
        
    def title(self):
        tmp = self.name.split('-')
        return tmp[0]
        
    def artist(self):
        tmp = self.name.split('-')
        return tmp[1]
    
def import_songs(filename):
    with open(filename) as f:
        content = f.readlines()
        for x in content:
            x = x.strip()
            d["songs"].append(Song(x))
            
            
d = shelve.open("songs_db", writeback=True)
if "songs" not in d:
    print("No database found, creating a new one.")
    d["songs"] = []
    print("Importing songs from songs.txt..")
    import_songs("songs.txt")
    d.sync()
    print("Done!")

def update_elo(winner_elo, loser_elo):
    """
    https://en.wikipedia.org/wiki/Elo_rating_system#Mathematical_details
    """
    expected_win = expected_result(winner_elo, loser_elo)
    change_in_elo = k_factor * (1-expected_win)
    winner_elo += change_in_elo
    loser_elo -= change_in_elo
    return winner_elo, loser_elo

def expected_result(elo_a, elo_b):
    """
    https://en.wikipedia.org/wiki/Elo_rating_system#Mathematical_details
    """
    expect_a = 1.0/(1+10**((elo_b - elo_a)/elo_width))
    return expect_a


        
def list_songs():
    newlist = sorted(d["songs"], key=lambda x: x.elo, reverse=True)
    for song in newlist:
        print("%s: %s" % (song.elo, song.name))

def faceoff(a, b):
    result = update_elo(b.elo, a.elo)
    a.elo = result[0]
    b.elo = result[1]
    
def insert_random(a, l=d["songs"]):
    l.insert(random.randrange(0, len(l)-1), a)
        

# random.shuffle(d["songs"])
# # for song in shuffled:
# #         print("%s: %s" % (song.elo, song.name))
# for x in range(3):
#     a = d["songs"].pop()
#     b = d["songs"].pop()
#     choice = input("(1) %s\n(2) %s\n" % (a.name, b.name))
#     if(choice == 1):
#         faceoff(a, b)
#     else:
#         faceoff(b, a)
#     insert_random(d["songs"], a)
#     insert_random(d["songs"], b)
#     d.sync()
    
#list_songs()




@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route('/')
def index():
    a = d["songs"].pop()
    b = d["songs"].pop()
    song_pair = [a, b]
    insert_random(a)
    insert_random(b)
    song_list = sorted(d["songs"], key=lambda x: x.elo, reverse=True)
    return template('index', song_pair=song_pair, song_list=song_list)
    
@post('/evaluate')
def post_evaluate():
    print("got here")
    winner_id = int(request.forms.get('winner'))
    loser_id = int(request.forms.get('loser'))
    winner = Song("")
    loser = Song("")
    for song in d["songs"]:
        if song.id == winner_id:
            print(song.name)
            winner = song
        if song.id == loser_id:
            print(song.name)
            loser = song
    
    # winner = next((x for x in d["songs"] if x.id() == winner_id), None)
    # loser = next((x for x in d["songs"] if x.id() == loser_id), None)
    print("winner: %s" % winner.name)
    print("loser: %s" % loser.name)
    if winner is not None and loser is not None:
        faceoff(winner, loser)
        print("faceoff %s %s" % (winner_id, loser_id))
        return 'ok'
    else:
        print("error %s %s" % (winner_id, loser_id))
        return 'error'
    
run(host='0.0.0.0', port=80)

d.close()
        



