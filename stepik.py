def dict_travel(nested_dicts, path=[]):
    for k in nested_dicts:
        if isinstance(nested_dicts[k], dict):
            m = dict(sorted(nested_dicts[k].items()))
            dict_travel(m, path + [k])
        else:

            print(f'{".".join(path + [k])}: {nested_dicts[k]}')


data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)
