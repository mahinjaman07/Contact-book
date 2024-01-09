userContact = {};
contactBook = True;
while contactBook:
    choice = input("1. Add New Contact \n"
                   "2. Search Contact\n"
                   "3. Display Contact \n"
                   "4. Edit Contact \n"
                   "5. Delete Contact\n"
                   "6. EXIT \n"
                   "Please Write Number Between 1-6 :");

    if choice == "1":
        contactName = input("Contact Name :");
        contactNumber = input("Contact Number :");
        userContact[contactName] = contactNumber;

    elif choice == "2":
        userName = userContact.keys();
        inputName = input("Enter Your Contact Name :");
        if inputName in userName:
            print(f"Your Contact Number is {userContact[inputName]}");
        else:
            print("No contacts found with this name..!"
                  "Thank You <3")


    elif choice == "3":
        names = userContact.keys();
        namesLen = len(names);
        if namesLen == 0:
            print("There is no contact number..!");

        else:
            for name in names:
                print("Name          Contact");
                print(f"{name}         {userContact[name]}");

    elif choice == "4":
        editContact = input("Edit Your Contact \n Enter your contact name: ");
        if editContact in userContact:
            updateContact = input("Update Your Contact :")
            userContact[editContact] = updateContact;
        else:
            print("You have not Change Contact.Because There are no contacts with this name..!");

    elif choice == "5":
        deleteContact = input("Enter Your Delete Contact Name :")
        if deleteContact in userContact:
            userContact.pop(deleteContact);

        else:
            print("You cannot delete a contact Because There are no contacts with this name..!");

    else:
        contactBook = False;



