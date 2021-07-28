# Cisco AI Chatbox Phrase Generator
### Overview:
This program generates tagged phrases for a network-technical chatbox. It can generate 5 categories of phrases:

| Category | Use |
| --- | --- |
| `cat1` | Creates a phrase that gives all the `inventory` with `attribute` at a certain `time` |
| `cat2` | Creates a phrase that gives all `attribute` an `inventory` had at `time` |
| `cat3` | Creates a phrase that shows the `time` an `inventory` had `attribute` |
| `cat4` | Creates a phrase that shows how many `inventory` `objects` had `attribute` at `time` |
| `cat5` | Creates a phrase that shows the `time` an `inventory` had `attribute` |


This can be achieved through the use of a single function
### Function and Parameters:
This program uses the function `genQuestions(objects, **cat1, **cat2, **cat3, **cat4, **cat5)`. Below is a description of each parameter:

| Parameter | Use |
| --- | --- |
| `objects` | Determines whether the program should include `objects` during generation. Acceptable parameters include: `None`, `"random"`, and a `list`. `None` will not use objects when generating phrases. `"random"` will call the function `genObjects()` and generate a random string for an object. Using a `list` will iterate through the given list of objects to create a unique phrase.|
| `**cat1` | Determines how many `cat1` phrases the generator should generate. This is a kwarg.|
| `**cat2` | Determines how many `cat1` phrases the generator should generate. This is a kwarg.|
| `**cat1` | Determines how many `cat1` phrases the generator should generate. This is a kwarg.|
| `**cat1` | Determines how many `cat1` phrases the generator should generate. This is a kwarg.|
| `**cat1` | Determines how many `cat1` phrases the generator should generate. This is a kwarg.|
Therefore this code:
```python
genQuestions(None, cat1=1, cat3=1)
```
will output something like:
```
Category 1 Phrases:
What are the {VMs|class|primary} in {deleted|modification|attribute} at {April 21, 2021|time}?

Category 3 Phrases:
Were there any times when {security groups|class|primary} had {faults|modification|attribute}
```