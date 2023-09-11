import pickle, json

with open('sample3.pkl', mode='rb') as file: #десералізація файлу
    d = pickle.load(file)

print(d)

with open('sample.json', mode='r') as file1: #десералізація файлу
    d2 = json.load(file1) #загружаемо з фалу

print(type(d))
print(d2)