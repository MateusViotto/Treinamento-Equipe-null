# Python 🐍💻

## Print 💬

### Printar uma variável

<code>print( "{ :.1f}".format( x ))</code>    
Imprime a variável x com 1 casa decimal    

<i> print( f"{ x } ") </i> <br><br>

<i> print( x ) </i> <br><br>

## Variáveis 🔠

<i>x = 0 </i><br>
Declara uma variável x com o valor 0<br><br>

<i>int(x) = 0 </i><br>
Declara uma variável inteira x com o valor 0<br><br>

## Booleanos ⁉

Booleano retorna True ou False.<br><br>
<i>print(10 > 9) : True</i><br>
<i>print(10 == 9) : False</i><br>
<i>print(10 < 9) : False</i><br><br>

<i>print( isinstace ( x , int ))</i><br>
Verifica se x é um número inteiro.<br><br>
  
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
<i>int(2.2) : 2 </i><br>
Converte um número float em um inteiro.<br><br>

<i>float(2) : 2.0 </i><br>
Converte um número inteiro em um float.<br><br>

<i>str(2) : "2" </i><br>
Converte um número em string.<br><br>

<i>int(True) : 1 </i><br>
Converte um booleano em inteiro.<br><br>

<i>bool(1) : True </i><br>
Converte um inteiro em booleano.<br><br>

## String 📃

### Navegando pela string:

#### Fatiando a string:
<i>
a[1]</i><br>
Consulta a segunda letra da variável "a".<br><br>

<i>
a[-1]</i><br>
Consulta a última letra da variável "a".<br><br>

<i>
a[0:10]</i><br>
Consulta as letras no intervado de 0 a 10 da variável "a".<br><br>

<i>
a[:10]</i><br>
Consulta todas as letras até a 10 da variável "a".<br><br>

<i>
a[1:]</i><br>
Consulta todas as letras até da 1 em diante da variável "a".<br><br>

<i>
a[-10: -1]</i><br>
Consulta as letras no intervado de 10 a 1 da variável "a".<br><br>

#### Modificando a string:

<i>
a.upper()</i><br>
Capitaliza todas as letras da variável.<br><br>

<i>
a.lower()</i><br>
Transforma todas as letras da variável em letras minúsculas.<br><br>

<i>
a.strip()</i><br>
Remove todos os espaços da variável.<br><br>

<i>
a.replace("H", "J")</i><br>
Substitui todas as letras "H" pela letra "J" na variável.<br><br>

<i>
a.split(",")</i><br>
Separa a string em tuplas.<br><br>

#### Outros:
<i>
len(a)</i><br>
Consulta o tamanho da variável "a".<br><br>

<i>
print("free" in txt)</i><br>
Retorna True/False caso "free" faça parte da variável txt.<br><br>



### Métodos:


<b>Atenção: Todos os métodos retornam um novo valor, eles não alteram o valor original.</b>


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

<i>thislist = [ "item1", "item2", "item3" ]</i><br>
Criando uma lista.<br><br>

<i>mylist = thislist.copy()</i><br>
Copia uma lista.<br><br>

### Consultar itens da lista:

<i>print( len( thislist))</i><br>
Imprime o tamanho da lista.<br><br>

<i>thislist[ 1 ] <br>
thislist[ -1 ]<br>
thislist[ 2:5 ]<br>
thislist[ :4 ]<br>
thislist[ 2: ]<br>
thislist[-4:-1]
</i><br>
Exemplos de consulta de itens da lista.<br><br>

<i>if "apple" in thislist: <br>
&emsp;print("Yes, 'apple' is in the fruits list")</i><br>
Consulta se o item existe na lista.<br><br>

### Mudar itens da lista:

<i>thislist[1] = "blackcurrant"</i><br>
Altera o segundo valor da lista.<br><br>

<i>thislist[1:3] = ["blackcurrant", "watermelon"]</i><br>
Altera o intervalo de valores da lista.<br><br>

<i>thislist.insert(2, "watermelon")</i><br>
Insere um novo item na posição sem substituir pelo valor naquela posição.<br><br>

<i>thislist.append("orange")</i><br>
Adiciona um item na lista.<br><br>

<i>thislist.extend(["mango", "pineapple", "papaya"])</i><br>
Adiciona mvários itens na lista.<br><br>

<i>thislist.remove("banana")</i><br>
Remove um item da lista.<br><br>

<i>thislist.pop(1)</i><br>
Remove um item de uma determinada posição da lista.<br><br>

<i>thislist.pop()</i><br>
Remove o último item da lista.<br><br>

