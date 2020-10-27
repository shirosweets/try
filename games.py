from typing import Dict, Any

GAMES = [
    {
        "game_id": 1,
        "game_name": "Game 1: My New End",
        "game_user": "Manson Candy",
        "is_active": True
    },
    {
        "game_id": 2,
        "game_name": "Game 2: El mundo del revés",
        "game_user": "Emy",
        "is_active": True
    },
    {
        "game_id": 3,
        "game_name": "Game 3: The chaos",
        "game_user": "Puppy",
        "is_active": False
    },
    {
        "id": 4,
        "name": "Game 4: No name guy",
        "game_user": "The God",
        "is_active": True
    },
    {
        "id": 5,
        "name": "Game 4: Kinda",
        "game_user": "MyCatIsVoldemort",
        "is_active": True
    },
    {
        "id": 6,
        "name": "Game 4: OK",
        "game_user": "IAmVoldemort",
        "is_active": True
    },
]

def get_game_by_id(game_id: int) -> Dict[str, Any]:
    res_game = None
    for game in GAMES:
        if game["id"] == game_id:
            res_game = game
            break
    return res_game