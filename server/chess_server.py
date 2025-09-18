from flask import Flask
from flask import request

"""
Server used for playing games. 
"""

app = Flask(__name__)

# TODO: Find a better way to store this information. 
games = { '1': { 'state': 'foo', 'pass_share': 'foo', 'pass_white': 'foo', 'pass_black': 'foo' } }

# Caller passes a password. A game ID and unique password are generated and given back to the caller. The 
# caller uses the generated password to make moves for their own color. The ID passed to the server is used
# to join the game. The password passed to the server is used in the join path. 
@app.post("/create")
def create_game():
    
    # TODO: Write some code here. 
    
    return 0

# Need to givet this path an ID and the password. The caller gets back another randomly generated password 
# to use for their own color. 
@app.post("/join")
def join_game():

    # TODO: Write some code here. 

    return 0

# Used to get the state of a game. No password needed for this path. 
@app.get("/games/<game_id>")
def get_game(game_id):
    if game_id not in games: 
        # TODO: Send back some sort of error?
        return 'bad'
    
    game = games.get(game_id)

    if 'state' not in game:
        # TODO: More serious error. 
        return 'reall_bad'
    
    state = games.get(game_id).get('state')
    
    return state