st = "Я зараз вивчаю Python"
st1 = st + chr(128522)
st2 = st1.encode('utf-8')
st3 = st2.decode()
print(st1)
print(st2)
print(st3)

