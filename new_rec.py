
from operator import length_hint
from unicodedata import name
from main import access_token
import requests
import json
import xlsxwriter
import csv
import os
import pprint
import export
import rec


def main():
    tracks = rec.get_recommended_tracks(3, '6XyY86QOPPrYVGvF9ch6wz') #number will populate tracks plus artist

    track_details = []
    count = 0
    for track in tracks:
      
        #update this so I can get all logic and artist
        # track_detail = get_details(track["track_id"], track["artist_ids"][0])
        if len(track["artist_id"]) > 1:
           
            for artist_ids in track["artist_id"]:
              

                track_detail = get_details(track["track_id"], artist_ids)

                track_details.append(track_detail)
        else:
            track_detail = get_details(track["track_id"], track["artist_id"][0])
            track_details.append(track_detail)
            # test_export = export._export_to_csv(input_dict=track_details, export_filename="Rec1_export.csv")

    pprint.pprint(track_details, sort_dicts=False)
      
    for track in track_details:

        test_export = export._export_to_csv(input_dict=track, export_filename="F:\Coding with Strangers\\bestsongever-main\\bestsongever-main\\Rec_export.csv")


def get_details(track_id, artist_id):
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'
    endpoint_url = "https://api.spotify.com/v1/recommendations?"


    # actual GET request with proper header as of now you need to make one for each stat
    t = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
    r = requests.get(BASE_URL + 'audio-analysis/' + track_id, headers=headers)
    h = requests.get(BASE_URL + 'tracks/' + track_id, headers=headers)
    s = requests.get(BASE_URL + 'artists/'+ artist_id, headers=headers)
    

    t_content = json.loads(t.content)
    h_content = json.loads(h.content)
    r_content = json.loads(r.content)
    s_content = json.loads(s.content)
    # pprint.pprint(h_content)
    #print(s_content.get('genres'))

    #My Big DICt. 
    data = r_content

    def loop(input_list:list, value):
        index = 0
        start = 0
        for x in input_list:
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



    #you have 2 choices here loop it all to do less
    #or print each one seen below
    track_id_info = {
        
    "spotify_artists_name_0" : 'NA',
    "spotify_artists_name_1" : 'NA',
    "spotify_artists_name_2" : 'NA',
    "spotify_artist_id_0" : 'NA',
    "spotify_artist_id_1" : 'NA',
    "spotify_artist_id_2" : 'NA',
    "song_name" : h_content.get('name'),
    "spotify_track_id" : h_content.get('id', 'NA'),
    "album_name" : h_content.get('album').get('name', 'NA'),
    "http_status_code" : f'{t.status_code}{h.status_code}',
    "genre_1" :'NA',
    "genre_2" :'NA',
    "genre_3" :'NA',
    "genre_4" :'NA',
    "genre_5" :'NA',
    "genre_6" :'NA',
    "genre_7" :'NA',
    "genre_8" :'NA',
    "genre_9" :'NA',
    "genre_10" :'NA',
    "popularity_track" : h_content.get('popularity', 'NA'),
    "popularity_artist" : s_content.get('popularity', 'NA'),
    "album_release_date" : h_content.get('album').get('release_date', 'NA'),
    "total_tracks" : h_content.get('album').get('total_tracks', 'NA'),
    'duration_min' : h_content.get('duration_ms', 'NA')//1000/60,
    'BPM' : t_content.get('tempo'),
    'danceability' : t_content.get('danceability', 'NA') , 
    'energy' : t_content.get('energy', 'NA'),
    'loudness' : t_content.get('loudness', 'NA'),
    'mode' : t_content.get('mode', 'NA'),
    'speechiness' : t_content.get('speechiness', 'NA'),
    'acousticness' : t_content.get('acousticness', 'NA'),
    'instrumentalness' : t_content.get('instrumentalness', 'NA'),
    'liveness' : t_content.get('liveness', 'NA'),
    'valence' : t_content.get('valence', 'NA'),
    'time_signature' : t_content.get('time_signature', 'NA'),
    'time_signature_confidence' : r_content.get('track').get('time_signature_confidence', 'NA'),
    'end_of_fade_in' : r_content.get('track').get('end_of_fade_in', 'NA'),
    'start_of_fade_out' : r_content.get('track').get('start_of_fade_out', 'NA'),
    'tempo_confidence' : r_content.get('track').get('tempo_confidence', 'NA'),
    'mode_confidence' : r_content.get('track').get('mode_confidence', 'NA'),
    'key_confidence' : r_content.get('track').get('key_confidence', 'NA'),
    'beat_start' :  loop(r_content.get('beats'), 'start').get('math', 'NA'),
    'beat_duration' :  loop(r_content.get('beats'), 'duration').get('math', 'NA'),
    'beat_confidence' :  loop(r_content.get('beats'), 'confidence').get('math', 'NA'),
    'beats_length' : len(r_content.get('beats', 'NA')),
    'tatum_start' :  loop(r_content.get('tatums'), 'start').get('math', 'NA'),
    'tatum_duration' :  loop(r_content.get('tatums'), 'duration').get('math', 'NA'),
    'tatum_confidence' :  loop(r_content.get('tatums'), 'confidence').get('math', 'NA'),
    'tatum_length' : len(r_content.get('tatums', 'NA')),
    'bars_start' :  loop(r_content.get('bars'), 'start').get('math', 'NA'),
    'bars_duration' :  loop(r_content.get('bars'), 'duration').get('math', 'NA'),
    'bars_confidence' :  loop(r_content.get('bars'), 'confidence').get('math', 'NA'),
    'bars_length' : len(r_content.get('bars', 'NA')),
    }

    
    #loop for finding all genres and placing them in plce holders in track_id_info DICt.
    songtype = s_content.get('genres')

    for genre_position, genre_value in enumerate(songtype, start=1):
        track_id_info[f"genre_{genre_position}"] = genre_value


    #loop for finding all ft artist and placing them in plce holders in track_id_info DICt.
    artistft =  h_content.get('artists')
    count = 0
    for artist in artistft:
        track_id_info[f"spotify_artists_name_{count}"] = artist['name']
        count+=1

    #loop for finding all ft artist and placing them in plce holders in track_id_info DICt.
    artistid =  h_content.get('artists')
    count = 0
    for newartistid in artistid:
        track_id_info[f"spotify_artist_id_{count}"] = newartistid['id']
        count+=1


    return track_id_info



