# Problem 1:
# Given two points, the formula for computing the distance is [(𝑥2 − 𝑥1)**2 + (𝑦2 − 𝑦1)**2]**0.5
# you can use a ** 0.5 to compute √𝑎 . The program should prompts the user to enter two points and computes the distance between them.
x1 = float(input("Enter the x-cordinate of the first point(x1): "))
x2 = float(input("Enter the x-cordinate of the first point(x2): "))
y1 = float(input("Enter the x-cordinate of the first point(y1): "))
y2 = float(input("Enter the x-cordinate of the first point(y2): "))

# Calculate the difference in x-coordinates
x_difference = x2 - x1
# Calculate the difference in y-coordinates
y_difference = y2 - y1

# Square the differences
x_diff_square = x_difference ** 2
y_diff_square = y_difference ** 2

# Add the squared differences
sum_of_squares = x_diff_square + y_diff_square

#  Compute the square root of the sum of squares to get the distance.
distance = sum_of_squares ** 0.5

# Displaying the result.
print(f"The distance between the two points is: {distance:.2f}")
