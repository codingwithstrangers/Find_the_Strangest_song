import json
  
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data_beat = json.load(f)

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



bars = data_beat.get('bars')
beats = data_beat.get('beats')
tatums = data_beat.get('tatums')

# #this will pull bars start info
# barstart =  loop(bars, 'start').get('math')

# #this will pull bars duration info
# bardur = loop(bars, 'duration').get('math')

# #this will pull bars confidence info
# barcon = loop(bars, 'confidence').get('math')

#this will pull beats start info
beatstart = loop(beats, 'start').get('math')

#this will pull beats duration info
beatdur = loop(beats, 'duration').get('math')

#this will pull beats confidence info
beatcon = loop(beats, 'confidence').get('math')


print(beatstart, beatdur, beatcon)



