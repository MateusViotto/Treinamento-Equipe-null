# Python 🐍💻

## Print 💬

### Printar uma variável

<code>print( "{ :.1f}".format( x ))</code>    
Imprime a variável x com 1 casa decimal    

<code>print( f"{ x } ")</code>    

<code>print( x ) </code>    

## Variáveis 🔠

<code>x = 0 </code>  
Declara uma variável x com o valor 0    

<code>int(x) = 0 </code>  
Declara uma variável inteira x com o valor 0    

## Booleanos ⁉

Booleano retorna True ou False.    
<code>print(10 > 9) : True  
print(10 == 9) : False    
print(10 < 9) : False</code>    

<code>print( isinstace ( x , int ))</code>  
Verifica se x é um número inteiro.    
  
## Operadores ➕➗
  
  Adição: &emsp;&emsp;<b>+</b><br>
  Subtração: &emsp;&emsp;<b>-</b><br>
  Multiplicação: &emsp;&emsp;<b>*</b><br>
  Divisão: &emsp;&emsp;<b>/</b><br>
  Módulo: &emsp;&emsp;<b>%</b><br>
  Exponenciação: &emsp;&emsp;<b>**</b><br>
  Resto: &emsp;&emsp;<b>//</b><br><br>
  
  E: &emsp;&emsp;<b>&</b><br>
  Ou: &emsp;&emsp;<b>|</b><br>
  Não: &emsp;&emsp;<b>~</b><br><br>
  
  Igual: &emsp;&emsp;<b>==</b><br>
  Diferente: &emsp;&emsp;<b>!=</b><br>

## Tipos ⌨
  
### Convertendo os tipos:
  
<code>int(2.2) : 2 </code>  
Converte um número float em um inteiro.    

<code>float(2) : 2.0</code>  
Converte um número inteiro em um float.    

<code>str(2) : "2"</code>  
Converte um número em string.    

<code>int(True) : 1 </code>  
Converte um booleano em inteiro.    

<code>bool(1) : True</code>  
Converte um inteiro em booleano.    

## String 📃

### Navegando pela string:

#### Fatiando a string:
  
<code>a[1]</code>  
Consulta a segunda letra da variável "a".    

<code>a[-1]</code>  
Consulta a última letra da variável "a".    

<code>a[0:10]</code>  
Consulta as letras no intervado de 0 a 10 da variável "a".    

<code>a[:10]</code>  
Consulta todas as letras até a 10 da variável "a".    

<code>a[1:]</code>  
Consulta todas as letras até da 1 em diante da variável "a".    

<code>a[-10: -1]</code>  
Consulta as letras no intervado de 10 a 1 da variável "a".    

#### Modificando a string:

<code>a.upper()</code>  
Capitaliza todas as letras da variável.    

<code>a.lower()</code>  
Transforma todas as letras da variável em letras minúsculas.    

<code>a.strip()</code>  
Remove todos os espaços da variável.    

<code>a.replace("H", "J")</code>  
Substitui todas as letras "H" pela letra "J" na variável.    

<code>a.split(",")</code>  
Separa a string em tuplas.    

#### Outros:
  
<code>len(a)</code>  
Consulta o tamanho da variável "a".    

<code>print("free" in txt)</code>  
Retorna True/False caso "free" faça parte da variável txt.    


### Métodos:


**Atenção: Todos os métodos retornam um novo valor, eles não alteram o valor original.**


