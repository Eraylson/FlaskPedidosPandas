import pandas as pd
diretorio_tabela = r'C:\Users\pesqu\PycharmProjects\Pedidos\dados\\'


def salvar_tabela(nome_da_tabela, tabela):
    tabela.to_csv(diretorio_tabela + nome_da_tabela + '.csv', index=False)
    print('tabela salva!')


def criar_tabela(nome_da_tabela, colunas):
    df = pd.DataFrame(columns = colunas)
    df.to_csv(nome_da_tabela+'.csv', index=False)

def abrir_tabela(nome_da_tabela):
    return pd.read_csv(diretorio_tabela+nome_da_tabela+'.csv')

def adicionar_pedido(cliente, endereco, pedido, nome_tabela):
    tabela = abrir_tabela(nome_tabela)
    if len(tabela) == 0:
        #tabela vazia
        ultimo_id = 0
    else:
        #pega o último id
        ultimo_id = tabela['id'].values[-1]

    id_pedido = ultimo_id + 1
    df = pd.DataFrame([id_pedido, cliente, endereco, pedido])
    df = df.transpose()
    df.columns = ['id', 'nome', 'endereco', 'pedido']
    tabela = tabela.append(df)
    tabela.to_csv(diretorio_tabela+nome_tabela+'.csv', index=False)

def buscar_pedido_id(id, tabela):

    resultado = tabela.query(f'id == {id}')
    # !!! tratar quando o pedido não for encontrado
    return resultado

def editar_pedido(id, tabela, cliente, endereco, desc_pedido):

    pedido = buscar_pedido_id(id, tabela)
    idx = pedido.index
    tabela.loc[idx,'nome'] = cliente
    tabela.loc[idx, 'endereco'] = endereco
    tabela.loc[idx, 'pedido'] = desc_pedido
    return tabela

def deletar_pedido(id, tabela):
    pedido = buscar_pedido_id(id, tabela)
    idx = pedido.index
    return tabela.drop(idx)


if __name__ == '__main__':
    nome_tabela = 'cliente'
    #criar_tabela(nome_tabela, ['id', 'nome', 'endereco', 'pedido'])
    adicionar_pedido('teste2', 'teste2', 'pedido2', nome_tabela)
    tabela = abrir_tabela(nome_tabela)
    print(tabela)