def add_everything_up(a, b):
    try:
        result = a + b
        if isinstance(result, (int, float)):
            return(round(result,3))


    except TypeError as exc:
        if isinstance(a, str):
            return(a + str(b))
        else:
            return(str(a) + str(b))



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
