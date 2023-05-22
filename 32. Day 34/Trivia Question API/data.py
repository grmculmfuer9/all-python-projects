import requests

parameters = {
    "amount": 10,
    "difficulty": "medium",
    "type": "boolean",
    "category": 18
}

data = requests.get(url="https://opentdb.com/api.php", params=parameters).json()
question_data = data["results"]
