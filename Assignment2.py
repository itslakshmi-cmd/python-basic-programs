'''#SWAPING 2 NUMBERS WITHOUT USING THE 3RD VARIABLE
a=int(input("enter the value: "))
b=int(input("enter the value: "))

#swapping a number without 3rd variable
a,b=b,a

print("after swapping:")
print("a=",a)
print("b=",b)

#CHECK WHETHER A NUMBER ENTERED BY USER IS POSITIVE ,NEGATIVE OR ZERO
num=int(input("enter the value: "))

if num>0:
    print("its a positive")
elif num<0:
    print("its negative")
else:
    print("its zero")

#PRINT ALL NUMBERS FROM 1 TO 20 BUT SKIP NUMBERS THAT ARE MULTIPLES OF 3 
for i in range(1,21):
    if i%3==0:
        continue
    print(i)'''

#FIND AND PRINT THE FIRST NUMBER BETWEEN 1 AND 100 THAT IS DIVISIBLE BY BOTH 4 AND 6
for i in range(1,101):
    if i%4==0 and i%6==0:
        print(i)

#DEFINE A FUNCTION THAT TAKES TWO NUMBERS AND RETURNS BOTH THEIR SUM AND PRODUCT 
def calc(a,b):
    sum_result=a+b
    product_result=a*b
    return sum_result,product_result

x=int(input("enter the first number: "))
y=int(input("enter the value: "))

s,p=calc(x,y)
print("sum=",s)
print("product=",p)

#WRITE A FUNCTION CALCULATE(A,B=10) THAT RETURNS A+B.CALL IT WITH ONE AND TWO ARGUMENTS
def calculate(a,b=10):
    return a+b

#calling the function with one arguments
result1=calculate(5)

#calling the function with two arguments
result2=calculate(5,20)

print("when called with one arguments: ",result1)
print("when called with two arguments: ",result2)

#CREATE A FUNCTION AVERAGE(*NUMS) THAT CALCULATES THE AVERAGE OF ALL THE GIVEN NUMBERS

def average(*nums):
    total=sum(nums)
    count=len(nums)
    avg =total/count
    return avg

print("average is:", average(10,20,30))
print("average is:", average(5,10))
print("average is:",average(2,4,6,8,10))

#DEMOSTRATE THE DIFFERNCE BETWEEN LOCAL AND GLOBAL VARIABLES IN PYTHON 
# Global variable
x = 10

def display():
    # Local variable
    y = 5
    print("Inside function:")
    print("x (global) =", x)
    print("y (local)  =", y)

# Main program
display()
print("Outside function:")
print("x (global) =", x)
# print(y)  # This would cause an error because y is local

#CREATE A FUNCTION THAT INCREMENTS A GLOBAL COUNTER EACH TIME IT IS CALLED
# Global variable
counter = 0

def increment():
    global counter       # declare that we’re using the global variable
    counter += 1
    print("Function called", counter, "time(s)")

# Main program
increment()
increment()
increment()

#ASSUME FILE1.PY CONTAINS A FUNCTION GREET(). WRITE ANOTHER FILE TO IMPORT AND CALL THAT FUCNTION
from file1 import greet
greet()

#WRITE A PYTHON PROGRAM TO FIND THE SECOND LARGEST ELEMT IN A LIST
numbers = [10, 45, 25, 78, 56, 78]
largest = max(numbers)
numbers.remove(largest)
second_largest = max(numbers)
print("Second largest element:", second_largest)

#REMOVE DULICATE ELMENTS FROM A LIST WITHOUT USING SET()
lst = [1, 2, 3, 2, 4, 1, 5, 3]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print("List without duplicates:", unique)

#GENEERATE SQUARES OF EVEN NUMBERS(1-20) USING LIST COMPREHENSION
squares =[x**2 for x in range(1,21) if x%2==0]
print("squares of even numbers:",squares)

#USING MAP AND FILTER DOUBLE EACH ELEMENT AND KEEP ONLY NUMBER>5
def double(x):
    return x * 2

def greater_than_5(x):
    return x > 5

numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Double each element
doubled = list(map(double, numbers))

# Step 2: Keep only numbers greater than 5
result = list(filter(greater_than_5, doubled))

