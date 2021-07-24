#Generates a phrase dataset for an AI powered chatbox
#There are different categories for different types of potential questions
inventory = ["VMs", "security groups", "NICs", "route tables", "rules", "networks", "CIDRs", "subnets", "subscriptions", "resource groups"]
attribute = ["location", "status", "utilization", "events", "faults", "cost", "created", "deleted"]
timeStamp = ["yesterday", "last week", "last month"]
questions = []
#Category 1: Inventory with Attribute at Time
def cat1():
  y = ""
  z = ""
  w = ""
  questions = ["What are the " + y + "in" + z + " at " + w + "?", "Can I see the " + y + " in " + z + " at " + w + "?", "Show me all of " + y + "in " + z + " at " + w + ".", "Give me information on " + y + "in " + z + " at " + w + ".", "I need information on " + y + " in " + z + " at " + w + ".", "Access all " + y + " in " + z + " at " + w + ".", "Find all" + y + " in " + z + " at " + w + "." , "I want all" + y + " in " + z + " at " + w + ".", "I want to see all " + y + " in " + z + " at " + w + ".", "Can I access " + y + " in " + z + " at " + w + ".", "Open information on" + y + " in " + z + " at " + w + "."]
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for timeItem in timeStamp:
          questions = ["What are the " + inventoryItem + " in " + attributeItem + " at " + timeItem + "?", "Can I see the " + inventoryItem + " in " + attributeItem + " at " + timeItem + "?", "Show me all of " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Give me information on " + inventoryItem + "in " + attributeItem + " at " + timeItem + ".", "I need information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + " at " + timeItem + ".", "Access all " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Find all " + inventoryItem + " in " + attributeItem + " at " + timeItem + "." , "I want all " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "I want to see all " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Can I access " + inventoryItem + " in " + attributeItem + " at " + timeItem + "?", "Open information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + "."]
          with open("output.txt", "a") as f:
            f.write('\n')
            f.write(questions[question])
          print(questions[question])
#Category 2: Attribute of Inventory at Time
def cat2():
  y = ""
  z = ""
  w = ""
  questions = ["Show me the " + z + " of " + y + " at " + w + "?", z + " of " + y + " at " + w, "What is " + z + " of " + y + " at " + w + "?", "Show " + z + " of " + y + " at " + w, "Which ones have " + z + " of " + y + " at " + w, "Give me the " + z + " of " + y + " at " + w, "Are there any "  + z + " of " + y + " at " + w, "Show the "  + z + " of " + y + " at " + w] 
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for timeItem in timeStamp:
          questions = ["Show me the " + inventoryItem + " of " + attributeItem + " at " + timeItem + "?", inventoryItem + " of " + attributeItem + " at " + timeItem, "What is " + inventoryItem + " of " + attributeItem + " at " + timeItem + "?", "Show " + inventoryItem + " of " + attributeItem + " at " + timeItem, "Which ones have " + inventoryItem + " of " + attributeItem + " at " + timeItem, "Give me the " + inventoryItem + " of " + attributeItem + " at " + timeItem, "Are there any "  + inventoryItem + " of " + attributeItem + " at " + timeItem, "Show the "  + inventoryItem + " of " + attributeItem + " at " + timeItem]
          with open("output.txt", "a") as f:
            f.write('\n')
            f.write(questions[question])
          print(questions[question])

#Category 3: Time Inventory had Attribute
def cat3():
  y = ""
  z = ""
  w = ""
  questions = ["When did " + y + " have " + z, "What time did " + y + " have " + z, "Give me a time when "  + y + " had " + z, "What times did" + y + " have " + z, "At what time did " + y + " have " + z, "Give me time when "  + y + " had " + z, "Were there any times when "  + y + " had " + z]
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for timeItem in timeStamp:
          questions = ["When did " + inventoryItem + " have " + attributeItem, "What time did " + inventoryItem + " have " + attributeItem, "Give me a time when "  + inventoryItem + " had " + attributeItem, "What times did" + inventoryItem + " have " + attributeItem, "At what time did " + inventoryItem + " have " + attributeItem, "Give me time when "  + inventoryItem + " had " + attributeItem, "Were there any times when "  + inventoryItem + " had " + attributeItem]
          with open("output.txt", "a") as f:
            f.write('\n')
            f.write(questions[question])
          print(questions[question])

#Category 4: How many Inventory have Attribute at Time
def cat4():
  x = ""
  y = ""
  z = ""
  questions = []
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for timeItem in timeStamp:
          questions = ["How many " + inventory + " were " + attribute +" at " + timeStamp, "How much " + inventory + " were " + attribute +" at " + timeStamp, "What number of " + inventory + " were " + attribute +" at " + timeStamp, "How many " + inventory + " were " + attribute +" at " + timeStamp]
          with open("output.txt", "a") as f:
            f.write('\n')
            f.write(questions[question])
          print(questions[question])
#Category 5: How many Attributes occured on Inventory at time
def cat5():
  x = ""
  y = ""
  z = ""
  questions = ["How many " + x + " occured on " + y + " at " + z, "Which " + y + " did the " + x + " occur on at " + z, "Tell me the number of "  + x + " that occured on " + y + " at" + z, "Show me how many " + x + " happened to the " + y + " at " + z, "Report to me how many " + x + " happened to " + y + " at " + z, "Display the" + y + " which " + x + " happened to at " + z]
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for timeItem in timeStamp:
          questions = ["How many " + attributeItem + " occured on " + inventoryItem + " at " + timeItem, "Which " + inventoryItem + " did the " + attributeItem + " occur on at " + timeItem, "Tell me the number of "  + attributeItem + " that occured on " + inventoryItem + " at" + timeItem, "Show me how many " + attributeItem + " happened to the " + inventoryItem + " at " + timeItem, "Report to me how many " + attributeItem + " happened to " + inventoryItem + " at " + timeItem, "Display the" + inventoryItem + " which " + attributeItem + " happened to at " + timeItem]
          with open("output.txt", "a") as f:
            f.write('\n')
            f.write(questions[question])
          print(questions[question])
cat5()