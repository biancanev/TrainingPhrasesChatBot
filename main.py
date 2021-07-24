#Generates a phrase dataset for an AI powered chatbox
#In addition to generating different phrases and categories, this program also labels and separates the output by intent
inventory = ["VMs", "security groups", "NICs", "route tables", "rules", "networks", "CIDRs", "subnets", "subscriptions", "resource groups"]
attribute = ["location", "status", "utilization", "events", "faults", "cost", "created", "deleted"]
timeStamp = ["yesterday", "last week", "last month"]
month = ["January", "February", "March"]
#Category 1: Inventory with Attribute at Time
def cat1():
  data = ""
  w = ""
  y = ""
  z = ""
  questions = ["What are the " + y + "in" + z + " at " + w + "?", "Can I see the " + y + " in " + z + " at " + w + "?", "Show me all of " + y + "in " + z + " at " + w + ".", "Give me information on " + y + "in " + z + " at " + w + ".", "I need information on " + y + " in " + z + " at " + w + ".", "Access all " + y + " in " + z + " at " + w + ".", "Find all" + y + " in " + z + " at " + w + "." , "I want all" + y + " in " + z + " at " + w + ".", "I want to see all " + y + " in " + z + " at " + w + ".", "Can I access " + y + " in " + z + " at " + w + ".", "Open information on" + y + " in " + z + " at " + w + "."]
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for timeItem in timeStamp:
          questions = ["What are the {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modifiction|attribute} at {" + timeItem + "|time}?", "Can I see the " + inventoryItem + " in " + attributeItem + " at " + timeItem + "?", "Show me all of " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Give me information on " + inventoryItem + "in " + attributeItem + " at " + timeItem + ".", "I need information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + " at " + timeItem + ".", "Access all " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Find all " + inventoryItem + " in " + attributeItem + " at " + timeItem + "." , "I want all " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "I want to see all " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Can I access " + inventoryItem + " in " + attributeItem + " at " + timeItem + "?", "Open information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Send me information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Report information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Give me information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "I want information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Give me all " + attributeItem + inventoryItem + "at" + timeItem + ".", "Access all " + attributeItem + inventoryItem + "at" + timeItem + ".", "I want information on " + attributeItem + inventoryItem + "at" + timeItem + ".", "Find all " + attributeItem + inventoryItem + "at" + timeItem + "."]
          data += "\n" + questions[question]
          print(questions[question])
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for monthTime in month:
          for day in range(1,31):
            questions = ["What are the " + inventoryItem + " in " + attributeItem + " at " + timeItem + "?", "Can I see the " + inventoryItem + " in " + attributeItem + " at " + timeItem + "?", "Show me all of " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Give me information on " + inventoryItem + "in " + attributeItem + " at " + timeItem + ".", "I need information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + " at " + timeItem + ".", "Access all " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Find all " + inventoryItem + " in " + attributeItem + " at " + timeItem + "." , "I want all " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "I want to see all " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Can I access " + inventoryItem + " in " + attributeItem + " at " + timeItem + "?", "Open information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Send me information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Report information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Give me information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "I want information on " + inventoryItem + " in " + attributeItem + " at " + timeItem + ".", "Give me all " + attributeItem + " " + inventoryItem + " at " + timeItem + ".", "Access all " + attributeItem + " " + inventoryItem + " at " + timeItem + ".", "I want information on " + attributeItem + " " + inventoryItem + " at " + timeItem + ".", "Find all " + attributeItem + " " + inventoryItem + " at " + timeItem + ".", "Give me all " + attributeItem + " " + inventoryItem + " at " + timeItem + ".", "Access all " + attributeItem + " " + inventoryItem + " at " + timeItem + ".", "I want information on " + attributeItem + " " + inventoryItem + " at " + timeItem + ".", "Find all " + attributeItem + " " + inventoryItem + " at " + timeItem + "."]
            timeItem = monthTime + " " + str(day) + ", " + "2021"
            data += "\n" + questions[question]
            print(questions[question])
  with open("intent1.txt", "w") as f:
    f.write(data)
#Category 2: Attribute of Inventory at Time
def cat2():
  data = ""
  y = ""
  z = ""
  w = ""
  questions = ["Show me the " + z + " of " + y + " at " + w + "?", z + " of " + y + " at " + w, "What is " + z + " of " + y + " at " + w + "?", "Show " + z + " of " + y + " at " + w, "Which ones have " + z + " of " + y + " at " + w, "Give me the " + z + " of " + y + " at " + w, "Are there any "  + z + " of " + y + " at " + w, "Show the "  + z + " of " + y + " at " + w]  
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for timeItem in timeStamp:
          questions = ["Show me the " + inventoryItem + " of " + attributeItem + " at " + timeItem + "?", inventoryItem + " of " + attributeItem + " at " + timeItem, "What is " + inventoryItem + " of " + attributeItem + " at " + timeItem + "?", "Show " + inventoryItem + " of " + attributeItem + " at " + timeItem, "Which ones have " + inventoryItem + " of " + attributeItem + " at " + timeItem, "Give me the " + inventoryItem + " of " + attributeItem + " at " + timeItem, "Are there any "  + inventoryItem + " of " + attributeItem + " at " + timeItem, "Show the "  + inventoryItem + " of " + attributeItem + " at " + timeItem]
          data += "\n" + questions[question]
          print(questions[question])
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for monthTime in month:
          for day in range(1,31):
            questions = ["Show me the " + inventoryItem + " of " + attributeItem + " at " + timeItem + "?", inventoryItem + " of " + attributeItem + " at " + timeItem, "What is " + inventoryItem + " of " + attributeItem + " at " + timeItem + "?", "Show " + inventoryItem + " of " + attributeItem + " at " + timeItem, "Which ones have " + inventoryItem + " of " + attributeItem + " at " + timeItem, "Give me the " + inventoryItem + " of " + attributeItem + " at " + timeItem, "Are there any "  + inventoryItem + " of " + attributeItem + " at " + timeItem, "Show the "  + inventoryItem + " of " + attributeItem + " at " + timeItem]
            timeItem = monthTime + str(day) + ", 2021"
            data += "\n" + questions[question]
            print(questions[question])
  with open("intent2.txt", "w") as f:
    f.write(data)

#Category 3: Time Inventory had Attribute
def cat3():
  data = ""
  y = ""
  z = ""
  w = ""
  questions = ["When did " + y + " have " + z, "What time did " + y + " have " + z, "Give me a time when "  + y + " had " + z, "What times did" + y + " have " + z, "At what time did " + y + " have " + z, "Give me time when "  + y + " had " + z, "Were there any times when "  + y + " had " + z]
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for timeItem in timeStamp:
          questions = ["When did " + inventoryItem + " have " + attributeItem, "What time did " + inventoryItem + " have " + attributeItem, "Give me a time when "  + inventoryItem + " had " + attributeItem, "What times did" + inventoryItem + " have " + attributeItem, "At what time did " + inventoryItem + " have " + attributeItem, "Give me time when "  + inventoryItem + " had " + attributeItem, "Were there any times when "  + inventoryItem + " had " + attributeItem]
          data += "\n" + questions[question]
          print(questions[question])
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for monthTime in month:
          for day in range(1,31):
            questions = ["When did " + inventoryItem + " have " + attributeItem, "What time did " + inventoryItem + " have " + attributeItem, "Give me a time when "  + inventoryItem + " had " + attributeItem, "What times did" + inventoryItem + " have " + attributeItem, "At what time did " + inventoryItem + " have " + attributeItem, "Give me time when "  + inventoryItem + " had " + attributeItem, "Were there any times when "  + inventoryItem + " had " + attributeItem]
            timeItem = monthTime + str(day) + ", 2021"
            data += "\n" + questions[question]
            print(questions[question])
  with open("intent3.txt", "w") as f:
    f.write(data)

#Category 4: How many Inventory have Attribute at Time
def cat4():
  data = ""
  x = ""
  y = ""
  z = ""
  questions = ["How many " + y + " were " + x +" at " + z, "How much " + y + " were " + x +" at " + z, "What number of " + y + " were " + x +" at " + z, "How many " + y + " were " + x +" at " + z, "Give me the number of " + y + " were " + x +" at " + z, "Give me the amount of " + y + " were " + x +" at " + z, "What amount of " + y + " were " + x +" at " + z, "What is the size of " + y + " were " + x +" at " + z, "What volume of " + y + " were " + x +" at " + z, "What quantity of " + y + " were " + x +" at " + z, "Give me the volume of" + y + " that were " + x +" at " + z, "Give me the size " + y + " that were " + x +" at " + z, "Give me the quantity of " + y + " that were " + x +" at " + z]
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for timeItem in timeStamp:
          questions = ["How many " + inventoryItem + " were " + attributeItem +" at " + timeItem, "How much " + inventoryItem + " were " + attributeItem +" at " + timeItem, "What number of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "How many " + inventoryItem + " were " + attributeItem +" at " + timeItem, "Give me the number of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "Give me the amount of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "What amount of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "What is the size of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "What volume of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "What quantity of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "Give me the volume of" + inventoryItem + " that were " + attributeItem +" at " + timeItem, "Give me the size " + inventoryItem + " that were " + attributeItem +" at " + timeItem, "Give me the quantity of " + inventoryItem + " that were " + attributeItem +" at " + timeItem]
          data += "\n" + questions[question]
          print(questions[question])
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for monthTime in month:
          for day in range(1,31):
            questions = ["How many " + inventoryItem + " were " + attributeItem +" at " + timeItem, "How much " + inventoryItem + " were " + attributeItem +" at " + timeItem, "What number of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "How many " + inventoryItem + " were " + attributeItem +" at " + timeItem, "Give me the number of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "Give me the amount of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "What amount of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "What is the size of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "What volume of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "What quantity of " + inventoryItem + " were " + attributeItem +" at " + timeItem, "Give me the volume of" + inventoryItem + " that were " + attributeItem +" at " + timeItem, "Give me the size " + inventoryItem + " that were " + attributeItem +" at " + timeItem, "Give me the quantity of " + inventoryItem + " that were " + attributeItem +" at " + timeItem]
            timeItem = monthTime + str(day) + ", 2021"
            data += "\n" + questions[question]
            print(questions[question])
  with open("intent4.txt", "w") as f:
    f.write(data)
def cat5():
  data = ""
  x = ""
  y = ""
  z = ""
  questions = ["How many " + x + " occured on " + y + " at " + z, "Which " + y + " did the " + x + " occur on at " + z, "Tell me the number of "  + x + " that occured on " + y + " at" + z, "Show me how many " + x + " happened to the " + y + " at " + z, "Report to me how many " + x + " happened to " + y + " at " + z, "Display the" + y + " which " + x + " happened to at " + z]
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for timeItem in timeStamp:
          questions = ["How many " + attributeItem + " occured on " + inventoryItem + " at " + timeItem, "Which " + inventoryItem + " did the " + attributeItem + " occur on at " + timeItem, "Tell me the number of "  + attributeItem + " that occured on " + inventoryItem + " at" + timeItem, "Show me how many " + attributeItem + " happened to the " + inventoryItem + " at " + timeItem, "Report to me how many " + attributeItem + " happened to " + inventoryItem + " at " + timeItem, "Display the " + inventoryItem + " which " + attributeItem + " happened to at " + timeItem]
          data += "\n" + questions[question]
          print(questions[question])
  for question in range(len(questions)):
    for inventoryItem in inventory:
      for attributeItem in attribute:
        for monthTime in month:
          for day in range(1,31):
            questions = ["How many " + attributeItem + " occured on " + inventoryItem + " at " + timeItem, "Which " + inventoryItem + " did the " + attributeItem + " occur on at " + timeItem, "Tell me the number of "  + attributeItem + " that occured on " + inventoryItem + " at" + timeItem, "Show me how many " + attributeItem + " happened to the " + inventoryItem + " at " + timeItem, "Report to me how many " + attributeItem + " happened to " + inventoryItem + " at " + timeItem, "Display the " + inventoryItem + " which " + attributeItem + " happened to at " + timeItem]
            timeItem = monthTime + str(day) + ", 2021"
            data += "\n" + questions[question]
            print(questions[question])
  with open("intent5.txt", "w") as f:
    f.write(data)
cat1()
cat2()
cat3()
cat4()
cat5()