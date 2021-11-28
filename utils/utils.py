def add_int(a, b):
    result = a + b
    return result


def add_float(a, b) -> float:
    result = a + b
    return result


def compare_two_number(a: int, b: int):
    if a == b:
        print(f'A {a} equals B {b}')
    elif a > b:
        print(f'A {a} greater than B {b}')
    else:
        print(f'A {a} less than B {b}')
