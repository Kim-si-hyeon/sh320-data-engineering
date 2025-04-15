#데이터프로그래밍 과제2

#%% 
print("hw2-1 : Recipts for Lovely Loveseats (가구판매점 영수증)")

lovely_loveseat_description = ("Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.")
lovely_loveseat_price = 254.00

stylish_settee_description = ("Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.")
stylish_settee_price = 180.50

luxurious_lamp_description = ("Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.")
luxurious_lamp_price = 52.15

sales_tax = .088 


customer_one_total = 0
customer_one_itemization =""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total +=luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_total += sales_tax

print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total: ")
print(customer_one_total)


#%% 
print("hw2-2 : Gradebooks (성적표)")

subjects = ["physics","calculus","poetry","history"]
grades = [98,97,85,88]

gradebook = [
    [subjects[0], grades[0]],
    [subjects[1], grades[1]],
    [subjects[2], grades[2]],
    [subjects[3], grades[3]]
]
print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)

gradebook[5][1] +=5
gradebook.remove(["poetry", 85])
gradebook.append(["poetry", "Pass"])
print(gradebook)

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)




#%%
print("hw2-3 : Carly's Clippers (칼리의 가위)")

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
    total_price += price

average_price = total_price / len(prices)

print("Average price is ",average_price)

new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print(total_revenue)
average_daily_revenue = total_revenue/7
print("Average daily revenue is",average_daily_revenue)

cuts_under_30 = [ hairstyles[i] for i in range(len(new_prices)) if new_prices[i]<30]
print(cuts_under_30)
    

#%%
print("hw2-4 : 나의 조선시대 이름 찾기")

month_lst = ['쌍', '쇠', '복', '돌', '팽', '육', '쌍', '개', '칠', '갑', '삼', '방']
print(month_lst)

day_lst = ['봉', '구', '욕', '포', '똥', '삼', '식', '석', '놈', '님', '년', '돌', '단', '득', '방', '질', '장', '걸', '래', '룡', '동', '순', '자', '박', '창', '언', '것', '포', '만', '단', '국']
print(day_lst)

def get_my_chosun_name(family_name,month,day):
    month_index = month_lst[month-1]
    day_index = day_lst[day-1]
    chosun_name = family_name + month_index + day_index
    return chosun_name
    
print("당신의 조선시대 이름은",get_my_chosun_name('안',9,18),"입니다.")