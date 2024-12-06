team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'
str1 = "В команде Мастера кода участников: %d !" % team1_num
str2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(str1)
print(str2)
str23 = "Команда Волшебники данных решила задач: {} !".format(score_2)
str24 = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(str23)
print(str24)
str25 = f"Команды решили {score_1} и {score_2} задач."
str26 = f"Результат битвы: {challenge_result}"
str27 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."
print(str25)
print(str26)
print(str27)