produtos = []

#função responsável por carregar os dados do arquivo "estoque.csv" para o estoque atual
def carregar_estoque(produtos):
    try:
        with open('estoque.csv', 'r', encoding='utf-8') as arquivo:
            text = arquivo.read().split('\n')
            for linha in text:
                partes = linha.split(',')
                if len(partes) == 3:
                    produto, quantidade, preco = partes
                    item = {'produto': produto, 'quantidade': int(quantidade), 'preço': float(preco)}
                    produtos.append(item)
    except Exception as e:
        print(e)

#função para adicionar produtos no estoque do mercado
def adicionar_no_estoque(produtos):
    nome = input('\ndigite o nome do produto: ')
    quantos = int(input('digite a quantidade do produto: '))
    valor = float(input('digite o preço: '))
    produto = {
        'produto': nome,
        'quantidade': quantos,
        'preço': valor
    }
    produtos.append(produto)
    print(f"\nProduto '{nome}' adicionado ao estoque.")
    
#função responsável pela formatação e visualização do estoque do mercado
def estoque(produtos, titulo = "_-_-ESTOQUE-_-_"):
    if not produtos:
        print("\n\nEstoque vazio!\n")
        return
    
    print(f"{'_' * 30}{titulo:>12}{'_' * 33}\n")
    print(f'|                      {"\tPRODUTO":<27} | {"QUANTIDADE":<10} | {"PREÇO (R$)":<10}')
    print('-' * 78)
    
    for items in produtos:
        print(f"| {items['produto']:<48} | {items['quantidade']:<10} | {items['preço']:<10}")

#função responsável por retirar produtos do estoque do mercado    
def tirar_do_estoque(produtos):
    
    estoque(produtos)
    
    nome = input('\n\ndigite o produto que deseja retirar: ')
    nome = nome.lower()
    # cria um indice para percorrer a lista de produtos 
    for indice in range(len(produtos)):
        if produtos[indice]['produto'] == nome:
            quantos = int(input('Digite a quantidade: '))
            
            #verifica se a quantidade solicitada é menor ou igual a quantidade disponível no estoque
            if produtos[indice]['quantidade'] >= quantos:
                produtos[indice]['quantidade'] -= quantos    
                print(f'\n- {quantos} {produtos[indice]['produto']}(s) retirado(s) do estoque.')

                # verifica se a quantidade do produto é igual a zero, se sim, remove o produto da lista
                if produtos[indice]['quantidade'] == 0:
                    produtos.pop(indice)
                    
                return
        # caso a quantidade não esteja no estoque, ou produto não exista 
            else:
                print('\nquantidade de produtos indisponível')
                return
    print('\nProduto não encontrado ')           

#função responsável por salvar os produtos no estoque do mercado
def salvar_estoque(produtos):
    with open("estoque.csv", 'w', encoding='utf-8') as arquivo:
        arquivo.write("produto,quantidade,preco\n")  
        for item in produtos:
            item_info = f"{item['produto']},{item['quantidade']},{item['preço']}\n"
            arquivo.write(item_info)
    
carregar_estoque(produtos)
        
# Menu do sistema        
while(True):
    print('\n')
    print('MENU')
    print('1 -Registrar produto')
    print('2- Listagem do estoque')
    print('3 - Retirar do estoque')
    print('X - Sair')
    opcao = input('\ndigite a opção: ')
    
    
    # verifica oque o usuário escolheu no menu e executa a função correspondente
    if opcao == '1':
        adicionar_no_estoque(produtos)
    elif opcao == '2':
        estoque(produtos, titulo = "_-_-ESTOQUE-_-_")
    elif opcao == '3':
        tirar_do_estoque(produtos)    
    elif opcao.lower() == 'x':
        
        salvar_estoque(produtos)
        
        if not produtos:
            break
        #mostra o estoque no final do progama
        else:
            estoque(produtos, titulo="_-_-ESTOQUE-_-_")
            print('')
            break
    else:
        print('\nOpção inválida!!')
