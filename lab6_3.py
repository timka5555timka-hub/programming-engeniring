from pprint import pprint

def dict_maker(**kwargs):
    my_dict = {'first': 'so easy'}
    my_dict.update(kwargs)
    return my_dict

# Пример использования
result = dict_maker(second=2, third='three', fourth=[1, 2, 3])
pprint(result)
