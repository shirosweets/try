from db_entities_relations import Game, Player, Board, Log
from pony.orm import db_session
from models import ViewBoard, ViewGame

#@db_session
#def add_players_to_game(playerList):
#    print("Adding all players on the lobby")
#
#    print("Players Added")


## Esto lo hacemos para ver como construir a partir de modelos, no necesariamente va a ser asi...
@db_session
def createGame(gameModelObj: ViewGame):
    print("Creating a new game from ViewGame...")
    g= Game(game_is_started= gameModelObj.game_is_started, 
    game_next_minister= gameModelObj.game_next_minister, 
    game_failed_elections= gameModelObj.game_failed_elections, 
    game_step_turn= gameModelObj.game_step_turn, 
    game_last_director= gameModelObj.game_last_director, 
    game_last_minister= gameModelObj.game_last_minister)
    createBoardFromGame(g)
    print("Game Added! ≧◉ᴥ◉≦\n")

@db_session
def createGame_alone(gameDict):
    print("Creating a new game...")
    g = Game(game_is_started= gameDict["game_is_started"], 
    game_next_minister= gameDict["game_next_minister"], 
    game_failed_elections= gameDict["game_failed_elections"], 
    game_step_turn= gameDict["game_step_turn"], 
    game_last_director= gameDict["game_last_director"], 
    game_last_minister= gameDict["game_last_minister"])
    createBoardFromGame(g)
    print("Game Added! ≧◉ᴥ◉≦")

@db_session
def createBoard(brdDict):
    print("Creating a new board...\n")
    Board(board_game = Game[brdDict["board_game"]], 
    board_promulged_fenix= brdDict["board_promulged_fenix"],
    board_promulged_death_eater= brdDict["board_promulged_death_eater"], 
    board_deck_codification= brdDict["board_deck_codification"], 
    board_is_spell_active= brdDict["board_is_spell_active"] )
    print("Board Added! ≧◉ᴥ◉≦")

@db_session
def testFunc():
    print(Game[1])

@db_session
def showDatabase():
    print("---|Games|---(id, game_board_game, game_is_started, game_next_minister, game_failed_elections, game_step_turn, game_last_director, game_last_minister)")
    Game.select().show()
    print("\n---|Boards|---(id, board_game, board_promulged_fenix, board_promulged_death_eater, board_deck_codification, board_is_spell_active)")
    Board.select().show()
    print("\n---|Players|---(id, player_game, player_number, player_nick, player_role, player_is_alive, player_chat_blocked, player_director, player_minister)")
    Player.select().show()

@db_session
def createBoardFromGame(vGame: ViewGame):
    print("Creating a new board from game...\n")
    Board(board_game = vGame, 
    board_promulged_fenix= 0, 
    board_promulged_death_eater= 0, 
    board_deck_codification= 10101010, # Reemplace 10101010 from logical deck
    board_is_spell_active= 0)
    print("Board Added ≧◉ᴥ◉≦")

@db_session
def add_proclamation_card_on_board(is_fenix: True, card_Board: Board): # Change True for "card"
    print("Adding a new proclamation card o board...\n")
    # is_fenix: True
    if is_fenix:
        Board.board_promulged_fenix = Board.board_promulged_fenix + 1
    # is_fenix: False
    else: 
        Board.board_promulged_death_eater = Board.board_promulged_death_eater + 1
    print("Proclamation card added on board ≧◉ᴥ◉≦")

# game1 is python dictionary

game1 = { "game_is_started": False, 
            "game_next_minister": -1,
            "game_failed_elections": 0, 
            "game_step_turn": -1,
            "game_last_director": -1,
            "game_last_minister": -1
        }

game2 = { "game_is_started": True, 
            "game_next_minister": -1,
            "game_failed_elections": 0, 
            "game_step_turn": 0,
            "game_last_director": -1,
            "game_last_minister": -1
        }

# Recordar que board_game es el indice de la base de datos. 
# Cuando lo usemos dentro de una db_session hay que hacer Game[1]
board1= { "board_game": 1, 
          "board_promulged_fenix": 0,
          "board_promulged_death_eater": 0,
          "board_deck_codification": 1010, 
          "board_is_spell_active": False
}


"""
class ViewPlayerGame(BaseModel):
    player_game_id : int    # Depends on Game
    player_number: int    # Defines order
    player_nick: str    # = userName Depends on User
    player_role: -1   # = -1 No asigned
    player_is_alive: True    # = True
    player_chat_blocked: False    # = False
    player_director: False
    player_minister: False
    player_last_director: -1    # = -1 No asigned
    player_last_minister: -1    # = -1 No asigned
"""

"""
player1 = ViewPlayerGame(
    
)"""

# Reemplace 4 for "logical select"
thisgameModel = ViewGame(game_next_minister=4)
createGame(thisgameModel)

thisgameModel2 = ViewGame(game_next_minister=7)
createGame(thisgameModel2)

showDatabase()
#testFunc()

#boardModel = ViewBoard()
#print(boardModel.board_is_spell_active)

#print(json.dumps(game1))

#game1.select().show()
#print(db)

check_board = ViewGame[2].Board
check_game = thisgameModel2(game_is_started= True)

showDatabase()

#db.bind('sqlite', 'data_base.sqlite', create_db=True) # 1)
#db.generate_mapping(create_tables=True) # 2)

