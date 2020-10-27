from fastapi import FastAPI, HTTPException, status
from fastapi import WebSocket, WebSocketDisconnect
from models import *
from db_entities_relations import *
from db_functions import *
from boards import BOARDS, get_board_by_id
from games import GAMES, get_game_by_id

app = FastAPI()


#users's endpoints


#lobbies's endpoints


#games's endpoints
@app.post(
    "/games/", 
    response_model=Game,
    status_code=status.HTTP_201_CREATED
)
async def create_new_game(new_game: Game) -> int:
    new_id = len(GAME) + 1
    game_dict = new_game.dict()
    game_dict.update({"id": new_id})
    GAME.append(game_dict)
    return GAME(
        id=new_id, 
        name=new_game.name, 
        operation_result="Succesfully created!")

#boards's endpoints
#@app.get("/games/")
#async def def_get_board(board_id: str):
#    board_ = get_board_by_id(board_id)
#    return {"board_": board_, "board": board_id}

@app.post("/games/")
async def def_select_director(nick: str):
    return {"is_selected": True}

@app.put("/games/") #<game_id>/actions/ #/{actions}/
# actions id is_fenix
async def def_add_proclamation(is_fenix: bool):
    #fun_read_board()
    fun_add_proclamation(is_fenix)
    return {"is_fenix": is_fenix, "proclamation_promulged_card": True}

#logs's endpoints