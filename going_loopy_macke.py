# Create a loop that prints even numbers until it reaches your year of age or, if your age is an odd number, 
# prints out odd numbers until it reaches your age.
# Create a list containing five different sandwich ingredients. 
# Then, create a loop that prints out the list (including the numbers)
# If you were standing on the moon right now, your weight would be 16.5 percent of what it is on Earth. 
# You can calculate that by multiplying your Earth weight by 0.165.  If you gained a kilo in weight every year for the next 15 years, 
# what would your weight be when you visited the moon each year and at the end of the 15 years? 
# Write a program using a for loop that prints your moon weight for each year.

"""
print("\n\nCounting backwards:")
for i in range(14, 0, 2):
     print(i, end=" ")

Ingretints = [" 1st Bred" " 2nd ham", "3rd cheses", " 4th doritos"] 
   print(ingretints)
    print('done')
"""
weight = 130
for year in range(1,16):
    weight = weight + 1 
    moon_weight = weight * 0.165
    print(f"year {year} is {moon_weight}")
