# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:slice]

#name = "Bro Code"

#first_name = name[0:3]
#last_name = name[4:]
#funcky_name = name[::2]
#reversed_name = name[::-1]

#print(first_name)      # [0:3]
#print(last_name)       # [4:end]
#print(funcky_name)     # [0:end:2]
#print (reversed_name)  # [0:end:-1]

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
