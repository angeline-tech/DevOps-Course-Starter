import requests
import os
import json

from todo_app.data.Card import Card
from todo_app.data.CardList import CardList

trello = "https://api.trello.com/1/"
def auth():
    return "?key={0}&token={1}".format(os.getenv("TRELLO_API_KEY"), os.getenv("TRELLO_TOKEN"))

to_do_list = CardList([])

def request_cards(list_id):
    url = "{0}lists/{1}/cards{2}".format(trello,os.getenv(list_id),auth()) 
    response = requests.get(url)
    return response.json()

def get_cards_in_list(list_id, status):
    trello_cards = request_cards(list_id)
    parsed_cards = []
    for card in trello_cards:
        card["status"] = status
        parsed_card = Card.from_raw(card)
        parsed_cards.append(parsed_card)
    return parsed_cards


def create_to_do(description):
    url = "{0}cards/{1}&idList={2}&name={3}".format(trello,auth(),os.getenv('TRELLO_TO_DO'),description)
    return requests.post(url)


def move_card_to_to_do(card_id):
    url = "{0}cards/{1}{2}&idList={3}".format(trello,card_id,auth(),os.getenv("TRELLO_TO_DO"))
    return requests.put(url)


def move_card_to_in_progress(card_id):
    url = "{0}cards/{1}{2}&idList={3}".format(trello,card_id,auth(),os.getenv("TRELLO_IN_PROGRESS"))
    return requests.put(url)


def move_card_to_complete(card_id):
    url = trello + "cards/" + card_id + auth() + "&idList=" + os.getenv("TRELLO_DONE")
    url = "{0}cards/{1}{2}&idList={3}".format(trello,card_id,auth(),os.getenv("TRELLO_DONE"))
    return requests.put(url)


def delete_card(card_id):
    url = "{0}cards/{1}{2}".format(trello,card_id,auth())
    return requests.delete(url)


def fetch_updated_cards():
    to_do_cards = get_cards_in_list("TRELLO_TO_DO", Card.to_do)
    in_progress_cards = get_cards_in_list("TRELLO_IN_PROGRESS", Card.in_progress)
    done_cards = get_cards_in_list("TRELLO_DONE", Card.completed)
    to_do_list.update_cards(to_do_cards + in_progress_cards + done_cards)


def get_cards(ascending: bool = True):
    return to_do_list.get_sorted(ascending)

def create_lists(board_id,name):
    url = "{0}/lists{1}&idBoard={2}&name={3}".format(trello,auth(),board_id,name)
    response = requests.post(url)
    data = response.json()
    return data['id']


def create_board():
    url = "{0}boards/{1}&name=test".format(trello,auth())
    response = requests.post(url)
    data = response.json()
    boardId = data['id']
    todo_id = create_lists(boardId,"todo_test")
    doing_id = create_lists(boardId,"doing_test")
    done_id = create_lists(boardId,"done_test")
    return boardId,todo_id,doing_id,done_id

def delete_board(boardId:str):
    url = "{0}boards/{1}/{2}".format(trello,boardId,auth())
    response = requests.delete(url)
    return response

