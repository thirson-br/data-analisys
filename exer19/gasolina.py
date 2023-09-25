# código de geração do gráfico 
import pandas as pd 
import seaborn as sns

# Lendo gasolina.csv
gasolina_df = pd.read_csv("gasolina.csv")

# Definindo tamanho do gráfico
altura  = 20 / 2.54
largura = 20 / 2.54

# Gerando o gráfico
with sns.axes_style('whitegrid'):

  grafico = sns.relplot(data=gasolina_df, x="dia", y="venda", kind="line")
  #grafico.set(title='Preço médio da gasolina SP nos 10 primeiros dias de Jul/21', xlabel='Dia', ylabel='Preço');
  grafico.ax.set_title("Preço médio da gasolina SP nos 10 primeiros dias de Jul/21", fontsize=12, fontweight="bold");
  grafico.set_xlabels("Dia", fontsize=10);
  grafico.set_ylabels("Preços", fontsize=10);
  grafico.fig.set_size_inches(w=largura, h=altura)
  grafico.fig.savefig(fname="exer19/gasolina.png", bbox_inches="tight")
