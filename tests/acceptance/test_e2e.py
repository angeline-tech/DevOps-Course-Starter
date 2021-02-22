import os
from threading import Thread
import pytest
from todo_app.app import create_app
from todo_app.service.trello_service import create_board, delete_board
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv


@pytest.fixture(scope='module')
def test_app():
# Create the new board & update the board id environment variable 
    load_dotenv('.env', override=True)
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
    with webdriver.Firefox(executable_path=os.getenv("GECKO_PATH")) as driver:
        yield driver
        driver.close()

def addTodoToDriver(driver):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'
    input = driver.find_element_by_name("title")
    input.clear()
    input.send_keys("SELENIUM")
    input.send_keys(Keys.RETURN)
    new_todo = driver.find_elements_by_id("todo_row_SELENIUM")
    time.sleep(2)

def test_can_add_and_delete_a_todo(test_app,driver):
    addTodoToDriver(driver)
    time.sleep(2)
    found = driver.find_elements_by_id("todo_row_SELENIUM")
    assert len(found) > 0
    driver.find_element_by_id("todo_delete_SELENIUM").click()
    found = driver.find_elements_by_id("todo_row_SELENIUM")
    assert len(found) == 0

def test_can_move_an_item_between_lists(test_app,driver):
    addTodoToDriver(driver)
    driver.find_element_by_id("todo_to_in_progress_SELENIUM").click()
    time.sleep(1)
    assert len(driver.find_elements_by_id("doing_row_SELENIUM")) > 0
    driver.find_element_by_id("doing_to_complete_SELENIUM").click()
    time.sleep(1)
    assert len(driver.find_elements_by_id("done_row_SELENIUM")) > 0    
    driver.find_element_by_id("done_to_todo_SELENIUM").click()
    time.sleep(1)
    assert len(driver.find_elements_by_id("todo_row_SELENIUM")) > 0    
    driver.find_element_by_id("todo_to_complete_SELENIUM").click()
    time.sleep(1)
    assert len(driver.find_elements_by_id("done_row_SELENIUM")) > 0    
    driver.find_element_by_id("done_to_in_progress_SELENIUM").click()
    time.sleep(1)
    assert len(driver.find_elements_by_id("doing_row_SELENIUM")) > 0    
    driver.find_element_by_id("doing_to_todo_SELENIUM").click()
    time.sleep(1)
    assert len(driver.find_elements_by_id("todo_row_SELENIUM")) > 0

    


