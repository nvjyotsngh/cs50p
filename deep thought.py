user_input = input("What is the Great Question of Life, the Universe and Everything??").lower()

right_answer = "42", "forty-two", "forty two"

if user_input in right_answer:
    print("yes")
else:
    print("no")