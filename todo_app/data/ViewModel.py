from datetime import datetime

from typing import List

from todo_app.data.Card import Card


class ViewModel:
    def __init__(self, cards: List[Card], sort_status, show_all_done_items=False):
        self._cards = cards
        self._sort_status = sort_status
        self._show_all_done_items = show_all_done_items

    @property
    def items(self): return self._cards

    @property
    def sort_status(self): return self._sort_status

    @property
    def show_all_done_items(self): return self._show_all_done_items

    @property
    def to_do_items(self): return list(filter(lambda x: x.status == Card.to_do, self._cards))

    @property
    def in_progress_items(self): return list(filter(lambda x: x.status == Card.in_progress, self._cards))

    @property
    def complete_items(self): return list(filter(lambda x: x.status == Card.completed, self._cards))

    @property
    def recently_done_items(self): return list(filter(lambda x: x.completed_today, self._cards))

    @property
    def all_done_items(self): return list(filter(lambda x: x.status == Card.completed, self._cards))
