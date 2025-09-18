from flask import Flask
app = Flask(__name__)

"""
Server used for playing games. 
"""

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
@app.get("/games/<string:game_id>")
def get_game():
    
    # TODO: Write some code here. 
    
    return 0