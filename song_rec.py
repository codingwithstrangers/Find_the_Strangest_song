import json
import requests
import csv
from main import access_token

def main():
    track_id = "6qc34bnVOyqGDPni8H5W0U"  # Replace with your track ID
    track_detail = get_details(track_id)

    print('Track Details:', track_detail)
    
    rec_export(input_dicts=[track_detail], export_filename="song_rec_export.csv")
    print('Task_done')

def get_details(track_id):
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    BASE_URL = 'https://api.spotify.com/v1/'

    t = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
    h = requests.get(BASE_URL + 'tracks/' + track_id, headers=headers)

    t_content = json.loads(t.content)
    h_content = json.loads(h.content)
   
    track_id_info = {
        "song_name" : h_content.get('name'),
        "spotify_track_id" : h_content.get('id', 'NA'),
        "album_name" : h_content.get('album').get('name', 'NA'),
        "http_status_code" : f'{t.status_code}{h.status_code}',
        "popularity_track" : h_content.get('popularity', 'NA'),
        "album_release_date" : h_content.get('album').get('release_date', 'NA'),
        "total_tracks" : h_content.get('album').get('total_tracks', 'NA'),
        'duration_min' : h_content.get('duration_ms', 'NA')//1000/60,
        'BPM' : t_content.get('tempo'),
        'danceability' : t_content.get('danceability', 'NA'), 
        'energy' : t_content.get('energy', 'NA'),
        'loudness' : t_content.get('loudness', 'NA'),
        'mode' : t_content.get('mode', 'NA'),
        'speechiness' : t_content.get('speechiness', 'NA'),
        'acousticness' : t_content.get('acousticness', 'NA'),
        'instrumentalness' : t_content.get('instrumentalness', 'NA'),
        'liveness' : t_content.get('liveness', 'NA'),
        'valence' : t_content.get('valence', 'NA'),
        'time_signature' : t_content.get('time_signature', 'NA')
    }

    # Loop for finding all featured artists and placing them in place holders in track_id_info dict
    artistft = h_content.get('artists')
    count = 0
    for artist in artistft:
        track_id_info[f"spotify_artists_name_{count}"] = artist['name']
        track_id_info[f"spotify_artist_id_{count}"] = artist['id']
        count += 1

    return track_id_info

def rec_export(input_dicts, export_filename):
    keys = input_dicts[0].keys() if input_dicts else []
    
    with open(export_filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(input_dicts)
    
    print("csv done")

if __name__ == "__main__":
    main()
