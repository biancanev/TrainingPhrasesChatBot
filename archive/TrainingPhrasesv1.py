#Base code for generating a list of phrases for training
limit = 20
y = ""
z = ""
questions = ["What are the " + y + "in" + z + "?", "Can I see the" + y + " in " + z + "?", "Show me all of " + y + "in " + z + ".", "Give me information on " + y + "in " + z + ".", "I need information on" + y + " in " + z +".", "Access all" + y + " in " + z + ".", "Find all" + y + " in " + z + "." , "I want all" + y + " in " + z + ".", "I want to see all" + y + " in " + z + ".", "Can I access" + y + " in " + z + "?", "Open information on" + y + " in " + z + "."]

for a in range(0, len(questions)):
    for b in range(0, limit):
        y = " VM" + str(b + 1)
        for x in range(0, limit):
            z = " location" + str(x + 1)
            questions = ["What are the " + y + "in" + z + "?", "Can I see the" + y + " in " + z + "?", "Show me all of " + y + "in " + z + ".", "Give me information on " + y + "in " + z + ".", "I need information on" + y + " in " + z +".", "Access all" + y + " in " + z + ".", "Find all" + y + " in " + z + "." , "I want all" + y + " in " + z + ".", "I want to see all" + y + " in " + z + ".", "Can I access" + y + " in " + z + "?", "Open information on" + y + " in " + z + "."]
            with open("output.txt", "a") as f:
              f.write('\n')
              f.write(questions[a - 1])
            print(questions[a])