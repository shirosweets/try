from pony.orm import db_session, select, count
from db_entities_relations import *
from models import *
from typing import Optional

#some users functions
#some lobby funtions
#some player functions
#some game functions

#some board functions
#@db_session
# Obtener un objeto Board = id : int
#def fun_read_board():
#    return Board.proclamation_promulged_fenix, Board.proclamation_promulged_death_eater, Board.deck_codification

@db_session
def iniciated_sesion():
    fun_add_proclamation(False, 1)
    return {"iniciated_sesion": True}

@db_session
def check_chaos(board: Board):
    check: bool
    return check

@db_session
def fun_add_proclamation(is_fenix: bool, game_id : ViewGame):
    
    #game_id = Game(game_id= 1, game_name= "Game My New End", game_user= "Manson Candy", is_active= True)
    board = ViewBoard()
    print(board.board_is_spell_active)
    

#some end_match functions


#some log functions