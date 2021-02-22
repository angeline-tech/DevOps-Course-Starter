from todo_app.data.Card import Card
from datetime import datetime, timedelta

to_do = Card("1", "This needs to be done", Card.to_do, datetime.now())
in_progress = Card("2", "Nearly finished this", Card.in_progress, datetime.now())
done = Card("3", "Done done done", Card.completed, datetime.now()-timedelta(days=1))
new_done_card = Card("4", "Just finished", Card.completed, datetime.now())
old_done_card = Card("5", "finished ages ago", Card.completed, datetime.now()-timedelta(days=7))
old_done_card_1 = Card("6", "finished ages ago 1", Card.completed, datetime.now()-timedelta(days=7))
old_done_card_2 = Card("7", "finished ages ago 2", Card.completed, datetime.now()-timedelta(days=7))
old_done_card_3 = Card("8", "finished ages ago 3", Card.completed, datetime.now()-timedelta(days=7))
old_done_card_4 = Card("9", "finished ages ago 4", Card.completed, datetime.now()-timedelta(days=7))

SampleCards = [to_do, in_progress, done]

DoneCards = [done, new_done_card, old_done_card]

ManyDoneCards = [done, new_done_card, old_done_card, old_done_card_1, old_done_card_2, old_done_card_3, old_done_card_4 ]

def empty_array():
    return []

def sample_cards():
    return SampleCards

def done_cards():
    return DoneCards