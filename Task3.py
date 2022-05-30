queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

new_queries = []
for phrase in queries:
    phrase = phrase.split()
    new_queries.append(len(phrase))

lenght_of_the_list = len(new_queries)

counter_of_words_in_phrase = {}
for lenght_of_phrase in new_queries:
    if lenght_of_phrase in counter_of_words_in_phrase:
        counter_of_words_in_phrase[lenght_of_phrase] += 1
    else:
        counter_of_words_in_phrase[lenght_of_phrase] = 1

for number_of_words_in_phrase, sum_of_words_in_phrase in counter_of_words_in_phrase.items():
    percent = sum_of_words_in_phrase / lenght_of_the_list * 100
    print(f'Количество поисковых запросов из {number_of_words_in_phrase} слов - {percent}%')
