print('Digite uma palavra para verificar se é um palíndromo:')
string = input()
string_reverse = []

i = len(string)
while i > 0: 
    string_reverse += string[i-1]
    i = i - 1 # decrement index 

string_reverse = "".join(string_reverse)

if (string.lower()) == (string_reverse.lower()):
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')





