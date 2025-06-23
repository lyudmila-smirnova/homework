def filter_by_state(list_data:list, state:str ='EXECUTED') -> list:
    """Функция принимает на вход список словарей с данными о банковских операциях
    и параметр state, возвращает новый список, содержащий только те словари,
    у которых ключ state содержит переданное в функцию значение."""
    new_list_data = []
    for temp_dict in list_data:
        if temp_dict['state'] == state:
            new_list_data.append(temp_dict)
    return new_list_data

list_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


print(filter_by_state(list_data, state='CANCELED'))


def sort_by_date(list_data:list, reverse:bool =True)-> list:
    """Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате."""
    sort_list_data_revers = sorted(list_data, key=lambda temp_dict: temp_dict['date'], reverse=reverse)
    return sort_list_data_revers


print(sort_by_date(list_data, reverse=False))
