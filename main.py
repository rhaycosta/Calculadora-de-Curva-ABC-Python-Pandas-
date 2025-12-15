import pandas as pd

def calcular_curva_abc(input_file, output_file):
    # 1. Leitura do arquivo Excel
    try:
        df = pd.read_excel(input_file)
        print("✅ Arquivo lido com sucesso!")
    except FileNotFoundError:
        print("❌ Arquivo não encontrado. Verifique o caminho.")
        return

    # 2. Verificar colunas básicas
    colunas_necessarias = ['Produto', 'Preco_Unitario', 'Quantidade_Vendida']
    if not all(col in df.columns for col in colunas_necessarias):
        print(f"❌ O arquivo precisa ter as colunas: {colunas_necessarias}")
        return

    # 3. Cálculo do Valor Total Movimentado (Faturamento por item)
    df['Valor_Total'] = df['Preco_Unitario'] * df['Quantidade_Vendida']

    # 4. Ordenação (Do maior valor para o menor - fundamental para Pareto)
    df = df.sort_values(by='Valor_Total', ascending=False)

    # 5. Cálculo das Porcentagens Acumuladas
    valor_total_estoque = df['Valor_Total'].sum()
    
    # ALTERAÇÃO 1: Removemos o "* 100" para trabalhar com decimais (0.80 em vez de 80)
    # Isso permite que o Excel formate como porcentagem corretamente depois.
    df['%_do_Total'] = (df['Valor_Total'] / valor_total_estoque)
    df['%_Acumulada'] = df['%_do_Total'].cumsum()

    # 6. Classificação ABC (Regra clássica de Pareto)
    # ALTERAÇÃO 2: Ajustamos a lógica para usar decimais (0.80 e 0.95)
    def definir_classe(percentual_acumulado):
        if percentual_acumulado <= 0.80:
            return 'A'
        elif percentual_acumulado <= 0.95:
            return 'B'
        else:
            return 'C'

    df['Curva_ABC'] = df['%_Acumulada'].apply(definir_classe)

    # 7. Formatação e Exportação
    colunas_finais = ['Produto', 'Quantidade_Vendida', 'Valor_Total', '%_Acumulada', 'Curva_ABC']
    
    print("💾 Salvando arquivo processado com formatação...")
    
    # ALTERAÇÃO 3: Bloco de formatação avançada com XlsxWriter
    # Criamos um "escritor" para poder mexer nas colunas
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    
    # Salvamos os dados
    df[colunas_finais].to_excel(writer, index=False, sheet_name='Analise_ABC')
    
    # Pegamos o "livro" (workbook) e a "planilha" (worksheet) para editar
    workbook  = writer.book
    worksheet = writer.sheets['Analise_ABC']
    
    # Criamos os estilos
    formato_moeda = workbook.add_format({'num_format': 'R$ #,##0.00'})
    formato_porcentagem = workbook.add_format({'num_format': '0.00%'})
    
    # Aplicamos nas colunas certas (A=0, B=1, C=2, D=3...)
    worksheet.set_column('A:A', 20)                      # Coluna A (Produto) mais larga
    worksheet.set_column('C:C', 18, formato_moeda)       # Coluna C (Valor Total) com R$
    worksheet.set_column('D:D', 15, formato_porcentagem) # Coluna D (% Acumulada) com %
    
    # Salva o arquivo final
    writer.close()
    
    # Resumo para mostrar no console
    resumo = df['Curva_ABC'].value_counts().sort_index()
    print("\n--- Resumo da Classificação ---")
    print(resumo)
    print(f"\n✅ Análise concluída! Arquivo salvo em: {output_file}")

if __name__ == "__main__":
    # Caminhos dos arquivos (ajuste conforme necessário)
    arquivo_entrada = 'data/produtos.xlsx'
    arquivo_saida = 'data/relatorio_abc.xlsx'
    
    # Executa a função
    calcular_curva_abc(arquivo_entrada, arquivo_saida)