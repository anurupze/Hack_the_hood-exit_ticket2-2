""" EXIT TICKET PART 2 for Week 5 """

# Here's a recap of what you did last week with dictionaries:
"""" EXIT TICKET """
# Create your food table here via key:value pairs
# (input the food & prices from lines 73-76):
food_prices = {
 "Chicken" : 1.59 ,
        "Beef" : 1.99,
        "Cheese" : 1.00,
        "Milk" : 2.50
  }
print(food_prices)

# Retrieve any value from the food prices dictionary by using its corresponding key along with the bracket notation
# For example, to get the price for cheese, run this:
milk_price = food_prices["Milk"]
print(milk_price)       

# Access the prices for each item & store into their own variable, just like the milk example.  
chicken_price = food_prices["Chicken"]
beef_price = food_prices["Beef"]
cheese_price = food_prices["Cheese"]

# Print those variables to check that you get the right value. Write the code to print on the line below:
print(chicken_price)  
print(beef_price) 
print(cheese_price)

### Now, we will continue working on DICTIONARIES. This time create your own dictionary from scratch, keeping the key:value pair format in mind. 
## First, create an empty dictionary for a shoe inventory at Foot Locker using curly braces:
shoe_count = {}
print(shoe_count) # this should be empty

# Now add a key-value pair to the empty dictionary with just 1 pair: Jordan 13 with 1 pair
shoe_count['Jordan 13'] = 1
print(shoe_count)

# Now add this key-value pair to the dictionary: Yeezy = 8
shoe_count['Yeezy'] = 8
print(shoe_count)

# # Now in the next 3 lines below, add the following key:value pairs, modeling after how Jordan 13 & Yeezy were added:

shoe_count['Air Max'] = 15
print(shoe_count)
# # # Foamposite:10
# # # Air Max:5
# # # SB Dunk:20
shoe_count['Foamposite'] = 10
shoe_count['Air Max'] = 5
shoe_count['SB Dunk'] = 20
print(shoe_count)


# # print(shoe_count)

# # ## Now access a value associated with a key from shoe_count by placing the key inside a set of square brackets. To access Air Max, you would use this code:
print(shoe_count['Air Max'])
# # # What output did you get? 5


# # # You can access a value & add it to a new variable, then print an f-string:
new_count = shoe_count['Air Max']
print(f"Currently, our branch has {new_count} pairs of Air Max in our inventory.")

# # # You double-checked how many pairs of Foamposite you have in stock, and you actually only had 9 pairs instead of 10. You can modify and correct this error by modifying the value using the next line:
shoe_count["Foamposite"] = 9
print(shoe_count)

# # # You also found out that you 1 more pair of Yeezy's, so in the next line, modify your dictionary to now reflect 9 pairs of Yeezy's--using the previous example in line 60
shoe_count["Yeezy"] = 9
print(shoe_count)

# # # A customer came in to purchase 2 pairs of SB Dunks. Deduct 2 from the value:
shoe_count["SB Dunk"] -= 2
print(shoe_count)

# # # Another customer came to now buy a pair of Jordan's. Modeling after line 68, deduct 1 from the value for Jordan's in the next line:
shoe_count["Jordan 13"] -= 1
print(shoe_count)

# # # Now a customer came back furious and returned a pair of Yeezy's. Add 1 to the value:
shoe_count["Yeezy"] += 1
print(shoe_count)

# # # That customer also returned shoes: 3 pairs of SB Dunk
shoe_count["SB Dunk"] += 3
print(shoe_count)

# # # At the end of the workday, you want to count the sum of all pairs of shoes that the store has. You can print this value this way:
print(sum(shoe_count.values()))

# # # The next day, the store got a new shipment. All stock increases by 7 pairs. Add 7 pairs to all 5 brands in the next 5 lines--model your code after either line 76 or line 80:
shoe_count['Jordan 13'] += 7
shoe_count['Yeezy'] += 7
shoe_count['Air Max'] += 7
shoe_count['Foamposite'] += 7
shoe_count['SB Dunk'] += 7
print(shoe_count)

