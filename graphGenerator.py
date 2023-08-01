#Aluna: Isabella Vecchi Ferreira
#Matrícula: 11621ECP002

import numpy as np
import matplotlib.pyplot as plt

QTD_DE_ALUNAS = 4000

def plotaGraficoColuna(percentuals, qtdAlunas, labels, title, xLabel, yLabel, yLim):
    colors = ['#f6c5cf', '#d9ead3', '#f9eb9c', '#c5d4ff']

    percentuals = np.array(percentuals)
    qtdPercentualAlunas = percentuals*(qtdAlunas/100)
    plt.bar(labels, qtdPercentualAlunas, color=colors)

    for index, value in enumerate(percentuals):
        plt.text(index, value, f'{value}%', ha='center', va='bottom')

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.ylim(0, yLim)
    plt.show()

### 1 - Renda Mensal per Capta de casa antes do curso
percentuals = np.array([12, 44, 8, 36])
colors = ['#f6c5cf', '#d9ead3', '#f9eb9c', '#c5d4ff']

# gráfico de pizza
labels = ['Até 1 salário', 'De 1 a 3 salários', 'De 3 a 5 salários', 'Acima de 5 salários']
explode = [0, 0, 0, 0]
start_angle = 180
plt.pie(percentuals, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%.1f%%', startangle=start_angle, counterclock=False)
plt.title('Antes do Curso')
plt.show()

# gráfico de colunas
labels = ['x < 1', '1 < x < 3', '3 < x < 5', 'x > 5']
title = 'Antes do Curso'
xLabel = 'Renda Per Capita de Casa'
yLabel = 'Qtd. de alunas da Reprograma'
yLim = 1800

plotaGraficoColuna(percentuals, QTD_DE_ALUNAS, labels, title, xLabel, yLabel, yLim)



### 2 - Renda Mensal per Capta de casa depois do curso
percentuals = np.array([8, 22, 38, 32])
colors = ['#f6c5cf', '#d9ead3', '#f9eb9c', '#c5d4ff']


# gráfico de pizza
labels = ['Até 1 salário', 'De 1 a 3 salários', 'De 3 a 5 salários', 'Acima de 5 salários']
explode = [0, 0, 0, 0]
start_angle = 180
plt.pie(percentuals, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%.1f%%', startangle=start_angle, counterclock=False)
plt.title('Atual')
plt.show()

# gráfico de colunas
labels = ['x < 1', '1 < x < 3', '3 < x < 5', 'x > 5']
title = 'Atualmente'
xLabel = 'Renda Per Capita de Casa'
yLabel = 'Qtd. de alunas da Reprograma'
yLim = 1800

plotaGraficoColuna(percentuals, QTD_DE_ALUNAS, labels, title, xLabel, yLabel, yLim)


### 3a
percentuals = np.array([66, 34])
labels = ['Sim', 'Não']
title = 'Antes do Curso'
xLabel = 'Estava Empregada'
yLabel = 'Qtd. de alunas da Reprograma'
yLim = 3500

plotaGraficoColuna(percentuals, QTD_DE_ALUNAS, labels, title, xLabel, yLabel, yLim)


# ### 3b
percentuals = np.array([78, 22])
labels = ['Sim', 'Não']
title = 'Atualmente'
xLabel = 'Está Empregada Atualmente'
yLabel = 'Qtd. de alunas da Reprograma'
yLim = 3500

plotaGraficoColuna(percentuals, QTD_DE_ALUNAS, labels, title, xLabel, yLabel, yLim)



### 4a
percentuals = np.array([12, 54, 34])
colors = ['#f6c5cf', '#d9ead3', '#f9eb9c']
title = 'Antes do curso, estava empregada na área de TI'


# gráfico de pizza
labels = ['Sim', 'Não', 'Não estava empregada']
explode = [0.1, 0, 0]
start_angle = 90
plt.pie(percentuals, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%.1f%%', startangle=start_angle, counterclock=False)
plt.title(title)
plt.show()

# gráfico de colunas
percentuals = np.array([12, 88])
labels = ['Sim', 'Não']
title = 'Antes do Curso'
xLabel = 'Estava Empregada na Área de TI'
yLabel = 'Qtd. de alunas da Reprograma'
yLim = 3700

plotaGraficoColuna(percentuals, QTD_DE_ALUNAS, labels, title, xLabel, yLabel, yLim)



### 4b
labels = ['Sim', 'Não']
percentuals = np.array([72, 28])

# gráfico de pizza
explode = [0.1, 0]
start_angle = 90
plt.pie(percentuals, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%.1f%%', startangle=start_angle, counterclock=False)
plt.title('Atualmente está empregada na área de TI')
plt.show()

# gráfico de colunas
title = 'Atualmente'
xLabel = 'Está Empregada na Área de TI'
yLabel = 'Qtd. de alunas da Reprograma'
yLim = 3700

plotaGraficoColuna(percentuals, QTD_DE_ALUNAS, labels, title, xLabel, yLabel, yLim)

### 7a - renda suficiente para garantir a própria subsistência
labels = ['Sim', 'Não']

percentuals = np.array([56, 44])
title = 'Antes do Curso'
xLabel = 'Renda Suficiente'
yLabel = 'Qtd. de alunas da Reprograma'
yLim = 2700

plotaGraficoColuna(percentuals, QTD_DE_ALUNAS, labels, title, xLabel, yLabel, yLim)


### 7b - renda suficiente para garantir a própria subsistência
percentuals = np.array([63, 37])
title = 'Atualmente'
xLabel = 'Renda Suficiente'
yLabel = 'Qtd. de alunas da Reprograma'
yLim = 2700

plotaGraficoColuna(percentuals, QTD_DE_ALUNAS, labels, title, xLabel, yLabel, yLim)