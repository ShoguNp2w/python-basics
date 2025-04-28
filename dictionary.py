#create dictionary
productS_dict = {"AG32":10, "HT91":20, 
                 "PL65":30, "OS31":15, "KB07":25, "TR48":35}

#find value
print(productS_dict["AG32"])

#find all values
print(productS_dict.values())

#find all keys
print(productS_dict.keys())

#get all items
print(productS_dict.items())

#add new key value pair
productS_dict["UI56"] = 40

#update value
productS_dict["HT91"] = 12

print(productS_dict.items())

playlist1 = [1, "Blinding Lights", "The Weeknd", 2, "One Dance", "Drake", 
 3, "Uptown Funk", "Mark Ronson", 4, "Closer", "The Chainsmokers",
 5, "One Kiss", "Calvin Harris", 6, "Mr. Brightside", "The Killers"]

playlist = {"The Weeknd":"Blinding Lights", "Drake":"One Dance"}

print(playlist)


print(playlist["The Weeknd"])

playlist["USher"] = "YEah!"

print(playlist.values())



