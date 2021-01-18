raw_card_1 = {
    "id": "5ff6f948ab975e59422b6b36",
    "checkItemStates": None,
    "closed": False,
    "dateLastActivity": "2021-01-07T12:06:34.692Z",
    "desc": "",
    "descData": None,
    "dueReminder": None,
    "idBoard": "5fada2089844c260662d674d",
    "idList": "DONE",
    "idMembersVoted": [],
    "idShort": 52,
    "idAttachmentCover": None,
    "idLabels": [],
    "manualCoverAttachment": False,
    "name": "My Fake Completed Task",
    "pos": 147456,
    "shortLink": "3zgt2ZxV",
    "isTemplate": False,
    "cardRole": None,
    "badges": {
        "attachmentsByType": {"trello": {"board": 0, "card": 0}},
        "location": False,
        "votes": 0,
        "viewingMemberVoted": False,
        "subscribed": False,
        "fogbugz": "",
        "checkItems": 0,
        "checkItemsChecked": 0,
        "checkItemsEarliestDue": None,
        "comments": 0,
        "attachments": 0,
        "description": False,
        "due": None,
        "dueComplete": False,
        "start": None,
    },
    "dueComplete": False,
    "due": None,
    "idChecklists": [],
    "idMembers": [],
    "labels": [],
    "shortUrl": "https://trello.com/c/3zgt2ZxV",
    "start": None,
    "subscribed": False,
    "url": "https://trello.com/c/3zgt2ZxV/52-do-not-touch",
    "cover": {
        "idAttachment": None,
        "color": None,
        "idUploadedBackground": None,
        "size": "normal",
        "brightness": "light",
    }
}

raw_card_2 = {
    "id": "5ff6e0be67dc30810a1d3458",
    "checkItemStates": None,
    "closed": False,
    "dateLastActivity": "2021-01-07T11:44:10.186Z",
    "desc": "",
    "descData": None,
    "dueReminder": None,
    "idBoard": "5fada2089844c260662d674d",
    "idList": "IN_PROGRESS",
    "idMembersVoted": [],
    "idShort": 45,
    "idAttachmentCover": None,
    "idLabels": [],
    "manualCoverAttachment": False,
    "name": "My Fake In Progress Task",
    "pos": 49152,
    "shortLink": "ifkVVRDs",
    "isTemplate": False,
    "cardRole": None,
    "badges": {
        "attachmentsByType": {"trello": {"board": 0, "card": 0}},
        "location": False,
        "votes": 0,
        "viewingMemberVoted": False,
        "subscribed": False,
        "fogbugz": "",
        "checkItems": 0,
        "checkItemsChecked": 0,
        "checkItemsEarliestDue": None,
        "comments": 0,
        "attachments": 0,
        "description": False,
        "due": None,
        "dueComplete": False,
        "start": None,
    },
    "dueComplete": False,
    "due": None,
    "idChecklists": [],
    "idMembers": [],
    "labels": [],
    "shortUrl": "https://trello.com/c/ifkVVRDs",
    "start": None,
    "subscribed": False,
    "url": "https://trello.com/c/ifkVVRDs/45-2",
    "cover": {
        "idAttachment": None,
        "color": None,
        "idUploadedBackground": None,
        "size": "normal",
        "brightness": "light",
    }
}

raw_card_3 = {
    "id": "5ff6f93a5b2b6156aa942741",
    "checkItemStates": None,
    "closed": False,
    "dateLastActivity": "2021-01-07T12:06:18.299Z",
    "desc": "",
    "descData": None,
    "dueReminder": None,
    "idBoard": "5fada2089844c260662d674d",
    "idList": "TO_DO",
    "idMembersVoted": [],
    "idShort": 50,
    "idAttachmentCover": None,
    "idLabels": [],
    "manualCoverAttachment": False,
    "name": "My Fake Task To Be Done",
    "pos": 114688,
    "shortLink": "eDsSzpm9",
    "isTemplate": False,
    "cardRole": None,
    "badges": {
        "attachmentsByType": {"trello": {"board": 0, "card": 0}},
        "location": False,
        "votes": 0,
        "viewingMemberVoted": False,
        "subscribed": False,
        "fogbugz": "",
        "checkItems": 0,
        "checkItemsChecked": 0,
        "checkItemsEarliestDue": None,
        "comments": 0,
        "attachments": 0,
        "description": False,
        "due": None,
        "dueComplete": False,
        "start": None,
    },
    "dueComplete": False,
    "due": None,
    "idChecklists": [],
    "idMembers": [],
    "labels": [],
    "shortUrl": "https://trello.com/c/eDsSzpm9",
    "start": None,
    "subscribed": False,
    "url": "https://trello.com/c/eDsSzpm9/50-help",
    "cover": {
        "idAttachment": None,
        "color": None,
        "idUploadedBackground": None,
        "size": "normal",
        "brightness": "light",
    }
}

def raw_cards(list_id):
    if(list_id=='TRELLO_TO_DO'):
        return [raw_card_1]  
    if(list_id=='TRELLO_IN_PROGRESS'):
        return [raw_card_2]  
    if(list_id=='TRELLO_DONE'):
        return [raw_card_3]
    else:
        return []
