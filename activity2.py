# Taking the total amount as input from user
Amount = int(input("Please enter the amount you want to withdraw : "))

# Calculating the number of notes of different denomintions
note_1 = Amount//5000
note_2 = (Amount%5000)//1000
note_3 = ((Amount%5000)%1000)//100
note_4 = (((Amount%5000)%1000)%100)//50
note_5 = ((((Amount%5000)%1000)%100)%50)//10

print("Notes of 5000 rupee", note_1)
print("Notes of 1000 rupee", note_2)
print("Notes of 100 rupee", note_3)
print("Notes of 50 rupee", note_4)
print("Notes of 10 rupee", note_5)