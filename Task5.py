start_list = ['2018-01-01', 'yandex', 'cpc', 100]

start_list_reversed = list(reversed(start_list))

for x, y in enumerate(start_list):
    if x < ((len(start_list)) - 1):
        a = start_list_reversed[0]
        b = start_list_reversed[1]
        dictionary = {b: a}
        del start_list_reversed[0]
        start_list_reversed[0] = dictionary
    else:
        break

print(dictionary)
