#Generates a phrase dataset for an AI powered chatbot
#In addition to generating different phrases and categories, this program also labels and separates the output by intent
import random

inventory = ["VMs", "security groups", "NICs", "route tables", "rules", "networks", "CIDRs", "subnets", "subscriptions", "resource groups"]
attribute = ["location", "status", "utilization", "events", "faults", "cost", "created", "deleted"]
timeStamp = ["yesterday", "last week", "last month"]
month = ["January", "February", "March"]
#Category 1: Inventory with Attribute at Time
def genObject(length):
  name = ""
  lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  for letter in range(length):
    case =  random.randint(1,2)
    if case == 1:
      name += lower[random.randint(0, 25)]
    elif case == 2:
      name += upper[random.randint(0, 25)]
  return name
def cat1(number, *objectParam):
  data = []
  inventoryItem = inventory[random.randint(0, len(inventory)-1)]
  attributeItem = attribute[random.randint(0, len(inventory)-1)]
  objectItem = ""
  timeItem = "Jan 1, 2021"
  nonObjectQuestions = ["What are the {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|time}?", "Can I see the {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modification|attribute} at {" + timeItem + "?", "Show me all of {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}.", "Give me information on {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}.", "I need information on {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}.", "Access all {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}.", "Find all {" + inventoryItem + "|class|primary}  in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}." , "I want all {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}.", "I want to see all {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}.", "Can I access {" + inventoryItem + "|class|primary}  in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}?", "Open information on {" + inventoryItem + "|class|primary}  in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}.", "Send me information on {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}.", "Report information on {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}.", "Give me information on {" + inventoryItem + "|class|primary}  in {" + attributeItem + "|modification|attribute} at {" + timeItem + "|sys_time}.", "I want information on {" + inventoryItem + "|class|primary} in {" + attributeItem + "|modification|primary} at " + timeItem + "|sys_time}.", "Give me all {" + attributeItem + "|modification|attribute} {" + inventoryItem + "|class|primary} at " + timeItem + "|sys_time}.", "Access all {" + attributeItem + "|modification|attribute} {" + inventoryItem + "|class|primary} at " + timeItem + "|sys_time}.", "I want information on {" + attributeItem + "|modification|attribute} {" + inventoryItem + "|class|primary} at " + timeItem + ".", "Find all {" + attributeItem + "|modification|attribute} {" + inventoryItem + "|class|primary} at " + timeItem + "|sys_time}."]
  objectQuestions = ["Give me the {" + attributeItem + "|modification|attribute} of the {" + inventoryItem + "|class|primary} that were associated to {" + objectItem + "|object|secondary} {" + timeItem + "}"]
  if objectParam == None:
    for iteration in range(number):
      data.append(nonObjectQuestions[random.randint(0, len(nonObjectQuestions)-1)])
    return data
  elif objectParam == "random":
    for iteration in range(number):
      objectItem = genObject(random.randint(5, 12))
      for iteration in range(number):
        data.append(objectQuestions[random.randint(0,len(objectQuestions)-1)])

  else:
    pass
#Category 2: Attribute of Inventory at Time
def cat2(number):
  data = []
  inventoryItem = inventory[random.randint(0, len(inventory)-1)]
  attributeItem = attribute[random.randint(0, len(inventory)-1)]
  timeItem = "Jan 1, 2021"
  questions = ["Show me the {" + attributeItem + "|modification|attribute} of {" + inventoryItem + "|class|primary} at {" + timeItem + "|sys_time}" + "?", "{" + attributeItem + "|modification|attribute} of {" + inventoryItem + "|class|primary} at {" + timeItem + "|sys_time}", "What is {" + attributeItem + "|modification|attribute} of {" + inventoryItem + "|class|primary} at {" + timeItem + "|sys_time}" + "?", "Show {" + attributeItem + "|modification|attribute} of {" + inventoryItem + "|class|primary} at {" + timeItem + "|sys_time}", "Which ones have {" + attributeItem + "|modification|attribute} of {" + inventoryItem + "|class|primary} at {" + timeItem + "|sys_time}", "Give me the {" + attributeItem + "|modification|attribute} of {" + inventoryItem + "|class|primary} at {" + timeItem + "|sys_time}", "Are there any {" + attributeItem + "|modification|attribute} of {" + inventoryItem + "|class|primary} at {" + timeItem + "|sys_time}", "Show the {"  + attributeItem + "|modification|attribute} of {" + inventoryItem + "|class|primary} at {" + timeItem + "|sys_time}"]
  for iteration in range(number):
    data.append(questions[random.randint(0, len(questions)-1)])
  return data
