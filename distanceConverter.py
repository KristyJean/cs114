"""Distance converter """
"""Convert a distance in miles to kilometers."""

# 1. Setup
kilometers_per_mile = 1.60934
miles_per_kilometers = 0.621371


# 2. Input
print('Please enter the distance in number form only')
distance = float(input())

print('Please enter known unit (ie: Kilometers or Miles)')
unit = input()
if unit == 'miles':
    kilometers = kilometers_per_mile * distance
    print('If you go ' + str(distance) + ' ' + str(unit) + ' you traveled ' + str(kilometers) + ' in kilometers.')
else
    kilometers = miles_per_kilometers * distance
    rint('If you go ' + str(distance) + ' ' + str(unit) + ' you traveled ' + str(kilometers) + ' in miles.')
