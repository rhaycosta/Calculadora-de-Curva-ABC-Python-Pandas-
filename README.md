# 📦 ABC Curve Analysis Calculator

Um script Python focado em Logística e Supply Chain para automatizar a classificação de estoque baseada na Curva ABC (Princípio de Pareto).

## 🎯 Objetivo
Identificar quais produtos geram maior receita e impacto financeiro para a empresa, permitindo decisões estratégicas de compras e gestão de armazém.

- **Classe A:** Itens de alto valor (representam ~80% do faturamento).
- **Classe B:** Itens de valor intermediário (~15% do faturamento).
- **Classe C:** Itens de baixo valor (representam ~5% do faturamento).

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Pandas** (Manipulação e análise de dados)
- **OpenPyXL/XlsxWriter** (Leitura e escrita de arquivos Excel)

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/abc-curve-logistics.git](https://github.com/SEU-USUARIO/abc-curve-logistics.git)
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Coloque sua planilha na pasta `data/` com o nome `produtos.xlsx` (ou ajuste o script).
4. Execute o script:
   ```bash
   python src/main.py
   ```

## 📊 Estrutura de Entrada (Excel)
O script espera um arquivo `.xlsx` com as seguintes colunas:
- `Produto` (Nome ou SKU)
- `Preco_Unitario` (Valor unitário)
- `Quantidade_Vendida` (Giro do produto)

## 📈 Resultados
O script gera um novo arquivo Excel contendo a classificação (A, B ou C) e a porcentagem acumulada de participação de cada item.

