from sistema import menu
from dados import personagem_ID, osPrimeirosNove, porNome


while True:
    resposta=menu(['Pesquisar pelo ID do personagem','Os primeiros nove','Pelo nome','Sair'])
    if resposta == 1:
        idp = int(input("Digite o Id do personagem: "))
        genshin_impact = personagem_ID(idp)
        print(genshin_impact)

    if resposta == 2:
        genshin_impact1 = osPrimeirosNove()
        print(genshin_impact1)
    
    if resposta == 3:
        nome = str(input("Digite o nome do personagem primeira letra maiuscula: "))
        genshin_impact2 = porNome(nome)
        print(genshin_impact2)
    if resposta == 4:
        break
 


