#Задание 3
my_string = "ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса;_Говнянов Игорь Петрович;22 года;Студент 6 курса"
text = my_string.replace('_','')
words = text.split(";")
for i in range(0,len(words)):
    if ('Петров' in words[i] and words[i].startswith('Петров')):
        print(words[i] + " " + words[i+1] + " " + words[i+2])

