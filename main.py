
def criar_sala():
    sala = []
    for fileiras in range(8):
        fileira = []
        for assento in range(10):
            fileira.append(0)
        sala.append(fileira)
    return sala

def mostrar_sala(sala):
    letras = ['A','B','C','D','E','F','G','H']
    sala_visual = []
    for fileira in sala:
        fileira_visual = []
        for assento in fileira:
            if assento == 0:
                fileira_visual.append('O')
            elif assento == 1:
                fileira_visual.append('X')

        sala_visual.append(fileira_visual)
    for pos,valor in enumerate(sala_visual):
        print(letras[pos],' '.join(valor))


def executar(funcao,num):
    try:
        valor = input(num).strip()
        if not valor:
            return
        return funcao(valor)
    except ValueError:
        print('o valor que o usuário digitou é inválido.')

def leia_int(num):
    return executar(int,num)


def main():
    sala = criar_sala()
    while True:
        opc = leia_int('Digite um número: ')
        if opc ==1:
            mostrar_sala(sala)

main()






