def print_dict(d: dict, level : int = 0) -> None:
    for k, v in d.items():
        spaces = "\t" * level
        print(f'{spaces}{k}', end="")
        if isinstance(v, dict):
            print()
            print_dict(v, level + 1)
        else:
            print(repr(v))


def classlookup(cls):
    c = list(cls.__bases__)
    res = {}
    for base in c:
        res[base] = classlookup(base)
    return res


def lookup(cls):
    result = {
        cls: classlookup(cls)
    }
    print_dict(result)
    # return result

def get_info(var):
    print('\t', type(var))
    print('dir\n', dir(var))
    try:
        print('vars\n', vars(var).keys())
    except Exception as e:
        pass