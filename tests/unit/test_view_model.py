import pytest

import tests.utils.card_utils as util
from todo_app.data.ViewModel import ViewModel


@pytest.fixture
def full_view_model():
    return ViewModel(util.SampleCards, True)


@pytest.fixture
def empty_view_model():
    return ViewModel([], True)


@pytest.fixture
def done_view_model():
    return ViewModel(util.DoneCards, True)


def test_can_return_all_cards(full_view_model):
    assert full_view_model.items == util.SampleCards


def test_can_just_to_do_cards(full_view_model):
    assert full_view_model.to_do_items == [util.to_do]


def test_can_return_just_in_progress_cards(full_view_model):
    assert full_view_model.in_progress_items == [util.in_progress]


def test_can_return_just_complete_cards(full_view_model):
    assert full_view_model.complete_items == [util.done]


def test_can_handle_no_cards(empty_view_model):
    assert empty_view_model.items == []
    assert empty_view_model.to_do_items == []
    assert empty_view_model.in_progress_items == []
    assert empty_view_model.complete_items == []

def test_can_return_just_complete_cards(done_view_model):
    assert done_view_model.recently_done_items == [util.new_done_card]
