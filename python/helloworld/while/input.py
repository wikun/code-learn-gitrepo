message = input("tell me something ,and i will repeat it: ")
print(message)

prompt = "if you tell us who you are, we can personalize the message you see."
prompt += "\nwhat is your first name? "
name = input(prompt)
print(f"\nhello,{name}")