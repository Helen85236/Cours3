import utils


def test_format_cart():
    assert utils.format_cart("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_filter_data():
    data = [{"state": "EXECUTED", "jeff": "jeffs value"}]
    assert utils.filter_data(data) == [{"state": "EXECUTED", "jeff": "jeffs value"}]


def test_sort_data():
    test_data = [
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {
                "amount": "51463.70",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "to": "Счет 38976430693692818358"
        },
        {
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873",
            "operationAmount": {
                "amount": "56516.63",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "to": "MasterCard 6783917276771847"
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        },
    ]
    sorted_data = utils.sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-07-12T20:41:47.882230', '2018-12-22T02:02:49.564873',
                                                '2018-07-11T02:26:18.671407']


def test_format_data_create():
    test_data = [
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {
                "amount": "51463.70",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "to": "Счет 38976430693692818358"
        }
    ]
    format_data = utils.format_data(test_data)
    assert format_data == ["\n12.07.2019 Перевод организации\nОткрытие счета   \n          "]


def test_format_data_transfer():
    test_data = [
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {
                "amount": "51463.70",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "to": "Счет 38976430693692818358"
        }
    ]
    format_data = utils.format_data(test_data)
    assert format_data == [
        "\n12.07.2019 Перевод организации\nСчет 4889 44** **** 4368 -> 51463.70 USD Счет 3897 64** **** 8358\n          "]
