import csv

def create_phonebook():
    phonebook = {}
    with open('phonebook.txt', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            last_name, first_name, middle_name, phone_number = row
            phonebook[(last_name, first_name)] = (middle_name, phone_number)
    return phonebook

def save_phonebook(phonebook):
    with open('phonebook.txt', 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        for key, value in phonebook.items():
            last_name, first_name = key
            middle_name, phone_number = value
            writer.writerow([last_name, first_name, middle_name, phone_number])

def search_phonebook(phonebook, search_term):
    matching_entries = []
    for key, value in phonebook.items():
        last_name, first_name = key
        if search_term.lower() in last_name.lower() or search_term.lower() in first_name.lower():
            matching_entries.append((key, value))
    return matching_entries

def add_entry(phonebook):
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    middle_name = input("Enter middle name: ")
    phone_number = input("Enter phone number: ")
    phonebook[(last_name, first_name)] = (middle_name, phone_number)
    print("Entry added successfully!")

def delete_entry(phonebook, search_term):
    matching_entries = search_phonebook(phonebook, search_term)
    if len(matching_entries) == 0:
        print("No matching entries found.")
    elif len(matching_entries) == 1:
        del phonebook[matching_entries[0][0]]
        print("Entry deleted successfully!")
    else:
        print("Multiple matching entries found. Please refine your search.")

def change_entry(phonebook, search_term):
    matching_entries = search_phonebook(phonebook, search_term)
    if len(matching_entries) == 0:
        print("No matching entries found.")
    elif len(matching_entries) == 1:
        last_name, first_name = matching_entries[0][0]
        middle_name, phone_number = matching_entries[0][1]
        new_last_name = input(f"Enter new last name ({last_name}): ") or last_name
        new_first_name = input(f"Enter new first name ({first_name}): ") or first_name
        new_middle_name = input(f"Enter new middle name ({middle_name}): ") or middle_name
        new_phone_number = input(f"Enter new phone number ({phone_number}): ") or phone_number
        del phonebook[matching_entries[0][0]]
        phonebook[(new_last_name, new_first_name)] = (new_middle_name, new_phone_number)
        print("Entry changed successfully!")
    else:
        print("Multiple matching entries found. Please refine your search.")


def main():
    phonebook = create_phonebook()
    while True:
        print("Select an option:")
        print("1. Search phonebook")
        print("2. Add entry")
        print("3. Delete entry")
        print("4. Change entry")
        print("5. Exit")
        choice = input()
        if choice == '1':
            search_term = input("Enter search term: ")
            matching_entries = search_phonebook(phonebook, search_term)
            if len(matching_entries) == 0:
                print("No matching entries found.")
            else:
                for entry in matching_entries:
                    print(f"{entry[0][0]}, {entry[0][1]}: {entry[1][0]}, {entry[1][1]}")
        elif choice == '2':
            add_entry(phonebook)
        elif choice == '3':
            search_term = input("Enter search term: ")
            delete_entry(phonebook, search_term)
        elif choice == '4':
            search_term = input("Enter search term: ")
            change_entry(phonebook, search_term)
        elif choice == '5':
            save_phonebook(phonebook)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()

