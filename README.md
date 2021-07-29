# Cisco AI Chatbox Phrase Generator
### Overview:
This program generates tagged phrases for a network-technical chatbox. It can generate 5 categories of phrases:

| Category | Use |
| --- | --- |
| 1 | Creates a phrase that gives all the `inventory` with `attribute` at a certain `time` |
| 2 | Creates a phrase that gives all `attribute` an `inventory` had at `time` |
| 3 | Creates a phrase that shows the `time` an `inventory` had `attribute` |
| 4 | Creates a phrase that shows how many `inventory` had `attribute` at `time` |
| 5 | Creates a phrase that shows how many `attribute` an `inventory` had at `time` |


This can be achieved through the use of a single function
### Function and Parameters:
This program uses the function `genQuestions(category1, category2, category3, category4, category5, objectParam, objectList, dateType)`. Currently, it is located on line 141. Below is a description of each parameter:

| Parameter | Use |
| --- | --- |
| `category1`(int) | Determines how many `Category 1` phrases the generator should generate. Default is `0`.|
| `category2`(int) | Determines how many `Category 2` phrases the generator should generate. Default is `0`.|
| `category3`(int) | Determines how many `Category 3` phrases the generator should generate. Default is `0`.|
| `category4`(int) | Determines how many `Category 4` phrases the generator should generate. Default is `0`.|
| `category5`(int) | Determines how many `Category 5` phrases the generator should generate. Default is `0`.|
| `objectParam`(str) | Determines whether the program should include `objects` during generation. Acceptable parameters include: `"none"`, `""random"`, and `"given"`. `"none"` will not use objects when generating phrases. `"random"` will call the function `genObjects()` and generate a random string for an object 20% of the time. The rest will be a normal output with no object. `"given"` will iterate through the given list in `objectList` to create a unique phrase. Default is `"random"`|
| `objectList`(tup) | If `objectParam` is `"given"`, the generator will iterate through the given list in category n given `(n, [])`. Default is `(0, [])`.|
| `dateType`(int) | Sets the format of dates used in generating times. `1` is MM/DD/YYYY. `2` is DD/MM/YYYY. `3` is YYYY/MM/DD. `4` is MM DD, YYYY. `5` chooses a random selection of all the previous dateTypes. Default is `5`. |

Therefore this code:
```python
>>>main.py

genQuestions(category1=3, category3=1 ,objectParam="random", dateType=3)
```
will output something like:
```
Category 1 Questions:
Show me the {faults|modification|attribute} of the {security groups|class|primary} pertaining to {THLJyapgnQ|object|secondary} on {2021/1/19}
Find all {faults|modification|attribute} {security groups|class|primary} at 2021/1/19|sys_time}.
Access all {faults|modification|attribute} {security groups|class|primary} at 2021/1/19|sys_time}.
Category 3 Questions:
At what time did {rules|class|primary} have {events|modification|attribute}
```

In addition to printing out the phrases, the generator also returns the phrases in a list. If you want to save the information to a text file, you may do as such:
```python
>>>main.py

with open("file.txt","a") as f:
  f.write(genQuestions(category1=3, category3=1 ,objectParam="random", dateType=3))
```
which will generate the file `file.txt` as such:
```
>>>file.txt

['Show me the {faults|modification|attribute} of the {security groups|class|primary} pertaining to {THLJyapgnQ|object|secondary} on {2021/1/19}', 'Find all {faults|modification|attribute} {security groups|class|primary} at 2021/1/19|sys_time}.', 'Access all {faults|modification|attribute} {security groups|class|primary} at 2021/1/19|sys_time}.', 'At what time did {rules|class|primary} have {events|modification|attribute}']
```