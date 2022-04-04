import requests
import html

parameter = {
    "amount": 10,
    "type": "boolean"
}
request = requests.get(url="https://opentdb.com/api.php", params=parameter)
request.raise_for_status()
data = request.json()
question_data = data["results"]