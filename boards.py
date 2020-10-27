from typing import Dict, Any

BOARDS = [
    {
        "board_name": "Game 1: My New End",
        "board_id": 1111,
        "proclamation_promulged_fenix": 0,
        "proclamation_promulged_death_eater": 0,
        "deck_codification": 1010,
        "is_spell_active": False
    },
    {
        "id_board": 1000,
        "proclamation_promulged_fenix": 0,
        "proclamation_promulged_death_eater": 1,
        "deck_codification": 1010,
        "is_spell_active": False
    },
    {
        "id_board": 1002,
        "proclamation_promulged_fenix": 1,
        "proclamation_promulged_death_eater": 0,
        "deck_codification": 1010,
        "is_spell_active": False
    },
]

def get_board_by_id(board_id: int) -> Dict[str, Any]:
    res_board = None
    for board in BOARDS:
        if board["id"] == board_id:
            res_board = board
            break
    return res_board