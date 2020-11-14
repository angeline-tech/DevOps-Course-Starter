import requests
import os

trello = "https://api.trello.com/1/"
auth = "?key={0}&token={1}".format(os.getenv("TRELLO_API_KEY"), os.getenv("TRELLO_TOKEN"))


def get_cards_in_list(list_id, status):
    url = trello+"lists/"+os.getenv(list_id)+"/cards"+auth
    print(url)
    response = requests.get(url)
    raw_cards = response.json()
    parsed_cards = []
    for card in raw_cards:
        card["status"] = status
        parsed_cards.append(card)
    return parsed_cards


def create_to_do(description):
    url = trello+"cards/"+auth+"&idList="+os.getenv("TRELLO_TO_DO")+"&name="+description
    return requests.post(url)


def move_card_to_to_do(card_id):
    url = trello+"cards/"+card_id+auth+"&idList="+os.getenv("TRELLO_TO_DO")
    return requests.put(url)


def move_card_to_in_progress(card_id):
    url = trello+"cards/"+card_id+auth+"&idList="+os.getenv("TRELLO_IN_PROGRESS")
    return requests.put(url)


def move_card_to_complete(card_id):
    url = trello+"cards/"+card_id+auth+"&idList="+os.getenv("TRELLO_DONE")
    return requests.put(url)


def delete_card(card_id):
    url = trello+"cards/"+card_id+auth
    return requests.delete(url)


def get_all_cards():
    to_do_cards = get_cards_in_list("TRELLO_TO_DO", "To-Do")
    in_progress_cards = get_cards_in_list("TRELLO_IN_PROGRESS", "In Progress")
    done_cards = get_cards_in_list("TRELLO_DONE", "Done")
    return to_do_cards + in_progress_cards + done_cards
