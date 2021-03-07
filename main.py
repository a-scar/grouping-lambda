from collections import defaultdict
import json


# first pass on just getting this to work

def get_groups():
    group_list = []

    # load json file into data variable (replace with real service call)
    with open('fake_response.json') as f:
        data = json.load(f)

    # create formatted dict that will use a list type as values
    formatted_dict = defaultdict(list)

    # loop through accounts and create dict with primary owners
    for account in data.get('accounts'):
        for role in account['registeredRoles']:
            if role['isPrimaryOwner']:
                # default dict adds key,value if it does not find it. otherwise it appends
                # this allows us to check for duplicate clients while also creating dict
                formatted_dict[role['clientNum']].append({
                    'account_id': account['accountId'],
                    'effectiveEndDate': account['effectiveEndDate']
                })

    # structure return object with named fields
    # perhaps consider returning nested dict over list of dicts? not sure
    for key, value in formatted_dict.items():
        group_list.append({
            'client_num': key,
            'accounts': value
        })

    print(group_list)
    return group_list


if __name__ == '__main__':
    get_groups()
