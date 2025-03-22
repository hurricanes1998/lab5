otv = ""
while True:
    s = input("Введите слово или 'Stop' для завершения предложения: ")
    if s.lower() == "Stop" or s.lower() == "stop":
        break
    otv += s + " "
print("Результат:", otv.strip())