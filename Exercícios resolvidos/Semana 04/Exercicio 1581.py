i = int(input())
language_list = []
result = []

def chooseLang():
    first_element = language_list[0]
    for word in language_list:
        if first_element != word:
            check_result = False
            result.append('ingles')
            break
        else:
            check_result = True
        
    if check_result:
        result.append(first_element)

for x in range(i):
    u = int(input())
    for y in range(u):
        language = input()
        language_list.append(language)
    chooseLang()
    language_list = []

for z in range(len(result)):
    print(result[z])

