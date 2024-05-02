PLACEHOLDER = "[name]"

with open("./Input/Names/invited_guests.txt") as guests_file:
    names = guests_file.readlines()
    print(names)

with open("./Input/Letter/birthday_invitation_letter.txt") as invitation_file:
    invitation_letter = invitation_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = invitation_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadytoSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
