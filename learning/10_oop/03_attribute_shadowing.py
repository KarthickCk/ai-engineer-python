class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()

cutting.temperature = "mild"
cutting.cup = "small"

del cutting.cup
print(cutting.cup)