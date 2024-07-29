from main import access_token
import requests
import json
import pprint


def main():
    limit = 3
    seed_artists = "6XyY86QOPPrYVGvF9ch6wz"
    

    get_recommended_tracks(limit, seed_artists)


def get_recommended_tracks(limit, seed_artists):
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    #for all known ranges, best for using with genre and artist
    seed_genres="alternative metal, rap metal, nu metal "
    seed_tracks = ""
    target_tempo = "135.095"
    target_danceability = "0.554"
    target_liveness = "0.0731"
    target_popularity = "75"
    target_acousticness = ".315"
    target_energy = ".524"
    target_instrumentalness = "0"
    target_key = "1"
    target_speechiness = ".0351"
    target_valence = ".246"

    endpoint_url = "https://api.spotify.com/v1/recommendations?"
    query = f'{endpoint_url}limit={limit}&seed_genres={seed_genres}&seed_tracks={seed_tracks}&seed_artists={seed_artists}'
    query += f'&target_tempo={target_tempo}'
    query += f'&target_danceability={target_danceability}'
    query += f'&target_liveness={target_liveness}'
    query += f'&target_popularity={target_popularity}'
    query += f'&target_acousticness={target_acousticness}'
    query += f'&target_energy={target_energy}'
    query += f'&target_instrumentalness={target_instrumentalness}'
    query += f'&target_key={target_key}'
    query += f'&target_speechiness={target_speechiness}'
    query += f'&target_valence={target_valence}'


    # print(query)
    result = requests.get(query, headers=headers)

    result_content = json.loads(result.content)
    pprint.pprint(result_content, compact=True)

    tracks = []


    # For each track in results
    for track in result_content["tracks"]:
        track_id = track["id"]

        artist_ids = []

        for artist in track["artists"]:
            artist_ids.append(artist["id"])
    
        tracks.append(
            {
                "track_id": track_id, 
                "artist_id": artist_ids
            }
        )

    return tracks