<i>del thislist[0]</i><br>
Remove o primeiro item da lista.<br><br>

<i>del thislist</i><br>
Deleta a lista.<br><br>

<i>thislist.clear()</i><br>
Limpa a lista.<br><br>

### Loop pela lista:

<i>for x in thislist:</i><br>
Percorre todos os itens da lista.<br><br>

<i>newlist = [x for x in fruits if x != "apple"]</i><br>
Cria uma lista a partir de outra lista com restrições.<br><br>

<i>newlist = [x if x != "banana" else "orange" for x in fruits]</i><br>
Cria uma nova lista a partir de outra, adicionando "orange" sempre quando é "banana".<br><br>

### Organizar a lista:

<i>thislist.sort()</i><br>
Organiza a lista em ordem alfabetica.<br><br>

<i>thislist.sort(reverse = True)</i><br>
Organiza a lista em ordem reversa a alfabetica.<br><br>

<i>def myfunc(n):<br>
  return abs(n - 50)<br>
  thislist.sort(key = myfunc)</i><br>
Organiza a lista baseado em quão próximo o valor está de 50.<br><br>

<i>thislist.sort(key = str.lower)</i><br>
Organiza a lista em ordem alfabética separando as palavras com letras maiúsculas<br><br>

### Juntar duas listas:

<i>lista3 = lista2 + lista1</i><br>
Cria uma nova lista baseada na junção de outras duas.<br><br>

### Outros métodos:

<i>count( )</i><br>
Retorna o numero de elementos com um determinado valor.<br><br>

<i>index( )</i><br>
Retorna o indice em que se encontra um determinado valor.<br><br>

## Tuplas 📁

<b>Diferente das listas as tuplas são imutáveis. Isso significa que não é possível alterá-la.<br>
Uma tupla pode ser composta por vários tipos (int, float, str, bool)</b>
  
<i>thistuple = ( "item1", "item2", "item3" )</i><br>
Criando uma tupla.<br><br>

<i>thistuple( 1 ) <br>
thistuple( -1 )<br>
thistuple( 2:5 )<br>
thistuple( :4 )<br>
thistuple( 2: )<br>
thistuple( -4:-1 )
</i><br>
Exemplos de consulta de itens da tupla.<br><br>

### Juntar duas listas:

<i>tupla3 = tupla2 + tupla1</i><br>
Cria uma nova tupla baseada na junção de outras duas.<br><br>
 
### Métodos:

<i>count( )</i><br>
Retorna o numero de elementos com um determinado valor.<br><br>

<i>index( )</i><br>
Retorna o indice em que se encontra um determinado valor.<br><br>

  
## Sets 📦

<b>Diferente das tuplas e listas os sets não possuem uma ordem. Os sets possuem apenas valores unicos.</b>
  
<i>thisset = {"apple", "banana", "cherry"}</i><br>
Criando um set.<br><br>

### Consultar itens de um set:

<i>print( len( thisset))</i><br>
Imprime o tamanho do set.<br><br>
 
### Adicionar e remover itens de um set:
  
<i>thisset.add("orange")</i><br>
Adiciona um item ao set.<br><br>
  
<i>thisset.update(tropical)</i><br>
Adiciona os elementos de "tropical" ao set.<br><br>
  
<i>thisset.remove("banana")</i><br>
Remove um item do set. <b>Se o item a ser excluído não existir ocorrerá um erro.</b><br><br>
  
<i>thisset.discard("banana")</i><br>
Remove um item do set. <b>Se o item a ser excluído não existir NÃO ocorrerá um erro.</b><br><br>
  
<i>thisset.pop( )</i><br>
Remove um item aleatório do set.<br><br>

<i>thisset.clear( )</i><br>
Limpa o set.<br><br>

<i>del thisset</i><br>
Exclui um set.<br><br>

