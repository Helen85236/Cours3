import json
from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def sorted_key(x):
    return x['date']


def sort_data(data):
    data = sorted(data, key=sorted_key, reverse=True)
    return data[0:5]


def format_cart(cart):
    sender = cart.split()
    formated_cart = sender.pop(-1)
    cart_info = " ".join(sender)
    formated_cart = f"{cart_info} {formated_cart[:4]} {formated_cart[4:6]}** **** {formated_cart[-4:]}"

    return formated_cart


def format_data(data):
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']
        if "from" in row:
            from_arrow = "->"
            sender = format_cart(row['from'])
            dest = format_cart(row['to'])
            tt = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        else:
            sender = "Открытие счета"
            from_arrow = ""
            tt = ""
            dest = ""

        formatted_data.append(f"""
{date} {description}
{sender} {from_arrow} {tt} {dest}
          """)

    return formatted_data
