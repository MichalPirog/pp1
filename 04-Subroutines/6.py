# Define a function that displays numbers in the layout as below (like on a phone keypad). Apply an loop statement. Then call the function.

def keyboard():
   for x in range(1,8,3):
    print(f"{x} {x+1} {x+2}")

keyboard()
        