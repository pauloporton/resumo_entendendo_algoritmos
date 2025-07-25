# Dividir para conquistar

*algoritmos DC são recursivos*

- Forma de pensar o problema
- Divide em dois problemas menores

    - 1º : Descubra o caso-base, que deve ser o mais simples possível
    - 2º : Descubra como reduzir o seu problema para que ele se torne o caso-base
    *Se envolver array, muitas vezes o caso-base será um array vazio ou com 1 elemento*

# Quicksort

- 1º : Escolher um pivô (valor do array)
- 2º : Dividir o array em dois sub-arrays (valores menores e maiores que o pivô)
- 3º : Executar o quicksort recursivamente em abos os sub-arrays

*Sempre escolher item aleatório como pivô, pois a execução média é O(n * log n)*