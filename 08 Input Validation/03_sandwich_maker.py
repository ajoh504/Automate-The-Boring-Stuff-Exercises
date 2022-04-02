import pyinputplus as pyip

while True:
    # append user input to sandwich_choices
    sandwich_choices = []
    bread = pyip.inputMenu(["wheat", "white", "sourdough"])
    sandwich_choices.append(bread)
    protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"])
    sandwich_choices.append(protein)
    want_cheese = pyip.inputYesNo("Do you want cheese?")
    if want_cheese == "yes":
        cheese = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"])
        sandwich_choices.append(cheese)
    mayo = pyip.inputYesNo("Do you want mayo?")
    if mayo == "yes":
        sandwich_choices.append(mayo)
    mustard = pyip.inputYesNo("Do you want mustard?")
    if mustard == "yes":
        sandwich_choices.append(mustard)
    lettuce = pyip.inputYesNo("Do you want lettuce?")
    if lettuce == "yes":
        sandwich_choices.append(lettuce)
    tomato = pyip.inputYesNo("Do you want tomato?")
    if tomato == "yes":
        sandwich_choices.append(tomato)
    sandwich_num = pyip.inputInt(
        "How many of these sandwiches do you want?", greaterThan=0
    )
    break

# cost based on number of choices
# base sandwich is $5.99. Every additional topping is $0.10
print(sandwich_choices)
cost = 5.99
extras = 0
if len(sandwich_choices) > 2:
    extras = (len(sandwich_choices) - 2) * 0.10 # multiply toppings by 10 cents
    cost += extras # add toppings charge to base cost
    cost *= sandwich_num
    cost = round(cost, 2) # round up to the hundredth decimal
print('Your total is $' + str(cost))
