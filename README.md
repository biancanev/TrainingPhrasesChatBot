# Cisco AI Chatbox Phrase Generator
### Overview:
This program generates tagged phrases for a network-technical chatbox. It can generate 5 categories of phrases:

| Category | Use |
| --- | --- |
| 1 | Creates a phrase that gives all the `inventory` with `attribute` at a certain `time` |
| 2 | Creates a phrase that gives all `attribute` an `inventory` had at `time` |
| 3 | Creates a phrase that shows the `time` an `inventory` had `attribute` |
| 4 | Creates a phrase that shows how many `inventory` had `attribute` at `time` |
| 5 | Creates a phrase that shows the `time` an `inventory` had `attribute` |


This can be achieved through the use of a single function
### Function and Parameters:
This program uses the function `genQuestions(category1, category2, category3, category4, category5, objectParam, objectList, dateType)`. Below is a description of each parameter:

| Parameter | Use |
| --- | --- |
| `category1`(int) | Determines how many `Category 1` phrases the generator should generate. Default is `0`.|
| `category2`(int) | Determines how many `Category 2` phrases the generator should generate. Default is `0`.|
| `category3`(int) | Determines how many `Category 3` phrases the generator should generate. Default is `0`.|
| `category4`(int) | Determines how many `Category 4` phrases the generator should generate. Default is `0`.|
| `category5`(int) | Determines how many `Category 5` phrases the generator should generate. Default is `0`.|
| `objectParam`(str) | Determines whether the program should include `objects` during generation. Acceptable parameters include: `"none"`, `""random"`, and `"given"`. `"none"` will not use objects when generating phrases. `"random"` will call the function `genObjects()` and generate a random string for an object 20% of the time. The rest will be a normal output with no object. `"given"` will iterate through the given list in `objectList` to create a unique phrase. Default is `"random"`|
| `objectList`(tup) | If `objectParam` is `"given"`, the generator will iterate through the given list in category n given `(n, [])`. Default is `(0, [])`.|
| `dateType`(int) | Sets the format of dates used in generating times. `1` is MM/DD/YYYY. `2` is DD/MM/YYYY. `3` is YYYY/MM/DD. `4` is MM DD, YYYY. Default is `4` |

Therefore this code:
```python
genQuestions(cat1=1, cat3=1, objectParam="given", objectList=(1,["VM1"]))
```
will output something like:
```
Category 1 Phrases:
What are the {VMs|class|primary} correlated to {VM1|object|secondary} in {deleted|modification|attribute} at {April 21, 2021|time}?

Category 3 Phrases:
Were there any times when {security groups|class|primary} pertaining to {sec_group3} had {faults|modification|attribute}
```