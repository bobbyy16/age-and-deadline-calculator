import datetime
def dead():

    user_input=input("enter your goal with a deadline by colon \n")
    input_list=user_input.split(":")

    goal =input_list[0]
    deadline=input_list[1]

    deadline_date=datetime.datetime.strptime(deadline, "%d.%m.%Y")
    today_date= datetime.datetime.today()
    time_till=deadline_date-today_date
    print(f"Dear user! Time remaining for your goal : {goal} is {time_till.days} days")

def birth():
    user_input = input("enter your birth date  \n")
    bday_date = datetime.datetime.strptime(user_input, "%d.%m.%Y")
    today_date = datetime.datetime.today()
    time_done =  today_date-bday_date
    years=time_done/365
    # arr=years.split(" ")
    # remaing=time_done%365
    # print(remaing)
    # print(years)
    print(f"Dear user! The days from your birth are : {time_done.days} and you r {years.days} years old")