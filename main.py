def criar_sala():
    sala = []
    for c in range(8):
        lista = []
        for i in range(10):
            lista.append(0)
        sala.append(lista)
    return sala

sala = criar_sala()
print(sala)


