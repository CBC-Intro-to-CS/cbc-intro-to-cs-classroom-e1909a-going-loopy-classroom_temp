for x in range(2, 16, 2): 
    print(x)



x = 1 
results = ["Turkey", "Cheese", "Mustard", "Mayonnaise", "Tomatoes"]
for i in results:
    print(f"{x} {i}")
    x = x + 1


weight = 160 
for year in range(1, 16):
    weight = weight + 1 
    moon_weight = weight * 0.165 
    print(f"Year {year} is {moon_weight}")