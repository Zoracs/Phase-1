from requests.exceptions import ConnectTimeout, ReadTimeout, Timeout
import get_FC_members
from unittest.mock import patch
import pytest

@patch("get_Discord_members.requests.get")
def test_custom_request(mock):
    mock.side_effect = ConnectTimeout

    with pytest.raises(ConnectTimeout):
        assert get_FC_members.get_FC_members()

@patch('get_FC_members.requests.get')
def test_that_function_returns_list(mock):
    FC_data = {
        "FreeCompanyMembers": [


            {
                "Avatar": "https://img2.finalfantasyxiv.com/f/1216d7090fd1aa97f5fd6b47fdef60ea_7206469080400ed57a5373d0a9c55c59fc0_96x96.jpg?1604161298",
                "FeastMatches": 0,
                "ID": 10315359,
                "Lang": "null",
                "Name": "Dr Suna",
                "Rank": "パイナップル",
                "RankIcon": "https://img.finalfantasyxiv.com/lds/h/Z/W5a6yeRyN2eYiaV-AGU7mJKEhs.png",
                "Server": "Lich (Light)"
            },
            {
                "Avatar": "https://img2.finalfantasyxiv.com/f/9d4b3bbd4d191a08a507f8c591f01ad1_7206469080400ed57a5373d0a9c55c59fc0_96x96.jpg?1604159473",
                "FeastMatches": 0,
                "ID": 14276998,
                "Lang": "null",
                "Name": "Freya Luna",
                "Rank": "チェリー",
                "RankIcon": "https://img.finalfantasyxiv.com/lds/h/b/cliLaxMGlva579Q7-BGQofaHoU.png",
                "Server": "Lich (Light)"
            },
            {
                "Avatar": "https://img2.finalfantasyxiv.com/f/091ee11e331858902b9265cea64501a2_7206469080400ed57a5373d0a9c55c59fc0_96x96.jpg?1604161092",
                "FeastMatches": 0,
                "ID": 18532177,
                "Lang": "null",
                "Name": "Diablo Devil",
                "Rank": "桃",
                "RankIcon": "https://img.finalfantasyxiv.com/lds/h/6/p94F1j-5xhM2ySM16VNrA08qjU.png",
                "Server": "Lich (Light)"
            }]
    }
    mock.return_value.json.return_value = FC_data
    assert get_FC_members.get_FC_members(
    ) == ['Dr Suna', 'Freya Luna', 'Diablo Devil']
