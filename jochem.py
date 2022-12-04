import json

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list


# getbars
bars = data.get('beats')



new_index = 0
start = 0


# get the fist dict
for x in bars:
    new_number = x.get('duration')
    new_index += 1
    start += new_number


result = start / new_index



print(f"Beat count: {new_index}")
print(f"totals beats: {start}")
print(f"result: {result}")


# get the fitst start


# Closing file
f.close()



  
    