- <b>capitalize()	</b>&emsp;&emsp;&emsp;  Converts the first character to upper case
- <b>casefold()	    </b>&emsp;&emsp;&emsp;Converts string into lower case
- <b>center()	      </b>&emsp;&emsp;&emsp;Returns a centered string
- <b>count()	        </b>&emsp;&emsp;&emsp;Returns the number of times a specified value occurs in a string
- <b>encode()	      </b>&emsp;&emsp;&emsp;Returns an encoded version of the string
- <b>endswith()	    </b>&emsp;&emsp;&emsp;Returns true if the string ends with the specified value
- <b>expandtabs()	  </b>&emsp;&emsp;&emsp;Sets the tab size of the string
- <b>find()	        </b>&emsp;&emsp;&emsp;Searches the string for a specified value and returns the position of where it was found
- <b>format()	      </b>&emsp;&emsp;&emsp;Formats specified values in a string
- <b>format_map()	  </b>&emsp;&emsp;&emsp;Formats specified values in a string
- <b>index()	        </b>&emsp;&emsp;&emsp;Searches the string for a specified value and returns the position of where it was found
- <b>isalnum()	      </b>&emsp;&emsp;&emsp;Returns True if all characters in the string are alphanumeric
- <b>isalpha()	      </b>&emsp;&emsp;&emsp;Returns True if all characters in the string are in the alphabet
- <b>isascii()	      </b>&emsp;&emsp;&emsp;Returns True if all characters in the string are ascii characters
- <b>isdecimal()	    </b>&emsp;&emsp;&emsp;Returns True if all characters in the string are decimals
- <b>isdigit()	      </b>&emsp;&emsp;&emsp;Returns True if all characters in the string are digits
- <b>isidentifier()	</b>&emsp;&emsp;&emsp;Returns True if the string is an identifier
- <b>islower()	      </b>&emsp;&emsp;&emsp;Returns True if all characters in the string are lower case
- <b>isnumeric()	    </b>&emsp;&emsp;&emsp;Returns True if all characters in the string are numeric
- <b>isprintable() 	</b>&emsp;&emsp;&emsp;Returns True if all characters in the string are printable
- <b>isspace()	      </b>&emsp;&emsp;&emsp;Returns True if all characters in the string are whitespaces
- <b>istitle()	      </b>&emsp;&emsp;&emsp;Returns True if the string follows the rules of a title
- <b>isupper()	      </b>&emsp;&emsp;&emsp;Returns True if all characters in the string are upper case
- <b>join()	        </b>&emsp;&emsp;&emsp;Converts the elements of an iterable into a string
- <b>ljust()	        </b>&emsp;&emsp;&emsp;Returns a left justified version of the string
- <b>lower()	        </b>&emsp;&emsp;&emsp;Converts a string into lower case
- <b>lstrip()	      </b>&emsp;&emsp;&emsp;Returns a left trim version of the string
- <b>maketrans()	    </b>&emsp;&emsp;&emsp;Returns a translation table to be used in translations
- <b>partition()	    </b>&emsp;&emsp;&emsp;Returns a tuple where the string is parted into three parts
- <b>replace()	      </b>&emsp;&emsp;&emsp;Returns a string where a specified value is replaced with a specified value
- <b>rfind()	        </b>&emsp;&emsp;&emsp;Searches the string for a specified value and returns the last position of where it was found
- <b>rindex()	      </b>&emsp;&emsp;&emsp;Searches the string for a specified value and returns the last position of where it was found
- <b>rjust()	        </b>&emsp;&emsp;&emsp;Returns a right justified version of the string
- <b>rpartition()	  </b>&emsp;&emsp;&emsp;Returns a tuple where the string is parted into three parts
- <b>rsplit()	      </b>&emsp;&emsp;&emsp;Splits the string at the specified separator, and returns a list
- <b>rstrip()	      </b>&emsp;&emsp;&emsp;Returns a right trim version of the string
- <b>split()	        </b>&emsp;&emsp;&emsp;Splits the string at the specified separator, and returns a list
- <b>splitlines()	  </b>&emsp;&emsp;&emsp;Splits the string at line breaks and returns a list
- <b>startswith()	  </b>&emsp;&emsp;&emsp;Returns true if the string starts with the specified value
- <b>strip()	        </b>&emsp;&emsp;&emsp;Returns a trimmed version of the string
- <b>swapcase()	    </b>&emsp;&emsp;&emsp;Swaps cases, lower case becomes upper case and vice versa
- <b>title()	        </b>&emsp;&emsp;&emsp;Converts the first character of each word to upper case
- <b>translate()	    </b>&emsp;&emsp;&emsp;Returns a translated string
- <b>upper()	        </b>&emsp;&emsp;&emsp;Converts a string into upper case
- <b>zfill()	        </b>&emsp;&emsp;&emsp;Fills the string with a specified number of 0 values at the beginning

