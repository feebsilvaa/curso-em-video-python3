# Dissecando uma variavel
value = input('Digite algo: ')

is_number = False

try:
    value = int(value)
    value_type = type(value)
    is_number = True
except:
    try:
        value = float(value)
        value_type = type(value)
        is_number = True
    except:
        value_type = type(value)

if not is_number:
    has_spaces = value.isspace()
    is_alphabetic = value.isalpha()
    is_alphanumeric = value.isalnum()
    is_uppercased = value.isupper()
    is_lowercased = value.islower()
    is_capitalized = value[0].isupper() and value[1].islower()

else:
    has_spaces = False
    is_alphabetic = False
    is_alphanumeric = False
    is_uppercased = False
    is_lowercased = False
    is_capitalized = False

print('O tipo primitivo desse valor é: {}'.format(value_type))
print('Só tem espaços? {}'.format(has_spaces))
print('É um número? {}'.format(is_number))
print('É alfabético? {}'.format(is_alphabetic))
print('É alfanumérico? {}'.format(is_alphanumeric))
print('Está em maiúsculas? {}'.format(is_uppercased))
print('Está em minúsculas? {}'.format(is_lowercased))
print('Está capitalizado? {}'.format(is_capitalized))
