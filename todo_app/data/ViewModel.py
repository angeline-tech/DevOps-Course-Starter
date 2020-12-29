class ViewModel:
    def __init__(self, cards, sort_status):
        self._cards = cards
        self._sort_status = sort_status

    @property
    def items(self): return self._cards
    @property
    def sort_status(self): return self._sort_status