## Listas 📋

<b>Diferente das tuplas as listas são mutáveis. Isso significa que é possível alterá-la, adicionar ou remover itens. <br>
Uma lista pode ser composta por vários tipos (int, float, str, bool)</b>

<code>thislist = [ "item1", "item2", "item3" ]</code>  
Criando uma lista.    

<code>mylist = thislist.copy()</code>  
Copia uma lista.    

### Consultar itens da lista:

<code>print( len( thislist))</code>  
Imprime o tamanho da lista.<br><br>

<code>thislist[ 1 ] <br>
thislist[ -1 ]<br>
thislist[ 2:5 ]<br>
thislist[ :4 ]<br>
thislist[ 2: ]<br>
thislist[-4:-1]
</code>    
Exemplos de consulta de itens da lista.<br><br>

<code>if "apple" in thislist: <br>
&emsp;print("Yes, 'apple' is in the fruits list")</code>   
Consulta se o item existe na lista.<br><br>

### Mudar itens da lista:

<code>thislist[1] = "blackcurrant"</code><br>
Altera o segundo valor da lista.<br><br>

<code>thislist[1:3] = ["blackcurrant", "watermelon"]</code>  
Altera o intervalo de valores da lista.<br><br>

<code>thislist.insert(2, "watermelon")</code>  
Insere um novo item na posição sem substituir pelo valor naquela posição.<br><br>

<code>thislist.append("orange")</code>  
Adiciona um item na lista.<br><br>

<code>thislist.extend(["mango", "pineapple", "papaya"])</code>  
Adiciona mvários itens na lista.<br><br>

<code>thislist.remove("banana")</code>  
Remove um item da lista.<br><br>

<code>thislist.pop(1)</code>  
Remove um item de uma determinada posição da lista.<br><br>

<code>thislist.pop()</code>  
Remove o último item da lista.<br><br>

<code>del thislist[0]</code>  
Remove o primeiro item da lista.<br><br>

<code>del thislist</code>  
Deleta a lista.<br><br>

<code>thislist.clear()</code>  
Limpa a lista.<br><br>

### Loop pela lista:

<code>for x in thislist:</code>  
Percorre todos os itens da lista.<br><br>

<code>newlist = [x for x in fruits if x != "apple"]</code>  
Cria uma lista a partir de outra lista com restrições.<br><br>

<code>newlist = [x if x != "banana" else "orange" for x in fruits]</code>
Cria uma nova lista a partir de outra, adicionando "orange" sempre quando é "banana".<br><br>

### Organizar a lista:

<code>thislist.sort()</code>
Organiza a lista em ordem alfabetica.<br><br>

<code>thislist.sort(reverse = True)</code>  
Organiza a lista em ordem reversa a alfabetica.<br><br>

<code>def myfunc(n):<br>
  return abs(n - 50)<br>
  thislist.sort(key = myfunc)</code>  
Organiza a lista baseado em quão próximo o valor está de 50.<br><br>

<code>thislist.sort(key = str.lower)</code>  
Organiza a lista em ordem alfabética separando as palavras com letras maiúsculas<br><br>

### Juntar duas listas:

<code>lista3 = lista2 + lista1</code>  
Cria uma nova lista baseada na junção de outras duas.<br><br>

### Outros métodos:

<code>count( )</code>  
Retorna o numero de elementos com um determinado valor.<br><br>

<code>index( )</code>  
Retorna o indice em que se encontra um determinado valor.<br><br>

## Tuplas 📁

<b>Diferente das listas as tuplas são imutáveis. Isso significa que não é possível alterá-la.<br>
Uma tupla pode ser composta por vários tipos (int, float, str, bool)</b>
  
