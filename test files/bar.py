from email import contentmanager
import json
import numpy
from test import r.content
  
r_content = json.loads(r.content)

  
# returns JSON object as 
# a dictionary
data = r_content

  
# Iterating through the json
# list

#getbars
beats = data.get('beats')
new_index = 0
starts = 0

for item in beats:
    new_index += 1
    beats = item.get("beats")
    beatstart = item.get("start")
    starts += beatstart
    #print(new_index, duration, bars)

print ("%3d items in beats" % new_index)
print ("Total of %3d duration" % starts)

# print(starts / new_index)


#now do it for duration
beats = data.get('beats')
new_indexdur = 0
startsdur = 0

for item in beats:
    new_indexdur += 1
    beats = item.get("beats")
    beatdur = item.get("duration")
    startsdur += beatdur
    #print(new_index, duration, bars)

print ("%3d items in duration" % new_indexdur)
print ("Total of %3d duration" % startsdur)



#now do it for conidence

beats = data.get('beats')
new_indexcon = 0
startscon = 0

for item in beats:
    new_indexcon += 1
    beats = item.get("beats")
    beatcon = item.get("confidence")
    startscon += beatcon
    #print(new_index, duration, bars)

print ("%3d items in duration" % new_indexcon)
print ("Total of %3d duration" % startscon)
# print(startsdur / new_index)
# print(startscon / new_index)

print(starts / new_index , startsdur / new_indexdur, startscon / new_indexcon)



