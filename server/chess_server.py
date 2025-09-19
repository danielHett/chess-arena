from flask import Flask, request, jsonify, abort
import secrets
import uuid
from helpers import parse_state_string
from engine import is_valid_move

"""
Server used for playing games. 
"""

app = Flask(__name__)

# TODO: Find a better way to store this information. 
games = { '1': { 'state': 'foo', 'join_pass': 'foo', 'pass_white': 'foo', 'pass_black': 'foo' } }

# Caller passes a password. A game ID and unique password are generated and given back to the caller. The 
# caller uses the generated password to make moves for their own color. The ID passed to the server is used
# to join the game. The password passed to the server is used in the join path. 
@app.post("/create")
def create_game():
    content = request.json 
    if 'password' not in content:
        abort(400)

    # Create the object for the new game and add it to the database. 
    new_game_id = str(uuid.uuid4())
    new_game_pass_white = secrets.token_hex(128)
    new_game = { 'state': 'rnbqkbnrpppppppp32PPPPPPPPRNBQKBNR w', 'password': content['password'], 'pass_white': new_game_pass_white }
    games[new_game_id] = new_game

    return jsonify({ 'password': new_game_pass_white, 'game_id': new_game_id })

# Need to givet this path an ID and the password. The caller gets back another randomly generated password 
# to use for their own color. 
@app.post("/join")
def join_game():

    # TODO: Write some code here. 

    return 0

# Used to get the state of a game. No password needed for this path. 
@app.get("/games/<game_id>")
def get_game(game_id):
    print(games)
    print(game_id)
    
    if game_id not in games: 
        abort(404)
    
    return games.get(game_id).get('state')

"""
For updating the state of the game. 
"""
@app.post("/games/<game_id>")
def play_game(game_id):
    # First, does this game exist?
    if game_id not in games: 
        abort(404)

    game = games.get(game_id)

    # Pull all content from the request. 
    # Make sure that the right fields are in the body of the request. 
    content = request.json()
    if 'password' not in content or 'move' not in content:
        abort(400)
    
    # Next, does this person have the authority to update the state?
    # Whose turn is it? Then what is the password for that player? If the password matches, then we can continue. 
    required_password = game['pass_white'] if parse_state_string(game['state'])['player'] == 'w' else game['pass_black']
    if required_password != content['password']:
        abort(401)

    # Is the move valid? 
    # TODO: Someone write the code to check if the move is valid. 
    if not is_valid_move(game['state'], content['move']):
        abort(401)

    # If the move is valid, then update the board and return a valid response code. 
    # TODO: Write the code to update the board.  

    return 200