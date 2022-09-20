text = input("Greeting: ")
response = text.lower().strip()

if response.startswith("hello"):
    print("$0")
elif response.startswith("h"):
    print("$20")
else:
    print("$100")