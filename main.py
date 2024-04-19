import requests

API_KEY = "YOUR API KEY"

ENDPOINT = "https://api.api-ninjas.com/v1/"

CATEGORY = "sucess"

headers={
    "X-Api-Key": API_KEY
}

response = requests.get(url=f"{ENDPOINT}/quotes?caterory={CATEGORY}", headers=headers)

print(response.json())