print("Result:", result)

#COUNT AND PRINT NUMBER OF VOWELS IN A STRING
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)

#FROM A STRING hELLOwORLD CREATE A LIST OF LOWERCASE LETTERS ONLY USING LIST COMPREHENSION
text = "HelloWorld"
lowercase_letters = [ch for ch in text if ch.islower()]
print("Lowercase letters:", lowercase_letters)

#FIND AND PRINT THE COMMON ELEMENTS BETWEEN TWO SETS 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1.intersection(set2)
print("Common elements:", common)

#CREATE A DICT FROM TEO LISTS ONE CONTAINING KEY AND THE OTHER ONE IS VALUES 
keys = ["name", "age", "city"]
values = ["Lakshmi", 20, "Bengaluru"]

zipped = zip(keys, values)#zip is the built in python function that joins two or more lists together element by element

print(list(zipped))

#FROM A DIC {"A":10,"B":20,"C":30},FIND THE KEY ASSOCIATED WITH THE MAXIMUN VALUE
data = {"A": 10, "B": 20, "C": 30}

# Find key with maximum value
max_key = max(data, key=data.get)

print("Key with maximum value:", max_key)

#WRITE A REGEX PATTERN TO EXTRACT ALL EMAIL ADDRESSES FROM A GIVEN TEXT 
import re

text = "Contact us at support@example.com, info@vivekatuitions.in, or lakshmi123@gmail.com."

# Regex pattern for email addresses
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)
print("Extracted email addresses:", emails)


#WRITE A REGEX TO VALIDATE AN INDIAN MOBIE NUMBER SHOULD STRT WITH 6-9 AND HAVE EXACTLY 10 DIGITS
import re

number = input("Enter a mobile number: ")

# Regex pattern for valid Indian mobile numbers
pattern = r'^[6-9]\d{9}$'

if re.match(pattern, number):
    print("Valid Indian mobile number")
else:
    print("Invalid mobile number")

#WRITE A PYTHON FUNTION THAT FILTERS OUT WORDS STARTING WITH A VOWEL FROM A GIVEN LIST USING FILTER()
def starts_with_vowel(word):
    vowels = 'aeiouAEIOU'
    return word[0] in vowels   # returns True if word starts with a vowel

def not_start_with_vowel(word):
    return not starts_with_vowel(word)  # True if it does NOT start with a vowel

def filter_words(words):
    return list(filter(not_start_with_vowel, words))

# Main program
word_list = ["apple", "banana", "orange", "grapes", "umbrella", "kiwi"]
filtered = filter_words(word_list)

print("Words not starting with a vowel:", filtered)

#COUNT THE FREQUENCY OF EACH WORD IN A SENTENCE AND STORE THE RESULT IN A DICT 
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Create empty dictionary
freq = {}

# Count frequency of each word
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word frequency dictionary:", freq)

#GIVEN A LIST OF FILESNAMES EXTRACT ONLY THOSE ENDING WITH .CSV USING REGULAR EXPRESSION 
import re

filenames = ["data.csv", "report.txt", "sales.csv", "image.png", "marks.csv", "notes.docx"]

# Regex pattern for files ending with .csv
pattern = r'\b\w+\.csv\b'

csv_files = [file for file in filenames if re.search(pattern, file)]

print("CSV files:", csv_files)

#WRITE A PYTHON SCRIPT THAT TAKES A SENTENCE AND PRINTS :TOTAL WORDS,UNIQUE WORDS TOTAL VOWELS, AND WORDS STARTING WITH UPPERCASE
sentence = input("Enter a sentence: ")

# Split into words
words = sentence.split()

# Total words
total_words = len(words)

# Unique words
unique_words = len(set(words))

# Count total vowels
vowels = "aeiouAEIOU"
total_vowels = 0
for ch in sentence:
    if ch in vowels:
        total_vowels += 1

# Words starting with uppercase
uppercase_words = [w for w in words if w[0].isupper()]
count_uppercase = len(uppercase_words)

# Display results
print("Total words:", total_words)
print("Unique words:", unique_words)
print("Total vowels:", total_vowels)
print("Words starting with uppercase:", uppercase_words)
print("Count of uppercase-starting words:", count_uppercase)

