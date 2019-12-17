# genetic-algotithm

# Versão 1

O algoritmo genético é um algoritmo que permite que com alterações binárias (ou bit a bit) sejam executadas em cadeias de bits (números binários) para chegar num valor que minimeze ou maximize determinada função.
<br>
Para chegar ao objetivo de minimizar ou maximizar uma dada função, o algortimo genético utiliza de rotinas como mutações e crossovers para ir criando novos números que tem o objetivo de ir convergindo para o objetivo desejado.

## Inicialização do algoritmo, criação da população de inidivíduos e escolha do melhor indivíduo
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/code1.png?raw=true)

## Inicialização do loop para crossovers, calculo do fitness de cada indivíduo e escolha do indivíduo do melhor fitness
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/code2.png?raw=true)

## Inicio do crossover
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/code3.png?raw=true)

## Escolha de dois pais, mutação e crossover emtre eles
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/code4.png?raw=true)

## Escolha do melhor pai após o crossover, e população atualizada
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/code5.png?raw=true)

## Cópia das melhores execuções, geração e print da média
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/code6.png?raw=true)

## Constantes usadas
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/code7.png?raw=true)

## Classe que representa o indivíduo
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/code8.png?raw=true)

## Resultados obtidos

### 10-10
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/10-10.PNG?raw=true)

### 20-10
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/20-10.PNG?raw=true)

# Versão 2

## Alterações no Crossover e Mutação

Utilizamos um crossover aritmético e uma mutação de limite

### Mudanças no código
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/code9.png?raw=true)

### Comparação entre a Versão 1 e a Versão 2

Valor médio dos resultados:
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/Comparativo%20m%C3%A9dia%20vers%C3%B5es.PNG?raw=true)

Gráfico de evolução do Gbest
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/Evolu%C3%A7%C3%A3o%20do%20Gbest%20ao%20longo%20das%20execu%C3%A7%C3%B5es%20v1.PNG?raw=true)
![enter image description here](https://github.com/edsonboldrini/genetic-algotithm/blob/master/Evolu%C3%A7%C3%A3o%20do%20Gbest%20ao%20longo%20das%20execu%C3%A7%C3%B5es%20v2.PNG?raw=true)
