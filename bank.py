x = input("Greeting: ")
x = x.strip().lower()

if "hello" in x:
    print("$0")
elif x.startswith("h") and x!="hello":
    print("$20")
else:
    print("$100")