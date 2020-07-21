import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# inspect the DataFrames using print and head
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

# combine visits and cart
visits_cart = pd.merge(visits, cart, how='left')
print(visits_cart.head())

# percentage of users who visited the website but didn't place a t-shirt in their cart
cart_null = visits_cart[visits_cart.cart_time.isnull()]
per_not_cart = (float(len(cart_null)) / len(visits_cart)) * 100
print(per_not_cart)
# 80.5% of users did not proceed to card after visiting

# combine cart and checkout
cart_checkout = pd.merge(cart, checkout, how='left')

# percentage of users who put items in their cart, but did not proceed to checkout
cart_checkout_null = cart_checkout[cart_checkout.checkout_time.isnull()]
per_not_checkout = (float(len(cart_checkout_null)) / len(cart_checkout)) * 100
print(per_not_checkout)
# 20.9% of users who put item in their cart did not proceed to checkout

# combine checkout and purchase
checkout_purchase = pd.merge(checkout, purchase, how='left')

# percentage of users who proceeded to checkout, but did not purchase a t-shirt
checkout_purchase_null = checkout_purchase[checkout_purchase.purchase_time.isnull()]
per_not_purchase = (float(len(checkout_purchase_null)) / len(checkout_purchase)) * 100
print(per_not_purchase)
# 16.9% of users who proceeded to checkout did not purchase a t-shirt

# the weakest step of the funnel seems to be step 2, 'a user adds a t-shirt to their cart'. This step has the highest percentage of users not proceeding after the previous step (80.5%) 

# combine all four steps of the funnel
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head())

# calculate the average time from initial visit to final purchase
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
# the average visit time is around 44 minutes
