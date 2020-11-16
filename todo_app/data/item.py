class Card:

    def __init__(self, card_id, description, status):
        self.card_id = card_id
        self.description = description
        self.status = status


def to_card(raw_card):
    return Card(raw_card["id"], raw_card["name"], raw_card["status"])
