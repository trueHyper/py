listPlayers = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

playersCount = len(listPlayers)

midIndex = (playersCount) // 2

firstTeam = listPlayers[:midIndex]
secondTeam = listPlayers[midIndex:]

print(firstTeam)
print(secondTeam)
