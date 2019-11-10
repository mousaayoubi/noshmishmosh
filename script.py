import noshmishmosh
import numpy as np

#Get website visitors
all_visitors = (noshmishmosh.customer_visits)
print(all_visitors)

#Get buying customers
paying_customers = (noshmishmosh.purchasing_customers)
print(paying_customers)

#Get number website visitors
total_visitor_count = len(noshmishmosh.customer_visits)
print(total_visitor_count)

#Get number of buying customers
paying_visitor_count = len(noshmishmosh.purchasing_customers)
print(paying_visitor_count)

#Calculate coversion rate
baseline_percent = (paying_visitor_count*100.0)/total_visitor_count
print(baseline_percent)

#Get customer payment history
payment_history = noshmishmosh.money_spent
print(payment_history)

#Get average payment size
average_payment = np.mean(payment_history)
print(average_payment)

new_customers_needed = np.ceil(1240/average_payment)
print(new_customers_needed)

#Calculate percentage point increase
percentage_point_increase = (new_customers_needed*100.0)/total_visitor_count
print(percentage_point_increase)

#Calculate minimum detectable effect
minimum_detectable_effect = (percentage_point_increase/baseline_percent)*100.0
print(minimum_detectable_effect)

#Get sample size for a 90% statstical significance, 19% coversion rate and minimum detectable effect of 51%
ab_sample_size = 290
print(ab_sample_size)