# print("*** 1. Тааныштыруу ***")

# aty = input("Шарабидин уулу Рамазн: ")
# shaaru = input("Ош облусу, Алай району, Гүлчө шаары: ")
# print(f"Салам, {aty}! Сен {shaaru} шаарынан экенсиң.\n")

# print("--- 2. Кошуучу ---")
# san1 = float(input("Биринчи санды киргизиңиз: "))
# san2 = float(input("Экинчи санды киргизиңиз: "))

# print(f"Суммасы (+): {san1 + san2}")
# print(f"Айырмасы (-): {san1 - san2}")
# print(f"Көбөйтүүсү (*): {san1 * san2}")
# print(f"Бөлүүсү (/): {san1 / san2}\n")

# print("--- 3. Тик бурчтук ---")
# uzundugu = float(input("Узундугун (a) киргизиңиз: "))
# tuurasu = float(input("Туурасын (b) киргизиңиз: "))

# ayantu = uzundugu * tuurasu
# perimetri = 2 * (uzundugu + tuurasu)

# print(f"Аянты: (a * b) {ayantu}")
# print(f"Периметри: 2 * (a + b)): {perimetri}\n")

# print("--- 4. Убакыт ---")
# sekund = int(input("Секунддарды киргизиңиз: "))

# Saat = sekund // 3600
# minuta = (sekund % 3600) // 60
# kalgan_sekund = sekund % 60

# print(
#     f"{sekund} секунд = {saat} саат, {minuta} минута, {kalgan_sekund} секунд\n"
#     )


# print("--- 5. Чакан кассир ---")
# baasu = float(input("Баасын киргизиңиз: "))
# sany = int(input("Саны: "))

# jalpy_summa = baasu * sany
# arzandatuu = jalpy_summa * 0.9
# tolo_summasy = jalpy_summa - arzandatuu

# print(f"Жалпы баштапкы сумма: {jalpy_summa} сом")
# print(f"Арзандатылган сумма (10%): {arzandatuu} сом")
# print(f"Арзандатуу менен төлөнүүчү акыркы сумма: {tolo_summasy} сом")





# Запросить возраст пользователя
# jash = int(input("Жашыңызды киргизиңиз: "))

# # Проверка условия
# if jash >= 18:
#     print("Кирүүгө уруксат берилет! ")
# else:
#     print("Кирүүгө уруксат жок! ")


# ball = int(input("Топтогон баллды киргизиңиз (0-100): "))

# if ball < 0 or ball > 100:
#     print("Ката: Мындай балл болушу мүмкүн эмес! 0 менен 100дүн ортосундагы сан жазыңыз!")
# elif ball >= 90:
#     print("Сиздин бааңыз: 5 (Эң жакшы 🌟)")
# elif ball >= 75:
#     print("Сиздин бааңыз: 4 (Жакшы 👍)")
# elif ball >= 50:
#     print("Сиздин бааңыз: 3 (Канааттандырарлык ✍️)")
# else:
#     print("Сиздин бааңыз: 2 (Канааттандырарлык эмес, дагы аракет кылыңыз 📚)")








# san = int(input("Бир сан киргизиңиз: "))
# if san % 2 == 0:
#     print("Бул жуп сан")
# else:
#     print("Бул так сан")




# akkaunt = "abdulbasit"
# parol = 9876
# login_akkaunt = input("logindi kirgiziniz: ")
# login_parol = int(input("paroldu kirgiziniz: "))
# if login_akkaunt == akkaunt and login_parol == parol:
#     print("Kosh keldiniz")
# elif login_akkaunt != akkaunt and parol == login_parol:
#     print("login kata")
# elif login_akkaunt == akkaunt and login_parol != parol:
#     print("parol kata")
# else:
#     print("login kata, parol kata")


# marks = [5,4,3,5,4]
# total = 0
# for mark in marks:
#     total += mark
#     print("summa:", total)
#     print("ortocho:", total / len(marks))


#     for i in range(2, 31, 2):
#         print(i)


#         for i in range (3,55,3):
#             print(i)


# n = 10
# жыйынтык = n *



n = int(input("сан киргиз: "))

i = 1
while i <= n:
    print(i)
    i += 1


n = int(input("сан киргиз: "))

for i in range(1, n + 1):
    print(i)



