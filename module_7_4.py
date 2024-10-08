# задание по теме "Форматирование строк"

# Переменная team1_num с количеством участников в команде "Мастера кода"
team1_num = 6

# Переменная team2_num с количеством участников в команде "Волшебники данных"
team2_num = 6

# Переменная score_1 с количеством задач решённых командой "Мастера кода"
score_1 = 40

# Переменная score_2 с количеством задач решённых командой "Волшебники данных"
score_2 = 42

# Переменная team1_time с временем за которое команда "Мастера кода" решила все задачи
team1_time = 1552.512
# Переменная team1_time_avg со средним временем, за которое команда "Мастера кода" решили каждую задачу
team1_time_avg = (team1_time/score_1)

# Переменная team2_time с временем, за которое команда "Волшебники данных" решила все задачи
team2_time = 2153.31451
# Переменная team2_time_avg со средним временем, за которое команда "Волшебники данных" решили каждую задачу
team2_time_avg = (team2_time/score_2)

# Переменная challenge_result (исход соревнования)
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# Переменная tasks_total (количество задач, решенных обеими командами)
tasks_total = score_1 + score_2

# Переменная time_avg (среднее время решения)
time_avg = (team1_time_avg + team2_time_avg)/2

# Пример итоговой строки: "В команде Мастера кода участников: 5 ! "
team1_res = "В команде Мастера кода участников: %d !" % team1_num
print(team1_res)

# Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"
team2_res = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(team2_res)

# Пример итоговой строки: "Команда Волшебники данных решила задач: ____ !"
team2_scr_res = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(team2_scr_res)

# Пример итоговой строки: "Мастера кода решили задачи за ____ с !"
team1_time_res = "Мастера кода решили задачи за {:.1f} с !".format(team1_time)
print(team1_time_res)

# Пример итоговой строки: "Волшебники данных решили задачи за ____ с !"
team2_time_res = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(team2_time_res)

# Пример итоговой строки: "Команды решили 40 и 42 задач.”
score_total = f"Команды решили {score_1} и {score_2} задач."
print(score_total)

# Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"
result = f"Результат битвы: {challenge_result}!"
print(result)

# Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
tasks_total_time = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"
print(tasks_total_time)
