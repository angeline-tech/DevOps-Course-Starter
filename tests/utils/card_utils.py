from todo_app.data.Card import Card
from datetime import datetime, timedelta

to_do = Card("1", "This needs to be done", Card.to_do, datetime.now())
in_progress = Card("2", "Nearly finished this", Card.in_progress, datetime.now())
done = Card("3", "Done done done", Card.completed, datetime.now()-timedelta(days=1))
new_done_card = Card("4", "Just finished", Card.completed, datetime.now())
old_done_card = Card("5", "finished ages ago", Card.completed, datetime.now()-timedelta(days=7))

SampleCards = [to_do, in_progress, done]

DoneCards = [done, new_done_card, old_done_card]
