# [How to Build an Alarm Clock Using Python]()
![](https://github.com/SaiAshish-Konchada/Python-Projects-for-Beginners/blob/main/Alarm%20Clock/Alarm%20Clock.jpg)

[Blog: Step by Step Guide]():
==========================
You can find a step by step walkthrough in my [Blog]()
<br>

What will be covered in this Blog?
==========================
```
1. The Datetime Module
2. The Playsound Module
3. Basics of Python: Conditional Statements, Iterative Statements & Slicing a string 
4. Implementation of Your Very Own Alarm Clock
```
## What is the Datetime Module?

A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

Example: 
Import the datetime module and display the current date:

```
import datetime

x = datetime.datetime.now()
print(x)
```

When we run the above code snippet, we obtain the output as:

```
2021-01-21 00:01:15.165663
```

The date contains year, month, day, hour, minute, second, and microsecond.

You can access the official documentation of the Datetime module from [here](https://docs.python.org/3/library/datetime.html) to know more about it. 

## What is the Playsound module?

[Playsound](https://pypi.org/project/playsound/) is a pure Python, cross-platform, single function module with no dependencies for playing sounds. In other words, you can play a sound with just a single line of code. 

[Playsound](https://pypi.org/project/playsound/) is not available by default in the [Python Standard Library](https://docs.python.org/3/py-modindex.html) and has to be installed. To do this, we will use pip, the standard package manager for Python. All you've to do is, go the and terminal and run:

```
pip install playsound
```
That's it! You, now have the Playsound module in your system. Next, we are going to see an example on how to import the Playsound module and the single line of magic code that runs your audio file!

```
from playsound import playsound 
playsound('/path/to/a/sound/file/you/want/to/play.mp3')
```
## Basics of Python:

### Conditional Statement: if
If statement is a conditional statement that runs on the logic that if a certain condition is true, it will run the code inside the if block else it will run the other block. A simple implementation of the same is seen below:

```
a = 33
b = 200
if b > a:
  print("b is greater than a")

#output
b is greater than a
```
Try the above code [here](https://www.w3schools.com/python/trypython.asp?filename=demo_if2).

You can also have multiple if-else statements and also an if statement inside an if statement. This is known as the [Nested if- structure](https://www.w3schools.com/python/python_conditions.asp).

### Iterative statement: while
The [while loop](https://www.w3schools.com/python/python_while_loops.asp) repeats a set of statements repeatedly until the condition becomes false.

```
i = 1
while i < 6:
  print(i)
  i += 1

Output:
1
2
3
4
5
```
Try the above code [here](https://www.w3schools.com/python/trypython.asp?filename=demo_while).

LICENSE:
==========================
Copyright (c) 2021 The Insightful Coder

This project is licensed under the MIT License.
<p align="center">
  <b><i>Let's connect! Choose your favorite platform and say Hi  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="20px"></i></b>

[<img height="30" src = "https://img.shields.io/github/followers/SaiAshish-Konchada?label=Follow&style=social">](GitHub) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img height="30" src="https://img.shields.io/badge/Hashnode-%230077B5.svg?&style=for-the-badge&logo=Hashnode&logoColor=white" />](https://theinsightfulcoder.hashnode.dev/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="mailto:saiashishkonchada@gmail.com" style="text-decoration:none"><img height="30" src = "https://img.shields.io/badge/gmail-c14438?&style=for-the-badge&logo=gmail&logoColor=white"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[<img height="30" src="https://img.shields.io/badge/linkedin-blue.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/sai-ashish/)
<br />

<hr />

 If you have any Queries or Suggestions, feel free to reach out to me.

<h3 align="center">Show some &nbsp;❤️&nbsp; by starring some of the repositories!</h3>
