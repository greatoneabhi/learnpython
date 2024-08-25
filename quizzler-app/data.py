import requests

query_params = {"amount": 10, "difficulty": "easy", "type": "boolean"}

response = requests.get(url="https://opentdb.com/api.php", params=query_params)
response.raise_for_status()
data = response.json()
question_data = data["results"]