if __name__ == "__main__":
    main()

    #print(test_export)

    # data_list=list(track_id_info.items())
    # print(data_list)
    # returns JSON object as 
    # a dictionary

    #bars = data.get('bars')
    #beats = data.get('beats')
    #tatums = data.get('tatums')

    ##this will pull bars start info
    #beatstart =  loop(beats, 'start').get('math')

    ##this will pull bars duration info
    #beatdur = loop(beats, 'duration').get('math')

    ##this will pull bars confidence info
    #beatcon = loop(beats, 'confidence').get('math')

    ##this will pull bars start info
    #tatstart =  loop(tatums, 'start').get('math')

    ##this will pull bars duration info
    #tatdur = loop(tatums, 'duration').get('math')

    ##this will pull bars confidence info
    #tatcon = loop(tatums, 'confidence').get('math')

    ##this will pull bars start info
    #barstart =  loop(bars, 'start').get('math')

    ##this will pull bars duration info
    #bardur = loop(bars, 'duration').get('math')

    ##this will pull bars confidence info
    #barcon = loop(bars, 'confidence').get('math')


    


## time_signature = estimated time signature for beats per measure
## mode = 1 is major 0 is minor
## Key Guide = The key the track is in. Integers map to pitches
## using standard Pitch Class notation.
## E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
##