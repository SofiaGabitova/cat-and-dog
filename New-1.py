print('Новый файл в main и создание КОНФЛИКТА')

import random
group = ['Магиева', 'Веселовский', 'Кехер']
bass_players_dict = {'Веселовский' : 142, 'Кехер' : 50, 'Панагов' : 46,
                         'Данилов' : 3, 'Филь' : 6, 'Коротков' : 8,
                         'Листочкин' : 12, 'Печенкин' : 22}


name = random.choice(group)
sum_grade_concert = 10 + 5 + 2 + 7 + 9
date = [5, 6, 7, 4, 6]
total = round(sum_grade_concert / len(date))
print(sum_grade_concert / len(date))
print(total)