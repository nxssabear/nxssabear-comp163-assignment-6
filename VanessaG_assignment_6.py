#Assignment 6
#No AI assistance was used in the completion of this assignment.

contacts = [] #list to hold contact information
count = 1

print("Enter contact information (format: name|phone|email|address):")
print()

while True: #collect contact information
   info = input()

   if info.strip().upper() == "DONE":
        break
    
   else:
        parts = info.split("|") 
        contacts.append(parts)
final_contacts = []

for i in contacts: #process each contact
    name = " ".join(i[0].strip().split()).title()
    phone = i[1]

    digits_only = "" #extract digits from phone number
    for char in phone:
          if char.isdigit():       
            digits_only += char

    phone = (f"({digits_only[0:3]}) {digits_only[3:6]}-{digits_only[6:]}") #format phone number

    email = i[2].strip().lower() #format email

    address = i[3].strip().split() #split address into parts
    new_address = []

    for dress in address: #format address
        if len(dress) == 2 and dress.isalpha():
            new_address.append(dress.upper())
        else:
            new_address.append(dress.title())

    address = " ".join(new_address) #join address parts back together


