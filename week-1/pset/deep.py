response = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

response = response.lower()
correct_responses = ["42", "forty-two", "forty two"]

correct = False
i = 0
while i < 3:
    if response == correct_responses[i]:
        print("Yes")
        correct = True
        break
    i += 1 

if correct != True:
    print("No")