import requests

endpoint = 'http://localhost:5005/webhooks/rest/webhook'

data = {
    "message":"I am sad"
}

response = requests.post(endpoint, json=data)
print(response.json())