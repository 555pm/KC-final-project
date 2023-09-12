#hope you enjoy my project <3

p1_name, p1_price = 'One shot espresso', 1.350
p2_name, p2_price = 'iced pumpkin latte', 2.200
p3_name, p3_price = 'iced matcha latte', 1.950
p4_name, p4_price = 'monkey bread', 1.250
p5_name, p5_price = 'turkey & cheese supreme pretzel', 1.450
p6_name, p6_price = 'strawberry cheesecake', 1.850
p7_name, p7_price = 'Mug 12 oz marbled pumpkin', 5.000

company_name = "starbucks"
company_adress = "trolley -petrol station, hussein bin ali al-roomi road, salmia"
company_city = "Kuwait"
time_of_chk = "5:55 PM"
date = "Mon 11.9.2023"

#ending message
messeage = 'Thank you for shoping at starbucks see you soon Sarah'

print('*'*50)

print("\t\t\{}".format(company_name.title()))
print("\t\t{}".format(company_adress))
print("\t\t{}".format(company_city))
print("\t\t{}".format(time_of_chk))
print("\t\t{}".format(date))

print("*"*50)
print("\t product name \t product price")

print("\t{}\t\tkd{}".format(p1_name.title(), p1_price))
print("\t{}\t\tkd{}".format(p2_name.title(), p2_price))
print("\t{}\t\tkd{}".format(p3_name.title(), p3_price))
print("\t{}\t\tkd{}".format(p4_name.title(), p4_price))
print("\t{}\t\tkd{}".format(p5_name.title(), p5_price))
print("\t{}\t\tkd{}".format(p6_name.title(), p6_price))
print("\t{}\t\tkd{}".format(p7_name.title(), p7_price))

print("="*50)

print("\t\t\t total")

total = p1_price + p2_price + p3_price + p4_price + p5_price + p6_price + p7_price
print("\t\t\tkd{}".format(total))

print("="*50)

print("\n\t{}\n".format(messeage))

print("*"*50)