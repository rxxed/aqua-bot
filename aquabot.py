import requests
import json

BOT_TOKEN = "809729972:AAHSOfTP8Qh9WYrMmQ83VYWVIKZpm7JE-Dw"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

# response = requests.get(BASE_URL + "getMe")
# print(response.content.decode("utf8"))

def get_content_from_url(url):
    response = requests.get(url)
    response = response.content.decode("utf8")
    return response

def get_json_from_url(url):
    response = get_content_from_url(url)
    response_json_dict = json.loads(response)
    return response_json_dict
