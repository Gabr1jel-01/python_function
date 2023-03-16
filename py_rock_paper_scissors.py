'''
Racunalo bira izmedu kamena, skara i papira
Pitamo korisnika da on izabere izmedu kamena, skara i papira i pohranimo u neku varijablu
Usporedimo izbore i ovisno o izboru prikazemo rezultat
'''
import random
import os

pieces = {1: 'kamen',
          2: 'skare',
          3: 'papir'
          }


def menu() -> None:
    os.system('cls')
    print('*' * 50)
    print()
    for key, value in pieces.items():
        print(f'{key}. {value}')
    print()
    print('*' * 50)

def message(message: str, destination: str):
    match destination:
        case 'console':
            print(message)
        case 'db_':
            pass
        case 'txt_file':
            pass
        case _:
            pass
    
    pass


# Funkcija za unos
# Funkcija za provjeru str
# Funkcija za provjeru int


def user_input_validation(user_input: str) -> int:

    while not user_input.isnumeric():
        print('Morate unijeti brojke')
        user_input = input('Pokusajte unijeti ispravan broj iz izbornika ')

    user_input = int(user_input)
    while user_input < 1 or user_input > 3:
        print('Krivi unos')
        print('Unesite jedan od brojeva iz izbornika!')
        user_input = int(input('Pokusajte unijeti ispravan broj iz izbornika '))

    return int(user_input)

def check_game_status(computer_choice: int, user_choice: int) -> None:
    destination = 'console'
    
    if computer_choice == user_choice:
        message(
        print(f'Nerijeseno  - Vas izbor {pieces[user_choice]} je isti kao {pieces[computer_choice]}', destination))
    elif computer_choice == 1 and user_choice == 2:
        message(
        print(f'Izgubili ste  - Vas izbor {pieces[user_choice]} gubi od {pieces[computer_choice]}', destination))
    elif computer_choice == 1 and user_choice == 3:
        message(
        print(f'Pobijedili ste  - Vas izbor {pieces[user_choice]} pobjeduje {pieces[computer_choice]}', destination))
    elif computer_choice == 2 and user_choice == 1:
        message(
        print(f'Pobijedili ste  - Vas izbor {pieces[user_choice]} pobjeduje {pieces[computer_choice]}', destination))
    elif computer_choice == 2 and user_choice == 3:
        message(
        print(f'Izgubili ste  - Vas izbor {pieces[user_choice]} gubi od {pieces[computer_choice]}', destination))
    elif computer_choice == 3 and user_choice == 1:
        message(
        print(f'Izgubili ste  - Vas izbor {pieces[user_choice]} gubi od {pieces[computer_choice]}', destination))
    elif computer_choice == 3 and user_choice == 2:
        message(
        print(f'Pobijedili ste  - Vas izbor {pieces[user_choice]} pobjeduje {pieces[computer_choice]}', destination))
    

while True:
    menu()

    user_choice = user_input_validation(input('Izaberite jedan broj iz izbornika : '))
    computer_choice = random.randint(1, 3)

    check_game_status(computer_choice, user_choice)

    next_round = input('Zelite li ponoviti igru? (Da/Ne)')
    if next_round[: 2].lower() != 'da':
        break


# Pozdravna poruka
