# Make a list of the numbers from one to one million,
# and then the use nim() and max() functions to make
# sure your list actually starts at one and ends at one
# million. Also, use the sum() function to see how quickly
# Python can add a million numbers.

one_million = []

for value in range(1, 1000001):
    one_million.append(value)

print(min(one_million))
print(max(one_million))
print(sum(one_million))
