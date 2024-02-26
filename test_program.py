# Author: Howard Whang
# OSU Email Address: whangho@oregonstate.edu
# Assignment Name: Assignment 9
# Due Date: Feb 26, 2024
# Description: Test file for demonstrating the ski prices microservice.

import time

# Define 4 ski resorts and 1 error to test
ski_resort_1 = "alpine valley"
ski_resort_2 = "TAHOE DoNNer"
ski_resort_3 = "TELLURIDE"
ski_resort_4 = "Boreal MOUNtain ResOrt"
ski_resort_5 = "Some Unknown Resort"

# TEST 1: Wait 5 sec, then write name of ski resort to text file.
# The season pass price of that ski resort will print as well as show in another text file.
time.sleep(5)

text_file = open("ski_resort_name.txt", "w")
text_file.write(str(ski_resort_1))
text_file.close()

time.sleep(1)
pricing = open("price_output.txt", "r")
price_1 = pricing.readline()
print("The season pass pricing for", ski_resort_1, "is", price_1,".")
pricing.close()

# TEST 2: Wait 5 sec, then write name of ski resort to text file.
# The season pass price of that ski resort will print as well as show in another text file.
time.sleep(5)

text_file = open("ski_resort_name.txt", "w")
text_file.write(str(ski_resort_2))
text_file.close()

time.sleep(1)
pricing = open("price_output.txt", "r")
price_2 = pricing.readline()
print("The season pass pricing for", ski_resort_2, "is", price_2,".")
pricing.close()


# TEST 3: Wait 5 sec, then write name of ski resort to text file.
# The season pass price of that ski resort will print as well as show in another text file.
time.sleep(5)

text_file = open("ski_resort_name.txt", "w")
text_file.write(str(ski_resort_3))
text_file.close()

time.sleep(1)
pricing = open("price_output.txt", "r")
price_3 = pricing.readline()
print("The season pass pricing for", ski_resort_3, "is", price_3,".")
pricing.close()


# TEST 4: Wait 5 sec, then write name of ski resort to text file.
# The season pass price of that ski resort will print as well as show in another text file.
time.sleep(5)

text_file = open("ski_resort_name.txt", "w")
text_file.write(str(ski_resort_4))
text_file.close()

time.sleep(1)
pricing = open("price_output.txt", "r")
price_4 = pricing.readline()
print("The season pass pricing for", ski_resort_4, "is", price_4,".")
pricing.close()


# TEST 5: Wait 5 sec, then write name of ski resort to text file.
# The season pass price of that ski resort will print as well as show in another text file.
time.sleep(5)

text_file = open("ski_resort_name.txt", "w")
text_file.write(str(ski_resort_5))
text_file.close()

time.sleep(1)
pricing = open("price_output.txt", "r")
price_5 = pricing.readline()
print("The season pass pricing for", ski_resort_5, "is", price_5,".")
pricing.close()


quit()