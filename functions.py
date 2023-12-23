from datetime import datetime


def get_only_executed_state(operations_date):
    """Функция, которая получает из библиотеки только успешные транзакции"""
    executed_list = []

    for trans in operations_date:
        if "state" in trans.keys():
            if trans["state"] == "EXECUTED":
                executed_list.append(trans)
            else:
                pass
        else:
            pass
    return executed_list


def get_sort_by_date(executed_date):
    """Функция, которая выдает список отсортированных данных по дате"""
    executed_date.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"))
    return executed_date


def print_trans(trans):
    """Функция, которая получает транзакцию и выводит с причесанном виде с информацией, которая
    включает в себя дату транзакции, сумму транзакции, счет транзакции и описание транзакции"""
    date = datetime.strptime(trans["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    description = trans["description"]
    from_itog = ""
    if "from" in trans.keys():
        trans_from = trans["from"]
        trans_from_nomer = trans_from.split(' ')[-1]
        trans_from_nomer_6 = trans_from_nomer[0:4] + ' ' + trans_from_nomer[4:6]
        trans_from_nomer_last_4 = trans_from_nomer[-4:]
        num = (len(trans_from_nomer) - 10 - 2)//4
        from_itog = trans_from[:len(trans_from) - len(trans_from_nomer)] + trans_from_nomer_6 + "** " + "**** "*num + trans_from_nomer_last_4 + " -> "
    trans_to = trans["to"]
    trans_to = trans_to[:5] + "**" + trans_to[-4:]

    operation_amount = trans["operationAmount"]
    amount = operation_amount["amount"]
    currency_name = operation_amount["currency"]["name"]

    str_itog = date + ' ' + description + '\n' + from_itog + str(trans_to) + '\n' + amount + ' ' + currency_name + '.' + '\n'
    print(str_itog)
    return str_itog
