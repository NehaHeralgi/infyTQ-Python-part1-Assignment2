#FoodCorner home delivers vegetarian and non-vegetarian combos to its customer based on order.
#A vegetarian combo costs Rs.120 per plate and a non-vegetarian combo costs Rs.150 per plate. Their non-veg combo is really famous that they get more orders for their non-vegetarian combo than the vegetarian combo.
#Apart from the cost per plate of food, customers are also charged for home delivery based on the distance in kms from the restaurant to the delivery point. The delivery charges are as mentioned below:
#Distance in kms
#Delivery charge in Rs per km
#For first 3kms
#0
#For next 3kms
#3
#For the remaining
#6
#Given the type of food, quantity (no. of plates) and the distance in kms from the restaurant to the delivery point, write a python program to calculate the final bill amount to be paid by a customer. 
#The below information must be used to check the validity of the data provided by the customer: 
#Type of food must be ‘V’ for vegetarian and ‘N’ for non-vegetarian.
#Distance in kms must be greater than 0.
#Quantity ordered should be minimum 1.
#If any of the input is invalid, the bill amount should be considered as -1.
#lex_auth_012693782475948032141

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):

   bill_amount=0

   if(food_type=="V" or "N" and quantity_ordered>0 and distance_in_kms>0):

       if(distance_in_kms<=3):

           travel_fee=0

       elif(distance_in_kms>3 and distance_in_kms<=6):

           travel_fee=3*(distance_in_kms-3)

       else:

           travel_fee=6*(distance_in_kms-6)+9

       

       if(food_type=="V"):

           bill_amount=120*quantity_ordered+travel_fee

       elif(food_type=="N"):

           bill_amount=150*quantity_ordered+travel_fee

       else:

           bill_amount=-1

       

   else:

       bill_amount=-1

       

   return bill_amount


bill_amount=calculate_bill_amount("N",-1,7.0)

print(bill_amount)