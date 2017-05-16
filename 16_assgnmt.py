"""
16. Take the input from the user for(Total number of people, toatl number
of busses, Number of seats for bus). Based on the input
Deside whether there is sufficient busses or not and
give solution for how many extra busses required.
"""
people=input("Enter the number of people")
bus=input("Enter the number of buses")
seats=input("Enter the number of seats in one bus")
total_seats=bus*seats
x=0
print "Total seats are:",total_seats
if total_seats<people:
    x=people-(total_seats)
    
print "Required Seats x:",x
if x == 0:
    print "No buses required"
elif x<=seats:
    print "one bus required"
    
elif x>seats:
    y=float(x)/float(seats)
    if y.is_integer():
        
        print "Required buses y:",y
    else:
        print "Required buses are y:",int(y+1)
    
