from fastapi.testclient import TestClient
from fastapi import status

client = TestClient(app)

from typing import Dict, Any

def test_get_single_board():
    response = client.get("/games/5/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "board_name": "Game 1: My New End",
        "id": 5,
        "name": "Game 4: Kinda",
        "game_user": "MyCatIsVoldemort",
        "is_active": True
    }