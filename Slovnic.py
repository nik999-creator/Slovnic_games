games = {"Roblox":"evade and others",
         "Minecraft":"New world",
         "Genshin":"Diluc and others"}
answer = input("Додати нову гру? 1 - так 0 - ні")
while answer != "0":
    game = input("Введи гру")
    ingame = input("Введи що хочешь до цієї гри")
    games[game] = {"Гра":game, "До гри":ingame}
    answer = input("Додати нову гру? 1 - так 0 - ні")
print("Список ігр, зареєстрований на сайті")
for game in games:
    print(game)
q1 = input("Введи гру")
if q1 in games:
    print(games[q1])
else:
    print("Такої гри немає") 