import os
from threading import Thread
import pytest
from todo_app.app import create_app
from todo_app.service.trello_service import create_board, delete_board
from selenium import webdriver

@pytest.fixture(scope='module')
def test_app():
# Create the new board & update the board id environment variable 
    board = create_board()
    os.environ['TRELLO_TO_DO'] = board[1]
    os.environ['TRELLO_IN_PROGRESS'] = board[2]
    os.environ['TRELLO_DONE'] = board[3]
    # construct the new application
    application = create_app()
    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False)) 
    thread.daemon = True
    thread.start()
    yield application
    # Tear Down
    thread.join(1)
    deleted = delete_board(board[0])


@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver

def test_can_create_an_app(test_app,driver):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'