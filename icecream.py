'''ice cream blender'''
#may have to press "run without debugging for it to work (top left under "Run")

prompt = "\nEnter your favorite icecream toppings."
prompt += "\nEnter 'quit' when you are finished. "

toppings = []
while True:
    choice = input(prompt)
    toppings.append(choice)
    if choice.lower() == "quit":
        toppings.remove("quit")
        print(f"Amazing! your blizzard of {toppings} is done")
        break
    else:
        print(f"good choice, you have {toppings} so far")