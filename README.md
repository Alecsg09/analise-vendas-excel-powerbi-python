# Análise de Dados de Vendas com Excel, Power BI e Python

Este projeto faz uma análise avançada de dados de vendas, utilizando:
- **Excel** para preparação dos dados.
- **Power BI** para visualização e criação de métricas com DAX.
- **Python** para gerar dados fictícios.

## Estrutura do Projeto
- **Dados/dados_vendas_ampliado.xlsx**: Dados brutos de vendas.
- **powerbi/analise_vendas_ampliado.pbix**: Dashboard interativo no Power BI.
- **scripts/gerador.py**: Script Python para gerar dados fictícios.

## Como Usar
1. **Gerar Dados**:
   - Execute o script `gerador.py` para gerar dados fictícios.
   - Os dados serão salvos em `Dados/dados_vendas_ampliado.xlsx`.

2. **Analisar no Power BI**:
   - Abra o arquivo `analise_vendas_ampliado.pbix` no Power BI.
   - Conecte-o ao arquivo `dados_vendas_ampliado.xlsx`.
     ![Texto alternativo](https://github.com/Alecsg09/analise-vendas-excel-powerbi-python/blob/main/images/analise.jpg)


3. **Explorar o Dashboard**:
   - Use as visualizações interativas para analisar as vendas por produto, região e vendedor.

## Requisitos
- Python 3.x (com bibliotecas `pandas` e `faker` instaladas).
- Power BI Desktop.
- Excel (opcional).

## Instalação das Bibliotecas Python
Para executar o script, instale as bibliotecas necessárias:
```bash
pip install pandas faker

Autor
Alecsander Gomes
