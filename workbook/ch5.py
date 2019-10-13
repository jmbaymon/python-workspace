# # 2

# a = 10 
# b = 4

# print("%d - %d = %d" %(a,b, a-b))

# #3
# print("{} - {} = {}".format(a,b,a-b))

# #5 
# print( 'This (\') mark and this (\")')

# #6
# print('Travel Itinerary')
# day =[0 ,'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
# venue = [0 ,'Tokyo to Osaka', 'Osaka', 'Kyoto', 'Kyoto to Nara','Nara to Osaka','Osaka to Tokyo', 'Tokyo']

# print('Day 1 (%s): %s' %(day[1], venue[1]))
# print('Day 2 (%s): %s' %(day[2], venue[2]))
# print('Day 3 (%s): %s' %(day[3], venue[3]))
# print('Day 4 (%s): %s' %(day[4], venue[4]))
# print('Day 5 (%s): %s' %(day[5], venue[5]))
# print('Day 6 (%s): %s' %(day[6], venue[6]))
# print('Day 7 (%s): %s' %(day[7], venue[7]))

# #7
# num1 = input(" Enter an integer: ")
# num2 = input(" Enter another integer: ")

# print ('You entered {} and {}'.format(num1,num2))

#8

# in1 = input(" Enter a number: ")
# in2 = input(" Enter another number: ")

# in1 = int(in1)
# in2 = int(in2)

# #Calculate Average

# average = (in1 + in2)/2
# print("The average is %s" %(average))

#10

print('Chicago', 'Los Angeles' , 'New York', 'Osaka', 'Tokyo', 'Shanghai', 'Moscow', 'Paris', 'London', 'Seoul')
city_country = {'Chicago': 'United States(USA)', 'Los Angeles':'United States(USA)', 'New York': 'USA', ' Osaka': 'Japan', 'Tokyo': 'Japan', 'Shanghai': 'China', 'Moscow': 'Russia', 'Paris': 'France', 'London':'England', 'Seoul':'Korea'}

city = input('Enter a City: ')

country = city_country.get(city)
print(country) 

