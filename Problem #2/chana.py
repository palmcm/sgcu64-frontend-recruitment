place_list = ["Mahamakut Building", "Sara Phra Kaew", "CU Sport Complex", "Sanum Juub", "Samyan Mitr Town"]
user_inplace = dict()
count_place = list([0]*len(place_list))
seplinestring = "--------------------------------"

def checkin():
    telnumber = input("Enter phone number: ")
    for i in range(len(place_list)):
        print(f" {i+1}. {place_list[i]}")
    place = int(input("Select the place: ")) -1
    if telnumber in user_inplace:
        count_place[user_inplace[telnumber]] -=1
        print(f"Checking out {telnumber} from {place_list[user_inplace[telnumber]]}")
    user_inplace[telnumber] = place
    count_place[place] += 1
    print(f"Checking in {telnumber} into {place_list[place]}")

def checkout():
    telnumber = input("Enter phone number: ")
    if telnumber in user_inplace:
        count_place[user_inplace[telnumber]] -=1
        print(f"Checking out {telnumber} from {place_list[user_inplace[telnumber]]}")

def checkcount():
    print("Current Population")
    for i in range(len(place_list)):
        print(f" {i+1}. {place_list[i]}: {count_place[i]}")
        

def print_menu():
    print('''Welcome to Chula Chana!!!
Available commands:
  1. Check in user
  2. Check out user
  3. Print people count
  4. Quit''')

while True:
    print_menu()
    command = input("Please input any number: ")
    print(seplinestring)
    # Check in
    if command == '1':
        checkin()
    # Check out
    elif command == '2':
        checkout()
    # People count
    elif command == '3':
        checkcount()
    # Quit
    elif command == '4':
        break
    print(seplinestring)