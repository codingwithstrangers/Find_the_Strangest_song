import json
  
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

def loop(list, value):
    index = 0
    start = 0
    for x in list:
        new_number = x.get(value)
        index += 1
        start += new_number
    
    math = start / index
    Math = float(math)

    return {
      'amount': index,
      'result': start,
      'math': Math
    }



bars = data.get('bars')
beats = data.get('beats')
tatums = data.get('tatums')

#this will pull bars start info
tatstart =  loop(tatums, 'start').get('math')

#this will pull bars duration info
tatdur = loop(tatums, 'duration').get('math')

#this will pull bars confidence info
tatcon = loop(tatums, 'confidence').get('math')

# #this will pull beats start info
# beatstart = loop(beats, 'start').get('match')

# #this will pull beats duration info
# beatdur = loop(beats, 'duration').get('match')

# #this will pull beats confidence info
# beatcon = loop(beats, 'confidence').get('match')


print(tatstart, tatdur, tatcon)