<code>thistuple = ( "item1", "item2", "item3" )</code>  
Criando uma tupla.<br><br>

<code>thistuple( 1 ) <br>
thistuple( -1 )<br>
thistuple( 2:5 )<br>
thistuple( :4 )<br>
thistuple( 2: )<br>
thistuple( -4:-1 )</code>  
Exemplos de consulta de itens da tupla.<br><br>

### Juntar duas listas:

<code>tupla3 = tupla2 + tupla1</code>  
Cria uma nova tupla baseada na junção de outras duas.<br><br>
 
### Métodos:

<code>count( )</code>  
Retorna o numero de elementos com um determinado valor.<br><br>

<code>index( )</code>  
Retorna o indice em que se encontra um determinado valor.<br><br>

  
## Sets 📦

<b>Diferente das tuplas e listas os sets não possuem uma ordem. Os sets possuem apenas valores unicos.</b>
  
<code>thisset = {"apple", "banana", "cherry"}</code>  
Criando um set.<br><br>

### Consultar itens de um set:

<code>print( len( thisset))</code>  
Imprime o tamanho do set.<br><br>
 
### Adicionar e remover itens de um set:
  
<code>thisset.add("orange")</code>  
<code>thisset = set()</code>   
Adiciona um item ao set.<br><br>
  
<code>thisset.update(tropical)</code>  
Adiciona os elementos de "tropical" ao set.<br><br>
  
<code>thisset.remove("banana")</code>  
Remove um item do set. <b>Se o item a ser excluído não existir ocorrerá um erro.</b><br><br>
  
<code>thisset.discard("banana")</code>
<br>Remove um item do set. <b>Se o item a ser excluído não existir NÃO ocorrerá um erro.</b><br><br>
  
<code>thisset.pop( )</code>  
Remove um item aleatório do set.<br><br>

<code>thisset.clear( )</code>  
Limpa o set.<br><br>

<code>del thisset</code>  
Exclui um set.<br><br>

