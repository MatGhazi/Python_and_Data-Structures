# name = ['mohsen','ghazal','nick', 'ali']
# surname = ['mm','gg','nn','kk']
# phone = ['11','22','33','66']
# address = ['1q1','2w2','3e3','adsf5']
# typeOfPhone = ['Home','Cellphone','Business','Home']
# details = ['xxx','kkk','ggg','dasd']
# timesOfSearch = []
# times_searched = {0:1,1:1,2:1,3:1}

name = []
surname = []
phone = []
address = []
typeOfPhone = []
details = []
timesOfSearch = []
times_searched = {}

entities = [name, surname, phone, address, typeOfPhone, details]

def add_contact():
    """
    Add contact to each lists seperately 
    """
    name.append(input('enter name: '))
    surname.append(input('enter surname: '))
    phone.append(input('enter phone: '))
    address.append(input('enter address: '))
    typeOfPhone.append(input('enter type Of Phone number (Home/Cellphone/business): '))
    details.append(input('enter details: '))

def search_contact():
    """
    Get name or surname and find its index. Then, retrive information based on its index.
    """
    name_surname = input('please enter name or surname: ')
    name_idx = 0
    surname_idx = 0

    try:
        name_idx = name.index(name_surname)
    except:
       surname_idx = surname.index(name_surname)
    
    idx = surname_idx + name_idx
    times_contact_was_searched(idx)
    print(f'{name[idx]} - {surname[idx]} - {phone[idx]} - {address[idx]} - {typeOfPhone[idx]} - {details[idx]}')

    return idx

def remove_contact():
    """
    First serach to find the index of the contact that is ready to remove.
    Based on index, remove the contact in all lists.
    """
    idx = search_contact()
    times_contact_was_searched(idx, remove= True)
    print('the contact was searched and removed')
    for i in entities:
        i.pop(idx)

def change_contact():
    """
    to change the contact first find its index and then change.
    """
    print('Please enter the contact that need to be changed')
    idx = search_contact()
    name[idx] = input('enter new name: ')
    surname[idx] = input('enter new surname: ')
    phone[idx] = input('enter new phone: ')
    address[idx] = input('enter new address: ')
    typeOfPhone[idx] = input('enter new type Of Phone number: ')
    details[idx] = input('enter new details: ')
    
def display():
    """
    Display all contacts
    """
    print('________________ The result is: _________________ \n\n')
    for i in entities:
        print(i, end='\n')

def times_contact_was_searched(idx, remove=False, search = False):
    """
    Times each contact occure are stored in a dictionary.
    This function should be called whenever the contact is searched in other functions.
    """

    if remove:
        del times_searched[idx]
        return

    if search :
        print(f'The given contact has been search for {times_searched.get(idx)} times till now')
        return
    temp = times_searched.get(idx,0) 
    times_searched.update({idx : temp+1})

def sort_contact():
    """
    sort contact accroding to digit and alphabetically 
    """
    temp = []
    print('Kind of sorting:', 
            '1 - Sort by name',
            '2 - Sort by family',
            '3 - Sort by type of number', sep = '\n')

    sorted_item = int(input('enter the item (1, 2, 3) to be sorted: '))
    if sorted_item == 1:
        after_sort = sorted(name)
        for _n in after_sort:
            temp.append(name.index(_n))

        # print('1111', temp)
        print(f'Phonebook contacts are sorted by names are as following: \n')
        for idx in temp:
            print(f'{name[idx]} - {surname[idx]} - {phone[idx]} - {address[idx]} - {typeOfPhone[idx]} - {details[idx]}')

    elif sorted_item == 2:
        after_sort = sorted(surname)
        for _n in after_sort:
            temp.append(surname.index(_n))
        print(f'Phonebook contacts are sorted by surnames are as following: \n')

        for idx in temp:
            print(f'{name[idx]} - {surname[idx]} - {phone[idx]} - {address[idx]} - {typeOfPhone[idx]} - {details[idx]}')

    elif sorted_item == 3:
        typeofphone_sp = input('enter which of Home/Cellphone/business you want: ')
        for i in range(len(typeOfPhone)):
            if typeOfPhone[i] == typeofphone_sp:
                temp.append(i)
        print(f'All contacts with type of {typeofphone_sp} are as following: \n')
        for idx in temp:
            print(f'{name[idx]} - {surname[idx]} - {phone[idx]} - {address[idx]} - {typeOfPhone[idx]} - {details[idx]}')

def search_by_part_of_content():
    """
    search by part of content of name, surname or phone
    """
    print(' \n * Enter part of contact detail: \n')
    choose = input('Do you want to search according to \n name \n surname \n phone \n ?:')
    part = input(f'enter part of the {choose} regarding the contact: ')
    
    # if choose ==1:
    specific_list = globals()[choose]
    for idx in range(len(specific_list)):
        if specific_list[idx].startswith(part):
            times_contact_was_searched(idx)
            print(f'{name[idx]} - {surname[idx]} - {phone[idx]} - {address[idx]} - {typeOfPhone[idx]} - {details[idx]}')

def menu():
    """
    Menu to be shown at the first stage
    """
    print("********************************************************************")
    print("\t\t\t <<<  Phonebook  >>>", flush=False)
    print("********************************************************************")
    print("\tYou can now perform the following operations\n")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Remove an existing contact")
    print("4. Change contact")
    print("5. Display all contacts")
    print("6. Show times a contact has been searched")
    print("7. Sort contacts")
    print("8. search by part of content")
    print("9. Exit phonebook")
    print("********************************************************************")
 
    choice = int(input("Please enter the number of operation: "))
    return choice


# Main function code
print("....................................................................")
print("Hello dear user, Welcome to phonebook")
print("....................................................................")

 
chic = 1

while chic in (1, 2, 3, 4, 5, 6, 7, 8, 9):
    chic = menu()
    if chic == 1:
        add_contact()
    elif chic == 2:
        search_contact()
    elif chic == 3:
        remove_contact()
    elif chic == 4:
        remove_contact()
    elif chic == 5:
        display()
    elif chic == 6:
        print('***  You need to search the contact ***')
        idx = search_contact()
        times_contact_was_searched(idx, search=True)
    elif chic == 7:
        sort_contact()
    elif chic == 8:
        search_by_part_of_content()
    elif chic == 9:
        print('--- Thanks ---')
        break

