import requests
import os

api_key = os.getenv("TRELLO_API_KEY")
trello_token = os.getenv("TRELLO_TOKEN")
list_id = os.getenv("TRELLO_LIST_ID")


def get_all_cards():

    url = "https://api.trello.com/1/lists/{listId}/cards?key={apiKey}&token={trelloToken}".format(listId=list_id, apiKey=api_key, trelloToken=trello_token)
    print(url)
    response = requests.get(url)
    raw_cards = response.json()
    parsed_cards = []
    for card in raw_cards:
        parsed_cards.append(card)
    return parsed_cards
