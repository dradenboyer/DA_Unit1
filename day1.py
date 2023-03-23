menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """
welcome = "Welcome to the programming diary!"

user_input = input(menu)
while user_input := input(menu) != "3":
    if user_input == "1":
        print("Adding...")
    elif user_input == "2":
            print("Viewing...")
    else:
        print("Invalid option, please try again!")
    user_input = input(menu)

# bit.io queries 
# SELECT * FROM invoices 
# JOIN customers
# ON invoices.customer_id = customers.id

# SELECT * FROM invoices JOIN
# customers ON invoices.customer_id = customers.id
# WHERE invoices.product_category = 'Outdoors';

# SELECT * FROM invoices JOIN
# customers ON invoices.customer_id = customers.id
# WHERE invoices.product_category = 'Garden';

# SELECT product_category, SUM(unit_price*quantity) FROM invoices
# GROUP BY product_category
# ORDER BY SUM DESC;