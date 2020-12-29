class CardList:
    def __init__(self, cards: []):
        self.cards = cards

    def update_cards(self, new_cards):
        self.cards = new_cards

    def get_sorted(self, ascending: bool):
        if ascending:
            return sorted(self.cards, key=lambda x: x.status, reverse=True)
        elif not ascending:
            return sorted(self.cards, key=lambda x: x.status, reverse=False)
        return self.cards
