# CS361_Assignment_9
Ski Resort Pricing Microservice: This microservice contains a dictionary with the 2024 season pass prices for hundreds of ski resorts across the country. The microservice can be used to return the pricing for a specific ski resort that someone is searching for. 

This microservice uses text files as a pipeline to communicate. It will monitor and read text from ski_resort_name.txt to get a particular ski resort, and return the season pass pricing for that resort on price_output.txt. If the resort is not found, it will instead return an error message to price_output.txt. 

All data in the dictionary is from https://www.onthesnow.com/united-states/lift-tickets, accessed Feb 21, 2024. The name of the resorts stored in the microservice are spelled exactly as they are on this webpage. 

# Requesting data from the microservice: 
Open the text file ski_resort_name.txt, write the name of the ski resort you would like the pricing for into the text file, and close the text file. 

  text_file = open("ski_resort_name.txt", "w")
  
  text_file.write(str(ski_resort_1))
  
  text_file.close()

# Receiving data from the microservice:
Open the text file price_output.txt, read the pricing information returned by the microservice, close the text file.

  text_file = open("price_output.txt", "r")

  price = text_file.readline()
  
  text_file.close()

# UML Sequence Diagram:

![sequence diagram (1)](https://github.com/whangho/CS361_Assignment_9/assets/114325042/a51210f5-9256-4aad-8253-bea6d59e00bb)

