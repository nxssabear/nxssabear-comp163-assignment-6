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
