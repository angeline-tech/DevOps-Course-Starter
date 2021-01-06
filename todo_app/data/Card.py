class Card:

    def __init__(self, card_id, description, status):
        self.card_id = card_id
        self.description = description
        self.status = status

    @classmethod
    def from_raw(cls, raw_card):
        return cls(raw_card["id"], raw_card["name"], raw_card["status"])

    @classmethod
    def to_do(cls):
        return "To-do"

    @classmethod
    def in_progress(cls):
        return "In Progress"

    @classmethod
    def done(cls):
        return "Done"
