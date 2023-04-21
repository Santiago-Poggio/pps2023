f = open ('mihobby.md', 'r')
hobby = f.read()
respuestas= []
diccionario = {}
for i in range(2,7):
    respuestas.append(hobby.splitlines()[i])
for i in range(5):
    respuestas[i]= respuestas[i].replace("*","")
    diccionario[respuestas[i].split(":")[0]] = respuestas[i].split(":")[1] 
for i in diccionario:
    print(i)
for i in diccionario:
    print(diccionario[i])