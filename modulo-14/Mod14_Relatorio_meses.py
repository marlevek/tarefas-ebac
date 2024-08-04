import os
import sys 
import pandas as pd
import matplotlib.pyplot as plt


def criar_pastas(meses):
    for mes in meses:
        nome_pasta = f'mes_{mes}'
        if not os.path.exists(nome_pasta):
            os.makedirs(nome_pasta)


def gerar_graficos(meses):
    for mes in meses:
        nome_arquivo = f'SINASC_RO_2019_{mes.upper()}.csv'
        nome_pasta = f'mes_{mes}'
        
        dados = pd.read_csv(nome_arquivo)
        
        plt.figure(figsize=(8, 6))
        plt.plot(dados['DTNASC'], dados['APGAR5'])
        plt.title(f'Dados do mês {mes}')
        plt.xlabel('Data Nascimento')
        plt.ylabel('APAGAR 5')
        plt.grid(True)
        
        nome_grafico = f'grafico_{mes}.png'
        plt.savefig(os.path.join(nome_pasta, nome_grafico))
        plt.close()
        
if len(sys.argv) < 2:
    print('Por favor forneça a lista de meses como argumento')
    sys.exit(1)
    
meses_argumento = sys.argv[1:]

criar_pastas(meses_argumento)
gerar_graficos(meses_argumento)

print(f'Pastas e gráficos gerados com sucesso para os meses: {meses_argumento}')

