# without data

wifi_name = ""

wifi_password = ""

print(len(wifi_name))     # output :0
print(len(wifi_password)) # output :0

# with data

wifi_name = "Bhaskar"

wifi_password = "23456789"

print(len(wifi_name))       # output: 7

print(len(wifi_password))   # output: 8


# Declare the variables

wifi_name_length = len( wifi_name)
wifi_password_length = len( wifi_password )

print( wifi_name_length )
print( wifi_password_length )

# concatnation

first_name = "shiva"
last_name = "nanda"

print( first_name + last_name )         # ShivaNanda

print( first_name + " " + last_name )   # Shiva Nanda

print( "Mr. " + first_name + " " + last_name ) # Mr. Shiva Nanda

full_name = "Mr. " + first_name + " " + last_name

print( full_name )

# f string

emp_name = "murali"

emp_salary = "100000"

#  murali employee salary is Rs. 100000
# print( emp_name + " employee salary is Rs. " + emp_salary )


print ( f"Hi {first_name}, {emp_name} employee salary is Rs. {emp_salary}" )

query = f"select * from wifi where name= '{wifi_name}' and password='{wifi_password}';"

print( query )

first_name = first_name.upper()

print ( first_name )

token_number = "ASDFG1234"

token_number = token_number.lower()


print( token_number )














