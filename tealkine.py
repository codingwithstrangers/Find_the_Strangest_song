
from main import access_token
import requests
import json
from pprint import pprint


def main():
    seed_artists = "4NHQUGzhtTLFvgF5SZesLK,3RNrq3jvMZxD9ZyoOZbQOD,6XyY86QOPPrYVGvF9ch6wz,3nFkdlSjzX9mRTtwJOzDYB"

    track_info = get_track_recommendations(limit = 3, seed_artists=seed_artists)

    for track in track_info:
        pprint("track_id: " + track["id"])
    
        for artist in track["artists"]:
            pprint("artists_id: " + artist["id"])
 

def get_track_recommendations(limit:int = 3, seed_artists: list[str])
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    #for all known ranges, best for using with genre and artist
    seed_genres=""
    seed_tracks = ""
    target_tempo = ".50"
    target_danceability = ".050"
    target_liveness = ".50"
    target_popularity = "1"
    target_acousticness = ".50"
    target_energy = ".50"
    target_instrumentalness = ".50"
    target_key = "1"
    target_speechiness = ".50"
    target_valence = ".50"

    endpoint_url = "https://api.spotify.com/v1/recommendations"
    
    query_params = {
        "limit": limit,
        "seed_genres": seed_genres,
        "seed_tracks": seed_tracks,
        "seed_artists": seed_artists,
        "target_tempo": target_tempo,
        "target_danceability": target_danceability,
        "target_liveness": target_liveness,
        "target_popularity": target_popularity,
        "target_acousticness": target_acousticness,
        "target_energy": target_energy,
        "target_instrumentalness": target_instrumentalness,
        "target_key": target_key,
        "target_speechiness": target_speechiness,
        "target_valence": target_valence,
    }


    # print(query)
    result = requests.get(query, params=query_params, headers=headers)

    result_content = json.loads(result.content)
    # pprint.pprint(result_content, compact=True)

    return result_content["tracks"]


# Note sure what this is supposed to do but eh...
# seed_artists = "4NHQUGzhtTLFvgF5SZesLK,3RNrq3jvMZxD9ZyoOZbQOD,6XyY86QOPPrYVGvF9ch6wz,3nFkdlSjzX9mRTtwJOzDYB"
def get_prama(limit: int = 1, seed_artists: list[str]):
    seed_genres=""
    seed_tracks = ""
    max_acousticness = ".50"
    min_acousticness = ".25"
    max_danceability = ".50"
    min_danceability = ".25"

    endpoint_url = "https://api.spotify.com/v1/recommendations?"
    prama = f'{endpoint_url}limit={limit}&seed_genres={seed_genres}&seed_tracks={seed_tracks}&seed_artists={seed_artists}'
    prama += f'&max_acousticness={max_acousticness}'
    prama += f'&min_acousticness={min_acousticness}'
    prama += f'&max_danceability={max_acousticness}'
    prama += f'&min_danceability={min_acousticness}'


    min_max_result = requests.get(prama,headers=headers)

    min_max_result_content = json.loads(min_max_result.content)


if __name__ == "__main__":
    main()