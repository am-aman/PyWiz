date = input("Enter Date (DD/MM/YYYY)")
date_list = date.split("/")

if 0 < int(date_list[0]) and int(date_list[0]) < 32:
    if  0 < int(date_list[1]) and int(date_list[1]) < 13:
        pass
    else:
        print("invalid Month")
else:
    print("invalid date")

print("valid date !")


date = int(date_list[0])
month_code = {1 : 1, 2 :4 ,  3 :4 ,  4 :0 ,  5 :2 ,  6 :5 ,  7 :0 , 8 :3 ,  9 :6 ,  10 :1 ,  11 :4 ,  12 :6 }
day_code = {0 : "Saturday" ,1 : "Sunday", 2 : "Monday" ,  3 :"Tuesday" ,  4 :"Wednesday" ,  5 :"Thursday" ,  6 :"Friday" }
month = month_code[int(date_list[1])]
print(month)
year = int(date_list[2][-2:])
extra_digit_for_year = int(year) // 4


if date_list[2][-2:] == "00":
    if (int(date_list[2]) % 400 == 0) :
        print("its a leap year")
        if date_list[1] == "01":
            month = 0
        elif date_list[1] == "02":
            month = 3
        else:
            print("its a leap year , but not jan and feb , so go on !")
    else: 
        print("not a leap year ")
elif date_list[2][-2:]!= "00":
    if (int(date_list[2]) % 4 == 0):
        print("its a leap year !")
        if date_list[1] == "01":
            month = 0
        elif date_list[1] == "02":
            month = 3
        else:
            print("its a leap year , but not jan and feb , so go on !")
    else:
        print("its not a leap year")

# print(f"{date} + {month}")


final = date + month + year + extra_digit_for_year
print(f"final ={date} + {month} + {year} + {extra_digit_for_year}")

if date_list[2][:2] == "20":
    final = final - 1 

answer =  final % 7

print(f"Its {day_code[answer]}")




