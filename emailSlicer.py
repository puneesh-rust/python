email = input("email")
index = email.index("@")

username = email[:index]

domain = email[index+1:]

print(f"your username is {username} and domain is {domain}")

# format specifier are the flag of the code ex.
# print(f"add number{num: 2f})  after : we used format specifier nf is used for digit after decimal 
## format specifiers = {value:flags} format a value based on what
#                     flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
