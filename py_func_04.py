import os 

def get_full_name(first_name: str, 
                  last_name: str, 
                  nick_name:str) -> str:
    
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    nick_name = nick_name.capitalize()
    
    return f'{first_name} {last_name} {nick_name}'

def get_name_parts(full_name: str) -> list:
    name_parts = full_name.split(' ')
    
    return name_parts

#full_name = get_full_name('Pero', 'Peric', 'Pere')
first_name = input('Upisite ime: ')
last_name = input('Upisite prezime: ')
nick_name = input('Upisite nadimak: ')

full_name = get_full_name(last_name=last_name,
                          nick_name=nick_name, 
                          first_name=first_name)


name_elements = get_name_parts(full_name)

#if os.name == 'ne':
    #os.system('cls')
#else:
    #os.system('clear')

os.system('cls' if os.name =='nt' else 'clear')
print(full_name)
print()
for name_element in name_elements:
    print(name_element, end='; ')
    
print()
print()
