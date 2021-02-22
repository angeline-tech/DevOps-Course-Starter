from datetime import datetime


class Card:
    to_do = "To Do"
    in_progress = "In Progress"
    completed = "Completed"

    def __init__(self, card_id, description, status, modified: datetime = None):
        self.card_id = card_id
        self.description = description
        self.status = status
        self.modified = modified

    @property
    def completed_today(self):
        return self.status == Card.completed and self.modified.date() == datetime.today().date()

    @classmethod
    def from_raw(cls, raw_card):
        modified = datetime.strptime(raw_card["dateLastActivity"], '%Y-%m-%dT%H:%M:%S.%fZ')
        return cls(raw_card["id"], raw_card["name"], raw_card["status"], modified)