### Junções com sets:
  
  ![image](https://user-images.githubusercontent.com/96631827/226457376-b4c137b7-fb4f-4468-8bc4-679b7ed20454.png)
  
<i>set3 = set1.union(set2)</i><br>
Une dois sets dentro de outro.<br><br>

<i>x.intersection_update(y)</i><br>
Mantém apenas os itens presentes nos dois sets.<br><br>

<i>z = x.intersection(y)</i><br>
Retorna apenas os itens presentes nos dois sets.<br><br>

![image](https://user-images.githubusercontent.com/96631827/226458063-131024e6-06c5-4df0-8f5d-37dab8089c81.png)
  
<i>x.symmetric_difference_update(y)</i><br>
Mantém apenas os itens presentes que NÃO estão nos dois sets.<br><br>
 
<i>z = x.symmetric_difference(y)</i><br>
Retorna apenas os itens presentes que NÃO estão nos dois sets.<br><br>
  
![image](https://user-images.githubusercontent.com/96631827/226457464-5b30751b-5c41-4c96-b29a-d0b50f588d39.png)

<i>set( album_set1 ).issuperset( album_set2 )</i><br>
Verifica se album_set1 contém todos os itens de album_set2.<br><br>

<i>album_set1.difference( album_set2 ) </i><br>
Encontra as diferenças em set1 mas não em set2.<br><br>
  
## Dicionário 📕

<b>Dicionários são utilizados para armazenar dados em "keys". Um dicionário é uma coleção mutável que não permite duplicações.</b>  
 
<i>thisdict = {<br>
  "brand": "Ford",<br>
  "model": "Mustang",<br>
  "year": 1964<br>
} </i><br>
Declarando um dicionário.<br><br>

<i>thisdict = dict(name = "John", age = 36, country = "Norway")</i><br>
Declarando um dicionário utilizando um construtor.<br><br>
 
<i>len(thisdict)</i><br>
Retorna o tamanho do dicionário.<br><br>
### Acessar itens do dicionário:
  
<i>thisdict["brand"]</i><br>
Consultando um valor no dicionário.<br><br>

<i>x = thisdict.get("model")</i><br>
Consultando um valor no dicionário.<br><br>

<i>x = thisdict.keys()</i><br>
Retorna uma lista com as "keys".<br><br>
  
<i>x = thisdict.values()</i><br>
Retorna uma lista com os valores.<br><br>
  
<i>x = thisdict.items()</i><br>
Retorna uma lista com os itens.<br><br>

### Mudar valores em um dicionário:

<i>thisdict["year"] = 2018</i><br>
Altera um valor do dicionário.<br><br>

<i>thisdict.update({"year": 2020})</i><br>
Altera um valor do dicionário.<br><br>

<i>thisdict["color"] = "red"</i><br>
Adiciona um item do dicionário.<br><br>
  
<i>thisdict.update({"color": "red"})</i><br>
Adiciona um item do dicionário.<br><br>

<i>thisdict.pop("model")</i><br>
Remove um item do dicionário.<br><br>

<i>del thisdict["model"]</i><br>
Remove um item do dicionário.<br><br>

<i>thisdict.clear()</i><br>
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
<i>if b > a:<br>
&emsp;#código</i><br>
Verifica se b é maior que a.<br><br>

<i>elif b == a:<br>
&emsp;#código</i><br>
Verifica se b é igual a a caso a condição anterior seja falsa.<br><br>

<i>else:<br>
&emsp;#código</i><br>
É executado caso todas as condições sejam falsas.<br><br>

### Maneiras curtas de escrever if:
<i>if a > b: print("a is greater than b")</i><br>
É possível escrever o if em apenas uma linha.<br><br>
  
<i>print("A") if a > b else print("B")</i><br>
Diferentes prints para determinadas condições.<br><br>

## While 🔄

### Sintaxe:

<i>while i < 6:<br>
&emsp;#código</i><br>
Repete o código até que i seja maior ou igual a 6.<br><br>

<i>break</i><br>
Interrompe o ciclo do while.<br><br>
  
## For ⏳
 
### Sintaxe:

<i>for x in fruits:<br>
&emsp;#código</i><br>
Repete o código para cada item presente em fruits.<br><br> 

<i>continue</i><br>
Retorna ao inicio do ciclo.<br><br>
  
### Funções: 
  
<i>for x in range(6):<br>
&emsp;#código</i><br>
Repete o código até x atingir o valor do range.<br><br> 

## Funções 🧱

<i>def my_function():<br>
&emsp;#código</i><br>
Cria uma função.<br><br> 

<i>my_function()</i><br>
Chama uma função.<br><br>

<i>return</i><br>
Retorna um valor.<br><br>
 
## Classe 🌳

<i>class MyClass<br>
&emsp;#código</i><br>
Cria uma classe.<br><br> 

<b>Uma função init é executada sempre quando a classe é chamada.</b><br>
<i>class MyClass<br>
&emsp;def __init__(self, name, age):<br>
&emsp;&emsp;self.name = name<br>
&emsp;&emsp;self.age = age</i><br>
Define uma função init.<br><br> 

## EOFError ⛔

<i> try: <br>
&emsp;#codigo <br><br>
except EOFError: <br>
&emsp; break <br><br></i>
