from todo_app.data.Card import Card

to_do = Card("1", "This needs to be done", Card.to_do())
in_progress = Card("2", "Nearly finished this", Card.in_progress())
done = Card("3", "Done done done", Card.done())

SampleCards = [to_do, in_progress, done]
