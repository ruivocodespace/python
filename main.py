# VARIÁVEIS
largura_endereco = 28
altura_endereco = 40
comprimento_endereco = 50


# FUNÇÃO PARA VALIDAR MEDIDA
def validar_medida(nome_medida):
    valido = 0

    while valido == 0:
        try:
            medida = float(input(f"Digite a {nome_medida} do produto:"))

            if medida <= 0:
                print("Erro, medida menor ou igual a zero")
                valido = 0
            else:
                valido = 1

        except ValueError:
            valido = 0
            print("Entrada inválida, insira apenas números")
    return medida


# FUNÇÃO VERIFICAR COMPATIBILIDADE
def verificar_compatibilidade(largura, altura, comprimento):
    
    # UTILIZA IF ELSE PARA CONFIRMAR COMPATIBILIDADE
    if largura <= largura_endereco and altura <= altura_endereco and comprimento <= comprimento_endereco:
        return(True)
    else:  
        return(False)
    


largura_produto = validar_medida("largura")
altura_produto = validar_medida("altura")
comprimento_produto = validar_medida("comprimento")

# CHAMA A FUNÇÃO   
resultado = verificar_compatibilidade(largura_produto, altura_produto, comprimento_produto)
if resultado:
    print("O item cabe no endereço.")
else:
    print("O item não cabe no endereço")