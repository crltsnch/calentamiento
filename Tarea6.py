shipping_cost_per_kg = 1.20
customer_basket_cost = 34
customer_basket_weight = 44
if(customer_basket_cost >= 100):
    shipping_cost = 0
else:
    shipping_cost = customer_basket_weight * shipping_cost_per_kg
customer_cost = shipping_cost + customer_basket_cost
print("total basket cost including shipping is " + str(customer_cost))

#Al ejecutar el código sale: 86.8
#Al ejecutar el código sale: total basket cost including shipping is 101