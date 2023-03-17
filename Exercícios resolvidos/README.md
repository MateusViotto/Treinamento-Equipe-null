# Python 🐍💻

## Tipos
### Convertendo os tipos:
<i>int(2.2) = 2 </i><br>
Converte um número float em um inteiro.br><br>

<i>float(2) = 2.0 </i><br>
Converte um número inteiro em um float.br><br>

<i>str(2) = "2" </i><br>
Converte um número em string.br><br>

<i>int(True) = 1 </i><br>
Converte um booleano em inteiro.br><br>

<i>bool(1) = True </i>
Converte um inteiro em booleano.

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


