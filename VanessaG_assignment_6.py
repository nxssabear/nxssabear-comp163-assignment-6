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

    address = i[3].strip().split() #split address into parts
    new_address = []

    for dress in address: #format address
        if len(dress) == 2 and dress.isalpha():
            new_address.append(dress.upper())
        else:
            new_address.append(dress.title())

    address = " ".join(new_address) #join address parts back together

    final_contacts.append([name, phone, email, address]) #add  contact parts to final list

print("=== CONTACT DIRECTORY ===")

print()

for j in final_contacts: #print each contact
    print(f"CONTACT {count}:")
    print(f"Name:     {j[0]}")
    print(f"Phone:    {j[1]}")
    print(f"Email:    {j[2]}")
    print(f"Address:  {j[3]}")
    print()

    count += 1

print("=== DIRECTORY SUMMARY ===")
print(f"Total contacts processed: {count - 1}")

print()

print("=== FORMATTED FOR PRINTING ===")

for a in final_contacts: #print each contact formatted for printing
   name_parts = a[0].split()
   last_name = name_parts[-1]
   first_names = " ".join(name_parts[0:-1]) #handle multiple first names

   print(f"{last_name}, {first_names:<25}{a[1]:<20}{a[2]}")
