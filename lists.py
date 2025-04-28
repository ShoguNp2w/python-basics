#list of prices
prices = [10, 20, 30, 15, 25, 35]

print(type(prices))
print(type("hello"))

print(prices[0])
print(prices[3])
print(prices[5])

#last element
print(prices[-1])

#second and third element
print(prices[1:3])

#all elements from 4th index
print(prices[3:])

#first three elements
print(prices[:3])

#access every other element
print(prices[::2])

#access every third element starting from second
print(prices[1::3])

playlist = [1, "Blinding lights", "the weekend", 2, "one dance", "drake", 3, "uptown funk", "mark ronson", 4, "closer", "the chainsmokers", 5, "one kiss", 'calvin harris', 6, "mr brightside", "the killers"]

#find second song
print(playlist[4])

#find last song
print(playlist[-1])

#get all songs
print(playlist[1::3])
