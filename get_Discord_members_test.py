from unittest.mock import Mock, patch
import get_Discord_members

@patch("get_Discord_members.requests.get")
def test_get_the_Members_from_DiscordAPI(mock):
    null = None
    false = None
    true = None
    Discord_Data= [
    {
        "user": {
            "id": "151189447956758528",
            "username": "Deadly Spectrum",
            "avatar": "6d187088143f1b834aaf6999d4f53ef2",
            "discriminator": "2461",
            "public_flags": 0
        },
        "roles": [],
        "nick": null,
        "premium_since": null,
        "joined_at": "2019-05-26T19:04:44.061000+00:00",
        "is_pending": false,
        "mute": false,
        "deaf": false
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
        "nick": "Dr Suna",
        "premium_since": null,
        "joined_at": "2019-05-26T19:02:53.026000+00:00",
        "is_pending": false,
        "mute": false,
        "deaf": false
    },
    {
        "user": {
            "id": "229641448776007680",
            "username": "Zoracs",
            "avatar": "1fddb1e54e40975d347ce092f33d5a2f",
            "discriminator": "9707",
            "public_flags": 0
        },
        "roles": [
            "759774212595777567"
        ],
        "nick": "Yuki",
        "premium_since": null,
        "joined_at": "2019-06-05T21:09:16.684000+00:00",
        "is_pending": false,
        "mute": false,
        "deaf": false
    },
    {
        "user": {
            "id": "343401853888757772",
            "username": "Gogo",
            "avatar": "07c42bdd4a589a11ce8fa7d4c4d7fc9f",
            "discriminator": "5319",
            "public_flags": 0
        },
        "roles": [],
        "nick": "Diablo",
        "premium_since": null,
        "joined_at": "2019-06-07T19:23:45.172000+00:00",
        "is_pending": false,
        "mute": false,
        "deaf": false
    },
    {
        "user": {
            "id": "346354930774179845",
            "username": "CipherAres",
            "avatar": "9f761f047610cafbb7f0ea5df4413207",
            "discriminator": "7148",
            "public_flags": 256
        },
        "roles": [],
        "nick": "Ys",
        "premium_since": null,
        "joined_at": "2019-05-26T19:11:27.494000+00:00",
        "is_pending": false,
        "mute": false,
        "deaf": false
    },
    {
        "user": {
            "id": "394764671158190082",
            "username": "Ichiro",
            "avatar": "c10264b89ad3d9c4bde65eaea778fee2",
            "discriminator": "6649",
            "public_flags": 0
        },
        "roles": [],
        "nick": "RAGE MODE [ON]",
        "premium_since": null,
        "joined_at": "2019-08-01T23:29:24.191000+00:00",
        "is_pending": false,
        "mute": false,
        "deaf": false
    },
    {
        "user": {
            "id": "485759618006515715",
            "username": "Rin",
            "avatar": null,
            "discriminator": "7460",
            "public_flags": 0
        },
        "roles": [],
        "nick": null,
        "premium_since": null,
        "joined_at": "2019-06-05T21:15:05.180000+00:00",
        "is_pending": false,
        "mute": false,
        "deaf": false
    },
    {
        "user": {
            "id": "637351433032826891",
            "username": "Straef",
            "avatar": null,
            "discriminator": "8509",
            "public_flags": 0
        },
        "roles": [],
        "nick": null,
        "premium_since": null,
        "joined_at": "2019-10-25T18:15:05.730000+00:00",
        "is_pending": false,
        "mute": false,
        "deaf": false
    },
    {
        "user": {
            "id": "679346229213134888",
            "username": "Burts",
            "avatar": "7f28588b8bd73e5104ced7cc703d2e80",
            "discriminator": "4067",
            "public_flags": 0
        },
        "roles": [],
        "nick": "Freya Luna",
        "premium_since": null,
        "joined_at": "2020-02-18T15:23:00.922000+00:00",
        "is_pending": false,
        "mute": false,
        "deaf": false
    },
    {
        "user": {
            "id": "768869912801968141",
            "username": "Zoracs_Project",
            "avatar": null,
            "discriminator": "0392",
            "public_flags": 0,
            "bot": true
        },
        "roles": [
            "759774212595777567"
        ],
        "nick": null,
        "premium_since": null,
        "joined_at": "2020-11-03T16:42:00.599000+00:00",
        "is_pending": false,
        "mute": false,
        "deaf": false
    },
    {
        "user": {
            "id": "773221655883284490",
            "username": "fuckDiscord",
            "avatar": null,
            "discriminator": "1249",
            "public_flags": 0,
            "bot": true
        },
        "roles": [],
        "nick": null,
        "premium_since": null,
        "joined_at": "2020-11-03T16:39:54.772000+00:00",
        "is_pending": false,
        "mute": false,
        "deaf": false
    }
]
    mock.return_value.json.return_value = Discord_Data
    assert get_Discord_members.get_Discord_members() == ['Deadly Spectrum', 'Dr Suna', 'Yuki', 'Diablo', 'Ys', 'RAGE MODE [ON]', 'Rin', 'Straef', 'Freya Luna', 'Zoracs_Project', 'fuckDiscord']
