import requests

response = requests.post("https://hn25.ibaguette.com/leaderboard", json={
    "name": "test_user",
    "score": 1234
})