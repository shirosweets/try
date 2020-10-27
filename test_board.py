from fastapi.testclient import TestClient
from fastapi import status

client = TestClient(app)

from typing import Dict, Any

def test_get_single_game():
    response = client.get("/games/5/1111/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "board_id": 1111,
        "proclamation_promulged_fenix": 0,
        "proclamation_promulged_death_eater": 0,
        "deck_codification": 1010,
        "is_spell_active": False
    }