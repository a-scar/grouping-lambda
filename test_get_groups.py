import json

returned_data = [{'client_num': 819390246, 'accounts': [{'account_id': 83437354934, 'effectiveEndDate': '9999-12-31'},
                                                        {'account_id': 2923840949, 'effectiveEndDate': '9999-12-31'}]},
                 {'client_num': 353535535, 'accounts': [{'account_id': 34325325, 'effectiveEndDate': '9999-12-31'}]},
                 {'client_num': 343432325, 'accounts': [{'account_id': 57587484789, 'effectiveEndDate': '9999-12-31'}]}]


def test_returns_proper_structure():
    from main import get_groups

    with open('fake_response.json') as f:
        good_response = json.load(f)

    assert get_groups(good_response) == returned_data


def test_client_without_accounts():
    from main import get_groups

    with open('client_without_accounts.json') as f:
        no_accounts = json.load(f)

    assert get_groups(no_accounts) == []


def test_client_missing_accounts():
    from main import get_groups

    with open('client_missing_fields.json') as f:
        missing_fields = json.load(f)

    assert get_groups(missing_fields) == []