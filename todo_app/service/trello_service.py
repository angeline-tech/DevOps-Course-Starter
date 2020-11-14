import requests
import os

trello = "https://api.trello.com/1/"
auth = "?key={0}&token={1}".format(os.getenv("TRELLO_API_KEY"), os.getenv("TRELLO_TOKEN"))


def get_cards_in_list(list_id, status):
    url = trello+"lists/"+os.getenv(list_id)+"/cards"+auth
    response = requests.get(url)
    raw_cards = response.json()
    parsed_cards = []
    for card in raw_cards:
        card["status"] = status
        parsed_cards.append(card)
    return parsed_cards

def create_to_do(description):
    url = "https://api.trello.com/1/cards/?key={apiKey}&token={token}&idList={list_id}&name={name}"


def get_all_cards():
    to_do_cards = get_cards_in_list("TRELLO_TO_DO", "To-Do")
    in_progress_cards = get_cards_in_list("TRELLO_IN_PROGRESS", "In Progress")
    done_cards = get_cards_in_list("TRELLO_DONE", "Done")
    return to_do_cards + in_progress_cards + done_cards
