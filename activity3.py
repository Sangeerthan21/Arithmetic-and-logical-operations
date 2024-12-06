# take marks as input from the server
print("Enter the marks obtained in 4 subjects:")
math = int(input("Maths : "))
science = int(input("Science : "))
english = int(input("English : "))
tamil = int(input("Tamil : "))

# Let's calculate the percentage of marks
sum = math+science+english+tamil
print("Sum of Math, Science, English, Tamil is", sum)

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)