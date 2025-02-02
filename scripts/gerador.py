import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Configurações iniciais
fake = Faker('pt_BR')  # Para dados em português
random.seed(42)  # Para garantir que os dados sejam os mesmos toda vez que rodar o script

# Listas de opções para categorias, produtos e regiões
categorias = ['Eletrônicos', 'Móveis', 'Roupas', 'Acessórios']
produtos_por_categoria = {
    'Eletrônicos': ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch'],
    'Móveis': ['Sofá', 'Cadeira', 'Mesa', 'Estante'],
    'Roupas': ['Camiseta', 'Calça', 'Vestido', 'Jaqueta'],
    'Acessórios': ['Bolsa', 'Óculos', 'Relógio', 'Cinto']
}
regioes = ['Sul', 'Norte', 'Sudeste', 'Nordeste', 'Centro-Oeste']

# Função para gerar dados fictícios
def gerar_dados_vendas(num_linhas=100):
    dados = []
    for _ in range(num_linhas):
        categoria = random.choice(categorias)
        produto = random.choice(produtos_por_categoria[categoria])
        quantidade = random.randint(1, 20)
        preco_unitario = round(random.uniform(100, 5000), 2)
        custo_unitario = round(preco_unitario * random.uniform(0.5, 0.9), 2)
        regiao = random.choice(regioes)
        vendedor = fake.name()
        data = fake.date_between(start_date='-1y', end_date='today')  # Vendas nos últimos 12 meses

        # Adiciona os dados à lista
        dados.append([
            data,
            produto,
            categoria,
            quantidade,
            preco_unitario,
            regiao,
            vendedor,
            custo_unitario
        ])

    # Cria o DataFrame
    colunas = [
        'Data', 'Produto', 'Categoria', 'Quantidade', 'Preço Unitário',
        'Região', 'Vendedor', 'Custo Unitário'
    ]
    df = pd.DataFrame(dados, columns=colunas)

    # Calcula o Total de Vendas e o Custo Total
    df['Total de Vendas'] = df['Quantidade'] * df['Preço Unitário']
    df['Custo Total'] = df['Quantidade'] * df['Custo Unitário']
    df['Lucro'] = df['Total de Vendas'] - df['Custo Total']

    return df

# Gerar 100 linhas de dados fictícios
dados_vendas = gerar_dados_vendas(num_linhas=100)

# Salvar os dados em um arquivo Excel
dados_vendas.to_excel('dados_vendas_ampliado.xlsx', index=False)

print("Planilha gerada e salva como 'dados_vendas_ampliado.xlsx'!")