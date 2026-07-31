



def leia_int(num):
    return executar(int,num)
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
        valor = input(num).strip().upper()
        if not valor:
            print('Não pode deixar vazio!')
            return
        return funcao(valor)
    except ValueError:
        print('o valor que o usuário digitou é inválido.')



def criar_indice():
    nome = leia_string('Fileira: ')
    if not nome:
        return
    numero = leia_int('Assento: ')
    if numero <=0 or numero > 10:
        print('ERRO: o indíce é invalido.')
        return
    indice_fileira = ord(nome) - ord('A')
    indice_assento = numero -1
    return indice_fileira,indice_assento

def fazer_reserva(sala):
    resultado = criar_indice()
    if resultado:
        indice_fileira,indice_assento = resultado
    if sala[indice_fileira][indice_assento] == 0:
        sala[indice_fileira][indice_assento] =1
        print('Reservado com sucesso!')
    else:
        print('Não é possivel fazer a reserva')

def cancelar_reserva(sala):
    resultado = criar_indice()
    if resultado:
        indice_fileira,indice_assento = resultado
    if sala[indice_fileira][indice_assento] == 1:
            sala[indice_fileira][indice_assento] =0
            print('Reserva cancelada com sucesso!')

    else:
        print('não é possivel cancelar essa reserva.')
    
  
def leia_int(num):
    return executar(int,num)
def leia_string(msg):
    return executar(str,msg)


def main():
    sala = criar_sala()
    while True:
        opc = leia_int('Digite um número: ')
        if opc ==1:
            fazer_reserva(sala)
        elif opc == 2:
            cancelar_reserva(sala)
        elif opc == 3:
            mostrar_sala(sala)
             
        
main()






