'''
Racunalo bira izmedu kamena, skara i papira
Pitamo korisnika da on izabere izmedu kamena, skara i papira i pohranimo u neku varijablu
Usporedimo izbore i ovisno o izboru prikazemo rezultat
'''
import random
import os


pieces = { 1: 'kamen',
           2: 'skare', 
           3: 'papir'
}

def menu():
    os.system('cls')
    print()
    for key, value in pieces.items():
        print(f'{key}. {value}')
    print()





while True:
    menu()
    
    #region Players input -> computer and user
    user_choice = input('Izaberite jedan broj iz izbornika : ')
    while not user_choice.isnumeric():
        print('Morate unijeti brojke')
        user_choice = input('Pokusajte unijeti ispravan broj iz izbornika ')
    
    user_choice = int(user_choice)
    while int(user_choice) < 1 or int(user_choice) > 3:
        print('Krivi unos')
        print('Unesite jedan od brojeva iz izbornika!')
        user_choice = int(input('Pokusajte unijeti ispravan broj iz izbornika '))
#endregion

    #region Check game status
    computer_choice = random.randint(1,3)
    if computer_choice == user_choice:
        print(f'Nerijeseno  - Vas izbor {pieces[user_choice]} je isti kao {pieces[computer_choice]}')
    elif computer_choice == 1 and user_choice == 2:
        print(f'Izgubili ste  - Vas izbor {pieces[user_choice]} gubi od {pieces[computer_choice]}')
    elif computer_choice == 1 and user_choice == 3:
        print(f'Pobijedili ste  - Vas izbor {pieces[user_choice]} pobjeduje {pieces[computer_choice]}')
    elif computer_choice == 2 and user_choice == 1:
        print(f'Pobijedili ste  - Vas izbor {pieces[user_choice]} pobjeduje {pieces[computer_choice]}')
    elif computer_choice == 2 and user_choice == 3:
        print(f'Izgubili ste  - Vas izbor {pieces[user_choice]} gubi od {pieces[computer_choice]}')
    elif computer_choice == 3 and user_choice == 1:
        print(f'Izgubili ste  - Vas izbor {pieces[user_choice]} gubi od {pieces[computer_choice]}')
    elif computer_choice == 3 and user_choice == 2:
        print(f'Pobijedili ste  - Vas izbor {pieces[user_choice]} pobjeduje {pieces[computer_choice]}')
        
    #endregion
    
    
    next_round = input('Zelite li ponoviti igru? (Da/Ne)')
    if next_round[ : 2].lower() != 'da':
        break
    

# Pozdravna poruka 