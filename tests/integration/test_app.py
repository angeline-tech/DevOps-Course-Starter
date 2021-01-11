from tests.utils.string_utils import bytesContain
from tests.utils.card_utils import empty_array, sample_cards
from tests.utils.trello_utils import raw_cards
import pytest
from todo_app.app import create_app
from dotenv import find_dotenv, load_dotenv
import todo_app.service.trello_service as trello_service


@pytest.fixture
def client():

    load_dotenv('.env.test', override=True)
    # # Create the new app.
    test_app = create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client: 
        yield client

@pytest.fixture
def mocked_requests(monkeypatch):
    # monkeypatch.setattr(trello_service,"fetch_updated_cards",empty_array)
    monkeypatch.setattr(trello_service,"request_cards",raw_cards)
    

 
def test_heartbeat(client):
    response = client.get('/heartbeat')
    assert response.status_code == 200
    assert bytesContain(response.data,"Flask Server is Running") 

def test_index(mocked_requests,client):
    response = client.get('/')
    assert response.status_code == 200
    assert bytesContain(response.data,"My Fake In Progress Task") 
    assert bytesContain(response.data,"My Fake Completed Task") 
    assert bytesContain(response.data,"My Fake Task To Be Done") 