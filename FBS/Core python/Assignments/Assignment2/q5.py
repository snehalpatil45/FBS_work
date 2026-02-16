# wap to calculate selling price of book based on cost price and discount.

cost_price = int(input("Enter cost price of book:"))
discount = int(input("Enter discount of book:"))
discount_amount = (discount / 100) * cost_price
selling_price = cost_price - discount 
print("Selling price of book:",selling_price)