#Category 3: Time Inventory had Attribute
def cat3(number, objectParam):
  data = []
  inventoryItem = inventory[random.randint(0, len(inventory)-1)]
  attributeItem = attribute[random.randint(0, len(inventory)-1)]
  timeItem = "Jan 1, 2021"
  questions = ["When did {" + inventoryItem + "|class|primary} have {" + attributeItem + "|modification|attribute}", "What time did {" + inventoryItem + "|class|primary} have {" + attributeItem + "|modification|attribute}", "Give me a time when {" + inventoryItem + "|class|primary} had {" + attributeItem + "|modification|attribute}", "What times did {" + inventoryItem + "|class|primary} have {" + attributeItem + "|modification|attribute}", "At what time did {" + inventoryItem + "|class|primary} have {" + attributeItem + "|modification|attribute}", "Give me time when {" + inventoryItem + "|class|primary} had {" + attributeItem + "|modification|attribute}", "Were there any times when {" + inventoryItem + "|class|primary} had {" + attributeItem + "|modification|attribute}"]
  for iteration in range(number):
    data.append(questions[random.randint(0, len(questions)-1)])
  return data
#Category 4: How many Inventory have Attribute at Time
def cat4(number):
  data = []
  inventoryItem = inventory[random.randint(0, len(inventory)-1)]
  attributeItem = attribute[random.randint(0, len(inventory)-1)]
  timeItem = "Jan 1, 2021"
  questions = ["How many {" + inventoryItem + "|class|primary} were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "How much {" + inventoryItem + "|class|primary} were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "What number of {" + inventoryItem + "|class|primary} were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "How many {" + inventoryItem + "|class|primary} were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "Give me the number of {" + inventoryItem + "|class|primary} that were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "Give me the amount of {" + inventoryItem + "|class|primary} that were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "What amount of {" + inventoryItem + "|class|primary} were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "What is the size of {" + inventoryItem + "|class|primary} were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "What volume of {" + inventoryItem + "|class|primary} were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "What quantity of {" + inventoryItem + "|class|primary} were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "Give me the volume of {" + inventoryItem + "|class|primary} that were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "Give me the size of {" + inventoryItem + "|class|primary} that were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}", "Give me the quantity of {" + inventoryItem + "|class|primary} that were {" + attributeItem +"|modification|attribute} at {" + timeItem+ "|sys_time}"]
  for iteration in range(number):
    data.append(questions[random.randint(0, len(questions)-1)])
  return data
def cat5(number):
  data = []
  inventoryItem = inventory[random.randint(0, len(inventory)-1)]
  attributeItem = attribute[random.randint(0, len(inventory)-1)]
  timeItem = "Jan 1, 2021"
  questions = ["How many {" + attributeItem + " |modification|attribute} occured on {" + inventoryItem + "|class|primary} at {" + timeItem + "|sys_time}", "Which {" + inventoryItem + "|class|primary}did the {" + attributeItem + "|modification|attribute} occur on at {" + timeItem + "|sys_time}", "Tell me the number of {"  + attributeItem + "|modification|attribute} that occured on {" + inventoryItem + "|class|primary} at {" + timeItem + "|sys_time}", "Show me how many {" + attributeItem + "|modification|attribute} happened to the {" + inventoryItem + "|class|primary} at {" + timeItem + "|sys_time}", "Report to me how many {" + attributeItem + "|modification|attribute} happened to {" + inventoryItem + " |class|primary} at {" + timeItem + "|sys_time}", "Display the {" + inventoryItem + "|class|primary} which {" + attributeItem + "|modification|attribute} happened to at {" + timeItem + "|sys_time}"]
  for iteration in range(number):
    data.append(questions[random.randint(0, len(questions)-1)])
  return data
def genQuestions(**parameters):
  objectParam = "random"#is currently set as a vriable to fix bug, will be set as an actual parameter later
  for parameter in parameters:
    if parameter == "cat1":
      print("Category 1 Questions:")
      for phrase in cat1(parameters.get(parameter), objectParam):
        print(phrase)
    elif parameter == "cat2":
      print("Category 2 Questions:")
      for phrase in cat2(parameters.get(parameter), objectParam):
        print(phrase)
    elif parameter == "cat3":
      print("Category 3 Questions:")
      for phrase in cat3(parameters.get(parameter), objectParam):
        print(phrase)
    elif parameter == "cat4":
      print("Category 4 Questions:")
      for phrase in cat4(parameters.get(parameter), objectParam):
        print(phrase)
    elif parameter == "cat5":
      print("Category 5 Questions:")
      for phrase in cat1(parameters.get(parameter)), objectParam:
        print(phrase)
    else:
      print("Parameter " + parameter + " is not recognized")
      return None
genQuestions(cat3=4)