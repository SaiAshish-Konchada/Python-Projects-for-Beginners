# importing the required library
from pyshorteners import Shortener

# passing instance
s = Shortener()
# asking user for choice
choice = int(input("Enter 1 for link shortener and 2 for link expander: "))


# link shortener
def short():
    link = input("Enter the link to be shortened: ")
    shortened_link = s.tinyurl.short(link)
    print(" The Shortened Link is: " + shortened_link)


# link expander
def expand():
    link = input("Enter the link to be expanded: ")
    expanded_link = s.tinyurl.expand(link)
    print("The Expanded link is: " + expanded_link)


if choice == 1:
    short()
elif choice == 2:
    expand()
else:
    print("Wrong Entry. Please try again.")
