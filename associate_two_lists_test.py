import associate_two_lists
from unittest.mock import patch

FC_data_with_spaces = {
        "FreeCompanyMembers": [


            {
                "Avatar": "https://img2.finalfantasyxiv.com/f/1216d7090fd1aa97f5fd6b47fdef60ea_7206469080400ed57a5373d0a9c55c59fc0_96x96.jpg?1604161298",
                "FeastMatches": 0,
                "ID": 10315359,
                "Lang": "null",
                "Name": "test space",
                "Rank": "パイナップル",
                "RankIcon": "https://img.finalfantasyxiv.com/lds/h/Z/W5a6yeRyN2eYiaV-AGU7mJKEhs.png",
                "Server": "Lich (Light)"
            },
            {
                "Avatar": "https://img2.finalfantasyxiv.com/f/9d4b3bbd4d191a08a507f8c591f01ad1_7206469080400ed57a5373d0a9c55c59fc0_96x96.jpg?1604159473",
                "FeastMatches": 0,
                "ID": 14276998,
                "Lang": "null",
                "Name": "test1 space",
                "Rank": "チェリー",
                "RankIcon": "https://img.finalfantasyxiv.com/lds/h/b/cliLaxMGlva579Q7-BGQofaHoU.png",
                "Server": "Lich (Light)"
            }]
    }
FC_data = {
        "FreeCompanyMembers": [


            {
                "Avatar": "https://img2.finalfantasyxiv.com/f/1216d7090fd1aa97f5fd6b47fdef60ea_7206469080400ed57a5373d0a9c55c59fc0_96x96.jpg?1604161298",
                "FeastMatches": 0,
                "ID": 10315359,
                "Lang": "null",
                "Name": "test",
                "Rank": "パイナップル",
                "RankIcon": "https://img.finalfantasyxiv.com/lds/h/Z/W5a6yeRyN2eYiaV-AGU7mJKEhs.png",
                "Server": "Lich (Light)"
            },
            {
                "Avatar": "https://img2.finalfantasyxiv.com/f/9d4b3bbd4d191a08a507f8c591f01ad1_7206469080400ed57a5373d0a9c55c59fc0_96x96.jpg?1604159473",
                "FeastMatches": 0,
                "ID": 14276998,
                "Lang": "null",
                "Name": "test1",
                "Rank": "チェリー",
                "RankIcon": "https://img.finalfantasyxiv.com/lds/h/b/cliLaxMGlva579Q7-BGQofaHoU.png",
                "Server": "Lich (Light)"
            }]
    }
Discord_Data = [
        {
            "user": {
                "id": "151189447956758528",
                "username": "Deadly Spectrum",
                "avatar": "6d187088143f1b834aaf6999d4f53ef2",
                "discriminator": "2461",
                "public_flags": 0
            },
            "roles": [],
            "nick": "test",
            "premium_since": 'null',
            "joined_at": "2019-05-26T19:04:44.061000+00:00",
            "is_pending": 'false',
            "mute": 'false',
            "deaf": 'false'
        },
        {
            "user": {
                "id": "228512459307220993",
                "username": "Dom",
                "avatar": "f467d7012d63b27a0cbf7b570a1f330b",
                "discriminator": "2876",
                "public_flags": 0
            },
            "roles": [
                "759774212595777567"
            ],
            "nick": "test1",
            "premium_since": 'null',
            "joined_at": "2019-05-26T19:02:53.026000+00:00",
            "is_pending": 'false',
            "mute": 'false',
            "deaf": 'false'
        }
    ]
@patch('get_Discord_members.requests.get')
def test_if_ingested_files_produce_a_list_from_Discord_members(mock):
    
    mock.return_value.json.return_value = Discord_Data
    result = associate_two_lists.get_lists('Discord')
    assert result == ["test", "test1"]

@patch('get_FC_members.requests.get')
def test_if_ingested_files_produce_a_list_from_FC_members(mock):
    
    mock.return_value.json.return_value = FC_data
    result = associate_two_lists.get_lists('XIV_API')
    assert result == ["test", "test1"]

@patch('get_FC_members.requests.get')
def test_if_ingested_files_produce_a_list_from_FC_members_with_spaces(mock):
    
    mock.return_value.json.return_value = FC_data_with_spaces
    result = associate_two_lists.get_lists('XIV_API')
    assert result == ["test space", "test1 space"]

@patch('builtins.input')
@patch('associate_two_lists.get_lists')
def test_function_get_lists_and_mock_input(mock1, mock2):
    
    mock1.return_value = ["Dr Suna"]
    mock2.return_value = 'Dr Suna'
    result = associate_two_lists.establish_relationship_between_the_lists()
    assert result == {'Dr Suna':'Dr Suna'}

@patch('builtins.input')
@patch('associate_two_lists.get_lists')
def test_function_get_lists_and_mock_input_2(mock1, mock2):
    
    mock1.return_value = ["Dr Suna"]
    mock2.return_value = 'Dr Boner'
    result = associate_two_lists.establish_relationship_between_the_lists()
    assert result == 'Nope, try again next time.'

