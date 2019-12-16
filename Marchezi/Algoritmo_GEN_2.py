import random
import math

###### Autores: Gabriel Marchezi e Gabriel Viggiano ######

#Versao 2
def InicializarPopulação (numPop):
	listaPop = []
	individuo = 0
	while (numPop > 0):
		individuo = round(random.uniform(-20,20),3)
		listaPop.append(individuo)
		numPop = numPop - 1
	return listaPop

#seleciona dos pais através do método torneio
def Torneio(populacao):
	lista_torneio = []
	for i in range(len(populacao)):
		pai1 = populacao[random.randint(0,len(populacao)-1)]
		pai2 = populacao[random.randint(0,len(populacao)-1)]
		if Avalia_Individuo(pai1) < Avalia_Individuo(pai2):
			lista_torneio.append(pai1)
		else:
			lista_torneio.append(pai2)
	return lista_torneio

#Versao 2
'''def Crossover(lst_pais, taxa):
	lst_filhos = []
	for i in range(0,len(lst_pais),2):
		if(random.randint(1,100) <= taxa):
			filho1 = lst_pais[i] + 0.5 * (lst_pais[i] - lst_pais[i+1])
			filho2 = lst_pais[i+1] + 0.5 * (lst_pais[i+1] - lst_pais[i])
		else:
			filho1 = lst_pais[i]
			filho2 = lst_pais[i+1]
		lst_filhos.append(filho1)
		lst_filhos.append(filho2)
	return lst_filhos'''
# Crossover Aritmético
def Crossover(lst_pais,taxa):
	lst_filhos = []
	for i in range(0,len(lst_pais),2):
		if(random.randint(1,100) <= taxa):
			b = round(random.uniform(0,1),2)
			filho1 = b * lst_pais[i] + (1 - b) * lst_pais[i+1]
			filho2 = (1 - b) * lst_pais[i] + b * lst_pais[i+1]
		else:
			filho1 = lst_pais[i]
			filho2 = lst_pais[i+1]
		lst_filhos.append(filho1)
		lst_filhos.append(filho2)
	return lst_filhos

# Mutação de limites
def Mutacao (lst_filhos, taxa, ite_atual,iteracoes):
	lst_mutada = []
	for filho in lst_filhos:
		if(random.randint(1,100) <= taxa):
			r1 = round(random.uniform(0,1),2)
			if (r1 > 0.5):
				mutado = 20
			else:
				mutado = -20
		else:
			mutado = filho
		lst_mutada.append(mutado)
	return lst_mutada

#Recebe uma lista de individuos e retorna uma lista com os individuos com melhor e pior aptidão
def Melhor_Pior (lst_ind):
	lista = []
	melhor = lst_ind[0]
	pior = lst_ind[0]
	for individuo in lst_ind:
		if (Avalia_Individuo(individuo) < Avalia_Individuo(melhor)):
			melhor = individuo
		if(Avalia_Individuo(individuo) > Avalia_Individuo(pior)):
			pior = individuo
	lista.append(melhor)
	lista.append(pior)
	return lista



# Converte um número decimal para um número binário de 10 bits
def DecToBin(dec):
	b1n = bin(dec)[2:]
	while (len(b1n) < 10):
		b1n = '0' + b1n
	return b1n

# Convente um número binário para um número decimal
def BinToDec(b1n):
	b1n = '0b' + b1n
	dec = int(b1n,2)
	return dec


# Versao 2
def Avalia_Individuo(individuo):
	x = individuo
	resultado = round(math.cos(x) * x + 2,3)
	return resultado


def Algo_Gen(populacao, iteracoes, taxa_muta, taxa_cross):
	elite = Melhor_Pior(populacao)
	ite_atual = 0
	lst_exe = []
	while(ite_atual < iteracoes):
		populacao = Torneio(populacao)
		populacao = Crossover(populacao,taxa_cross)
		populacao = Mutacao(populacao,taxa_muta,ite_atual,iteracoes)
		elite_it = Melhor_Pior(populacao)
		if (Avalia_Individuo(elite_it[0]) < Avalia_Individuo(elite[0])):
			elite[0] = elite_it[0]
		cont = 0
		for individuo in populacao:
			if (individuo == elite_it[1]):
				del(populacao[cont])
				populacao.append(elite[0])
			cont += 1
		ite_atual +=1
		lst_exe.append(populacao)
	return lst_exe



def main():
	numpop = int(input("Digite a tamanho da população: "))
	iteracoes = int(input("Digite o número de iterações: "))
	taxa_muta = int(input("Digite a taxa de mutação: "))
	taxa_cross = int(input("Digite a taxa de crossover: "))
	execucoes = int(input("Digite o número de execuções:"))
	
	#Executa o Algoritmo Genético N vezes
	exe_atual = 0
	lst_exes = []
	while(exe_atual < execucoes):
		populacao_inic = []
		populacao_inic = InicializarPopulação(numpop)
		resultado = Algo_Gen(populacao_inic, iteracoes, taxa_muta, taxa_cross)
		lst_exes.append(resultado)
		exe_atual += 1

	#Encontra os melhores resultados de todas as iterações em todas as execuções
	lst_melhores_exe = []
	for exe in lst_exes:
		lst_melhores_ite = []
		for ite in exe:
			melhor = 1
			for ind in ite:
				if (Avalia_Individuo(ind) < melhor):
					melhor = Avalia_Individuo(ind)
			lst_melhores_ite.append(melhor)
		lst_melhores_exe.append(lst_melhores_ite)

	#Inicia a lista com as médias dos resultados preenchendo com zeros
	lista_medias = []
	for i in range(0,iteracoes):
		lista_medias.append(0)

	#Calcula a média das iterações das execuções e guarda também a execução com melhor resultado
	lst_melhor_result = [['']]
	melhor = 1
	for exe in lst_melhores_exe:
		pos = 0
		temp = []
		cond = False
		for result in exe:
			if(result < melhor):
				cond = True
				melhor = result
			temp.append(result)
			lista_medias[pos] += result
			pos += 1	
		if(cond == True):
			lst_melhor_result[0] = temp
	print("melhor: " + str(melhor))
	print(lst_melhor_result)
	cont = 0
	for i in lista_medias:
		lista_medias[cont] = lista_medias[cont]/execucoes
		cont += 1
	print("Médias das iterações em "+ str(execucoes) + " execuções: ")
	print(lista_medias)


if __name__ == '__main__':
	main()