#regexes
# \d stands for digits
# \d{3} means match the pattern three times

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My number is 478-432-5643')

print("Phone number found: " + mo.group())


#More Patterns Matching 
#Adding parentheses will create groups in the regex.
# EX: (\d\d\d)-(\d\d\d-\d\d\d\d)
# first set is group 1
# second set is group 2

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('My number is 478-432-5643')

#Entire phone number
mo.group(0)
mo.group()
#Area code
mo.group(1)
#Part numbers
mo.group(2)

#Shows groups in a list 
mo.groups()

#Multiple Groups with pipe

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search ('Batman and Tina Fey')
mo2 = heroRegex.search ('Tina Fey and Batman')
mo1.group()
mo2.group()

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel.Get the Batcopter')
mo3.group()
mo3.group(1)

#Optional Matching with The Question Mark

batRegex2 = re.compile(r'Bat(wo)?man')
mo4 = batRegex2.search('The Adventures of Batman')
mo4.group()

mo5 = batRegex2.search('The Adventures of Batwoman')
mo5.group()

# matching zero or more with the Star
batRegex3 = re.compile(r'Bat(wo)*man')
mo6 = batRegex3.search('The Adventures of Batman')

mo6.group()

mo7 = batRegex3.search('The Adventures of Batwoman')

mo7.group()

mo8 = batRegex3.search('The Adventures of Batwowowowowoman')

mo8.group()

#Matching One or More with the Plus

batRegex4 = re.compile(r'Bat(wo)+man')

mo9 = batRegex4.search('The Adventures of Batwoman')
mo9.group()

mo10 = batRegex4.search('The Adventures of Batwowowowwowman')
mo10.group()


mo11 = batRegex4.search('The Adventures of Batman')
mo11 == None