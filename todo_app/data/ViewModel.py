from todo_app.data.Card import Card


class ViewModel:
    def __init__(self, cards, sort_status):
        self._cards = cards
        self._sort_status = sort_status

    @property
    def items(self): return self._cards

    @property
    def sort_status(self): return self._sort_status

    @property
    def to_do_items(self): return list(filter(lambda x: x.status == Card.to_do(), self._cards))

    @property
    def in_progress_items(self): return list(filter(lambda x: x.status == Card.in_progress(), self._cards))

    @property
    def complete_items(self): return list(filter(lambda x: x.status == Card.done(), self._cards))
