import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 29th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Sai', 'Ashish','Ansul', 'Steve', 'Tony']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened) +".")
