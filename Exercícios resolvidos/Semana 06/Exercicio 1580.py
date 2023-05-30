

def countAnagrams(word):
    char_frequency = {}
    
    def factorial(n):
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact

    for char in word:
        char_frequency[char] = char_frequency.get(char, 0) + 1
      
    permutationCount = factorial(len(word))
    for frequency in char_frequency.values():
        permutationCount //= factorial(frequency)
    
    return permutationCount

result_list = []

while True:
    try: 
        word = input()
        result = countAnagrams(word) % (10**9 + 7)
        result_list.append(result)

    except EOFError: 
        for x in range (len(result_list)):
             print(result_list[x])
        break 
