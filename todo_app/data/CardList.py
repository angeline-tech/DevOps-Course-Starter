from todo_app.data.Card import Card


class CardList:
    def __init__(self, cards: [], ascending):
        self.cards = cards
        self.ascending = ascending

    def get_sorted_cards(self):
        if self.ascending == "ASCENDING":
            return sorted(self.cards, key=lambda x: x.status, reverse=True)
        elif self.ascending == "DESCENDING":
            return sorted(self.cards, key=lambda x: x.status, reverse=False)
        return self.cards

    def update_cards(self, new_cards):
        self.cards = new_cards

    def sort_by_status(self, ascending: bool):
        self.ascending = ascending


def to_card(raw_card):
    return Card(raw_card["id"], raw_card["name"], raw_card["status"])
