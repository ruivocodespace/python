# VARIÁVEIS
largura_endereco = 28
altura_endereco = 40
comprimento_endereco = 50

# FUNÇÃO VERIFICAR COMPATIBILIDADE
def verificar_compatibilidade(largura_endereco, altura_endereco, comprimento_endereco):
    
    # PEDE AO USUÁRIO AS MEDIDAS
    largura_produto = float(input("Digite a largura do produto:"))
    altura_produto = float(input("Digite a altura do produto:"))
    comprimento_produto = float(input("Digite o comprimento do produto:"))
    
    # UTILIZA IF ELSE PARA CONFIRMAR COMPATIBILIDADE
    if largura_produto <= largura_endereco and altura_produto <= altura_endereco and comprimento_produto <= comprimento_endereco:
        return(True)
    else:  
        return(False)

# CHAMA A FUNÇÃO   
resultado = verificar_compatibilidade(largura_endereco, altura_endereco, comprimento_endereco)

if resultado:
    print("O item cabe no endereço.")
else:
    print("O item não cabe no endereço")