# # # There is a special sale at the store. All stock decreases by 3. Decrease 3 pairs from all 5 brands in the next 5 lines--model your code after line 68:
shoe_count['Jordan 13'] -= 3
shoe_count['Yeezy'] -= 3
shoe_count['Air Max'] -= 3
shoe_count['Foamposite'] -= 3
shoe_count['SB Dunk'] -= 3
print(shoe_count)

# # # Finally, count the sum of all pairs of shoes that the store has. You can print this value this way:
print(sum(shoe_count.values()))
# # # Write here how many total pairs of shoes are in the inventory: 65


# # ### NOW LET'S GO WILD & MAKE A DICTIONARY OF YOUR OWN MAKING FROM SCRATCH!

# # ## Create another variable with a dictionary and fill in the values with whatever information you want. There must be at least four key : value pairs, like the last dictionary you created. Remember that dictionaries are most useful when they can highlight some sort of relationship between the values contained within it. Make sure that the values you use are related and make sense. An example: NBA_players = {“Lebron James”: 23, “Kobe Bryant”: 24, “Stephen Curry”: 30, “Brittney Griner”: 42} Here this variable “NBA_players” clues you into what sort of data is housed inside the structure. I have used the player names as the keys and their jersey numbers as the values. Would I possibly want to use the jersey numbers as the key instead? Why or why not? Think about this as you create your own dictionary.
# # # Other potential dictionary key:value pairs:
# # # movie/anime:year created
# # # car:price
# # # TikTok user:number of followers
# # # song:number of streams
# # # artist:number of albums
# # # month:money saved
# # # day:hours slept
# # # person:number of siblings
# # ## Create your dictionary starting on the next line:
stock_prices = {
  "Ford" : 12.45,
  "Intel" : 40.14,
  "Apple" : 154.90,
  "Tesla" : 809.25,
  "Sony" : 87.26
}

# # # Print your dictionary by adding the name of your dictionary inside print() below:
print(stock_prices)

# # ## Next, let's look at accessing the data stored within a dictionary. To retrieve any value from a dictionary you have to use its corresponding key along with bracket notation. Using the above dictionary, if I wanted to access the jersey number of Lebron James I would use the following line of code: 
# # # Steph_jersey = NBA_players[“Stephen Curry”] 
# # # and this would assign the value of 30 to the newly created variable.
# # ## Retrieve any value from your own dictionary, following the model in line 45 onto the next line:
Fords_price = stock_prices["Ford"]

Intels_price = stock_prices["Intel"]

Apple_price = stock_prices["Apple"]

Teslas_price = stock_prices["Tesla"]

Sonys_price = stock_prices["Sony"]

# # # Print those variables in the next line to check that you get the right value--model your code to line 26 in the food:price example:
# # print()
print(Fords_price)
print(Intels_price)
print(Apple_price)
print(Teslas_price)
print(Sonys_price)
# # ## Next is updating existing values in a dictionary. To update the value for a given key we use the same bracket notation approach and variable reassignment. We can either replace the value entirely or modify it using arithmetic operators. Using the same NBA_players dictionary as an example, what if I wanted to change Lebron’s jersey number to 6, which was his number during his time in Miami? 
# # # NBA_players[“Lebron James”] = 6 
# # # Update an existing value from 1 of your key:value pairs in the next line & then print your dictionary
stock_prices["Tesla"] = 810.44
# # print()
print(stock_prices)

# # # Finally we will need to know how to delete items from a dictionary as well. There is a built-in keyword in python: del which is used to delete keys from a dictionary. You can use the same bracket notation that you have been using for all the other processes so the line of code would look like the following: 
# # # del NBA_players[“Lebron James”]
# # # Delete an item from your dictionary then print it
# # del
# # print()
del stock_prices["Sony"]
print(stock_prices)

# # ## YOU DID IT!! GREAT JOB!
# # ### NOW commit to GitHub!