from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

result = {}
for item in contacts_list:
    name = (' '.join([item[0], item[1], item[2]])).split(' ')
    field = ' '.join([name[0], name[1]])
    pattern_phone = r"(8|\+7)[(\s]*(\d{3})[-)\s]*(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})\s*[(]?([доб.]*\s*\d*)[)]?"
    sub = r"+7(\2)\3-\4-\5 \6"
    if field not in result:
        result[field] = {'surname': '', 'organization': '', 'position': '', 'phone': '', 'email': ''}
    if name[2] != '':
        result[field]['surname'] = name[2]
    if item[3] != '':
        result[field]['organization'] = item[3]
    if item[4] != '':
        result[field]['position'] = item[4]
    if item[5] != '':
        result[field]['phone'] = re.sub(pattern_phone, sub, item[5])
    if item[6] != '':
        result[field]['email'] = item[6]
# pprint(result)

contacts = []
for name, name_data in result.items():
    item = name.split(' ')
    item.append(name_data.get('surname'))
    item.append(name_data.get('organization'))
    item.append(name_data.get('position'))
    item.append(name_data.get('phone'))
    item.append(name_data.get('email'))
    contacts.append(item)
# pprint(contacts)

with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    data = csv.writer(f, delimiter=',')
    data.writerows(contacts)
