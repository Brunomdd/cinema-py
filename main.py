
def leia_int(num):
    return executar(int,num)

def linha(tam=32):
    return '-'*tam

def cabecalho(txt):
    print(linha())
    print(f'{txt}'.center(32))
    print(linha())

def criar_sala():
    sala = []
    for fileiras in range(8):
        fileira = []
        for assentos in range(10):
            fileira.append(0)
        sala.append(fileira)
    return sala

def mostrar_sala(sala):
    cabecalho('MAPA DO SISTEMA DE CINEMA')
    letras = ['A','B','C','D','E','F','G','H']
    sala_visual = []
    for fileira in sala:
        fileira_visual = []
        for assento in fileira:
            if assento == 0:
                fileira_visual.append('O')
            else: 
                fileira_visual.append('X')
           
        sala_visual.append(fileira_visual)
    for pos,valor in enumerate(sala_visual):
        print(letras[pos],' '.join(valor))


def executar(funcao,num):
    try:
        valor = input(num).strip()
        if not valor:
            print('Não pode deixar vazio!')
            return
        return funcao(valor)
    except ValueError:
        print('o valor que o usuário digitou é inválido.')
        
def criar_indice():
    nome = input('Fileira: ').upper()
    if not nome:
        return
    numero = leia_int('Assento:')
    if numero is None:
        return
    if numero <=0 or numero > 10:
        print('ERRO: número fora de intervalo.')
        return
    
    indice_fileira = ord(nome) - ord('A')
    if indice_fileira >7:
        print('ERRO: número totalmente fora de intervalo!')
        return
    indice_assento = numero -1
    return indice_fileira,indice_assento

def fazer_reserva(sala):
    cabecalho('FAZER RESERVA')
    resultado = criar_indice()
    if resultado:
        indice_fileira,indice_assento = resultado
        if sala[indice_fileira][indice_assento] == 0:
            sala[indice_fileira][indice_assento] =1
            print('Reservado com sucesso!')
        else:
            print('Não é possivel fazer a reserva')
            return

def cancelar_reserva(sala):
    cabecalho('CANCELAR RESERVA')
    resultado = criar_indice()
    if resultado:
        indice_fileira,indice_assento = resultado
        if sala[indice_fileira][indice_assento] == 1:
            sala[indice_fileira][indice_assento] =0
            print('Reserva cancelada com sucesso!')
        else:
            print('não é possivel cancelar essa reserva.')
            return 
        
def mostrar_estatisticas(sala):
    dados = {'total':0,
             'livres':0,
             'ocupados':0,}
    
    for fileira in sala:
        for assento in fileira:
            dados['total'] +=1
            if assento == 0:
                dados['livres'] +=1
            elif assento == 1:
                dados['ocupados'] +=1
    if dados['total'] >0:
        percentual = (dados['ocupados']/dados['total'])*100
        print(f"Percentual de ocupação: {percentual:.2f}%")
        print(f"Total: {dados['total']}")
        print(f"Lugares livres {dados['livres']}")
        print(f"lugares ocupados: {dados['ocupados']}")


def main():
    cabecalho('cinema py')
    sala = criar_sala()
    while True:
        opc = leia_int('digite uma opção: ')
        if opc ==1:
            fazer_reserva(sala)
        elif opc == 2:
            cancelar_reserva(sala)
        elif opc == 3:
            mostrar_sala(sala)
        elif opc == 4:
            mostrar_estatisticas(sala)
        elif opc == 5:
            cabecalho('Saindo do sistema . . ..')
            break
        else:
            print('Opção inválida.')


main()






