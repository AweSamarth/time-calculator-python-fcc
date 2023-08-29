# add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

# add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

def add_time(start, duration, theDay=""):
    extra_days=0
    array_of_days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    new_time=""
    # print(start, duration)

    slightly_broken=start.split(":")
    hours=int(slightly_broken[0])
    min_meridian=slightly_broken[1].split(" ")
    minutes=int(min_meridian[0])
    meridian=min_meridian[1]

    if(meridian=="PM" and hours<12):
        hours+=12

    add_hours = int(duration.split(":")[0])
    add_minutes = int(duration.split(":")[1])


    # print()
    hours+=add_hours
    minutes+=add_minutes

    hours+=(minutes//60)
    extra_days=hours//24
    hours%=24
    minutes%=60

    if(hours>=12):
        meridian="PM"
        hours-=12
    else:
        meridian="AM"
    hours=str(hours)
    minutes=str(minutes)

    if(len(minutes)==1):
        minutes="0"+minutes
    if(hours=="0"):
        hours="12"
    # print("hello")
    new_time+=hours+":"+minutes+" "+meridian
    # print(new_time)    

    
    if(theDay!=""):
        new_time+=", "+ array_of_days[(array_of_days.index(theDay.capitalize())+extra_days)%7]
        
    if(extra_days==1):
        new_time+=" (next day)"
    if(extra_days>1):
        new_time+= " ("+str(extra_days)+" days later)"

    # print(new_time)

    return new_time

# print(add_time("11:43 PM", "48:23", "saturday"))
print(add_time("3:30 PM", "2:12"))