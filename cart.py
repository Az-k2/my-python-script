cart = {
    "apple" : 5, "banana" : 8, "orange" : 2
}

print(cart["banana"])

if cart["apple"] <= 9:
print("you need more apple")
print(f"your apple is {
    cart["apple"]}")
elif cart["banana"] <= 5:
print("you have too much banana")
print(f"your banana is {
    cart["banana"]}")
elif cart["orange"] <= 3:
print("you need more orange")
print(f"your orange is {
    cart["orange"]}")
print(f"this is all in your cart : {
    cart
}")