### Junções com sets:
  
  ![image](https://user-images.githubusercontent.com/96631827/226457376-b4c137b7-fb4f-4468-8bc4-679b7ed20454.png)
  
<code>set3 = set1.union(set2)</code>  
Une dois sets dentro de outro.<br><br>

<code>x.intersection_update(y)</code>  
Mantém apenas os itens presentes nos dois sets.<br><br>

<code>z = x.intersection(y)</code>  
Retorna apenas os itens presentes nos dois sets.<br><br>

![image](https://user-images.githubusercontent.com/96631827/226458063-131024e6-06c5-4df0-8f5d-37dab8089c81.png)
  
<code>x.symmetric_difference_update(y)</code>  
Mantém apenas os itens presentes que NÃO estão nos dois sets.<br><br>
 
<code>z = x.symmetric_difference(y)</code>
Retorna apenas os itens presentes que NÃO estão nos dois sets.<br><br>
  
![image](https://user-images.githubusercontent.com/96631827/226457464-5b30751b-5c41-4c96-b29a-d0b50f588d39.png)

<code>set( album_set1 ).issuperset( album_set2 )</code>  
Verifica se album_set1 contém todos os itens de album_set2.<br><br>

<code>album_set1.difference( album_set2 )</code>  
Encontra as diferenças em set1 mas não em set2.<br><br>
  
## Dicionário 📕

<b>Dicionários são utilizados para armazenar dados em "keys". Um dicionário é uma coleção mutável que não permite duplicações.</b>  
 
<code>thisdict = {<br>
  "brand": "Ford",<br>
  "model": "Mustang",<br>
  "year": 1964<br>
} </code>  
Declarando um dicionário.<br><br>

<code>thisdict = dict(name = "John", age = 36, country = "Norway")</code>  
Declarando um dicionário utilizando um construtor.<br><br>
 
<code>len(thisdict)</code>  
Retorna o tamanho do dicionário.<br><br>
### Acessar itens do dicionário:
  
<code>thisdict["brand"]</code>  
Consultando um valor no dicionário.<br><br>

<code>x = thisdict.get("model")</code>  
Consultando um valor no dicionário.<br><br>

<code>x = thisdict.keys()</code>  
Retorna uma lista com as "keys".<br><br>
  
<code>x = thisdict.values()</code>  
Retorna uma lista com os valores.<br><br>
  
<code>x = thisdict.items()</code>  
Retorna uma lista com os itens.<br><br>

### Mudar valores em um dicionário:

<code>thisdict["year"] = 2018</code>  
Altera um valor do dicionário.<br><br>

<code>thisdict.update({"year": 2020})</code>  
Altera um valor do dicionário.<br><br>

<code>thisdict["color"] = "red"</code>  
Adiciona um item do dicionário.<br><br>
  
<code>thisdict.update({"color": "red"})</code>  
Adiciona um item do dicionário.<br><br>

<code>thisdict.pop("model")</code>  
Remove um item do dicionário.<br><br>

<code>del thisdict["model"]</code>  
Remove um item do dicionário.<br><br>

<code>thisdict.clear()</code>  
Limpa o dicionário.<br><br>

## IF e ELSE 🔃

### Operadores lógicos:

Igual: &emsp;&emsp;<b>==</b><br>
Diferente: &emsp;&emsp;<b>!=</b><br>
Menor que: &emsp;&emsp;<b><</b><br><br>
Menor ou igual a: &emsp;&emsp;<b><=</b><br><br>
Maior que: &emsp;&emsp;<b>></b><br><br>
Maior ou igual a: &emsp;&emsp;<b>>=</b><br><br>

### Sintaxe:
<code>if b > a:<br>
&emsp;#código</code>  
Verifica se b é maior que a.<br><br>

<code>elif b == a:<br>
&emsp;#código</code>  
Verifica se b é igual a a caso a condição anterior seja falsa.<br><br>

<code>else:<br>
&emsp;#código</code>  
É executado caso todas as condições sejam falsas.<br><br>

### Maneiras curtas de escrever if:
<code>if a > b: print("a is greater than b")</code>  
É possível escrever o if em apenas uma linha.<br><br>
  
<code>print("A") if a > b else print("B")</code>  
Diferentes prints para determinadas condições.<br><br>

## While 🔄

### Sintaxe:

<code>while i < 6:<br>
&emsp;#código</code>  
Repete o código até que i seja maior ou igual a 6.<br><br>

<code>break</code>  
Interrompe o ciclo do while.<br><br>
  
## For ⏳
 
### Sintaxe:

<code>for x in fruits:<br>
&emsp;#código</code>  
Repete o código para cada item presente em fruits.<br><br> 

<code>continue</code>  
Retorna ao inicio do ciclo.<br><br>
  
### Funções: 
  
<code>for x in range(6):<br>
&emsp;#código</code>  
Repete o código até x atingir o valor do range.<br><br> 

## Funções 🧱

<code> def calcular_area_poligono(vertices):
    area = 0
    n = len(vertices)
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
    return abs(area) / 2 </code>
    
<code>def my_function():<br>
&emsp;#código</code>  
Cria uma função.<br><br> 

<code>my_function()</code>  
Chama uma função.<br><br>

<code>return</code>  
Retorna um valor.<br><br>
 
## Classe 🌳

<code>class MyClass<br>
&emsp;#código</code>  
Cria uma classe.<br><br> 

<b>Uma função init é executada sempre quando a classe é chamada.</b><br>
<code>class MyClass<br>
&emsp;def __init__(self, name, age):<br>
&emsp;&emsp;self.name = name<br>
&emsp;&emsp;self.age = age</code>  
Define uma função init.<br><br> 

## EOFError ⛔

<code>while True:
&emsp;try: <br>
&emsp;&emsp;#codigo <br><br>
&emsp;&emsp;except EOFError: <br>
&emsp;break </code>    
