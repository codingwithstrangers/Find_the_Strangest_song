<div id="header" align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjAyMXphYmdkeWhsZjdzNWIyMjg0MGt5N3Rxd3dvZnFjZ2NuZXExMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/jvOHlU7qhcnsEGuTQZ/giphy.gif" width="150"/>
</div>

<p align="center">
  <img src="https://i.imgur.com/WXl2vPq.jpg" alt="Image Description" width="600"/>
</p>

# Find The Strangest Song

This project provides a Python script that interacts with the Spotify API to achieve two main objectives:

1. **Fetch Detailed Track Information**: Given a specific track ID, the script retrieves detailed information about the track, including audio features, album details, and artist information.
2. **Get Similar Tracks**: Using the details of the specified track, the script fetches up to 100 tracks that are similar to it. The data retrieved is then exported into a CSV file for further analysis or use.

<pre align="center">
----------------------------------------------------
</pre>

This script is a great way to find new songs and set parameters that can remove duplicates. You can only pull 100 songs at a time, and the song data can be calculated to the exact point.

### Why Did I Do This?

A YouTube contact reached out after seeing me demo this on stream and asked if I could randomly select songs based on emotions.

### How Users Can Use This

**For Programmers:**
- **Requirements:**
  - Python 3.x
  - Spotify Developer Account
  - Spotify API Access Token

**Features:**
- Fetch the detailed information of the specified track.
- Retrieve up to 100 tracks similar to the specified track.
- Export the data to a CSV file named `song_rec_export.csv` in the project directory.

**CSV File Output:**
After running the script, a CSV file (`song_rec_export.csv`) will be generated with the following columns:

- `song_name`
- `spotify_track_id`
- `album_name`
- `http_status_code`
- `popularity_track`
- `album_release_date`
- `total_tracks`
- `duration_min`
- `BPM`
- `danceability`
- `energy`
- `loudness`
- `mode`
- `speechiness`
- `acousticness`
- `instrumentalness`
- `liveness`
- `valence`
- `time_signature`
- `spotify_artists_name_0`
- `spotify_artist_id_0` (and more, depending on the number of artists and genres)
- Similar Track Columns: Data for each of the similar tracks retrieved

1. **How the Data Works**
   - You can manipulate data to find new songs and try to build the most unskippable playlist.
   - CSV data can be stored elsewhere to make tables or pivots.

### Need Help?

[![Twitter Follow](https://img.shields.io/badge/Twitter-Follow%20%40strangestcoder-1DA1F2?style=for-the-badge&logo=twitter)](https://x.com/strangestcoder)

[![Twitch Status](https://img.shields.io/badge/Twitch-Live%20Codingwithstrangers-9146FF?style=for-the-badge&logo=twitch)](https://www.twitch.tv/codingwithstrangers)

### Who is Doing This

Coding with Strangers, aka Heero.

### Features

**Summary:**
- Fetch the info from a single artist or song (genres can be used, but currently, that functionality is limited).
- Use the song or artist data to build a playlist or analyze song characteristics.
- Break down the data on the song using numerical values.

### What You Will Need

**Files Included:**
- `main.py` – Configuration for tokens.
- `new_rec.py` – Generate new song recommendations.
- `song_rec.py` – Fetch original song data.
- `Rec_export.csv` - List of songs.
- Note: Many other files need to be cleaned up as they were used for testing.

### Prerequisites

Before running the project, ensure you have the following:
- Python 3.10.16
- Godot installed (if applicable).
- Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create an application to get your access token.
- Run `pip install -r requirements.txt`.
- Install the `requests` package with `pip install requests`.

### Bugs

List of all known bugs:

- [ ] **Token Expiration Handling**: The script doesn't handle token expiration, which may cause API requests to fail after the token expires.
- [ ] **Error Handling for API Requests**: The script doesn't include proper error handling for API requests. If the Spotify API fails or returns an error (e.g., 404 or 500), the script may crash or produce incorrect output.
- [ ] **Handling of Missing Data**: The script assumes all data fields are present in the API response. If any field is missing (e.g., `popularity`, `tempo`), the script might raise a KeyError.
- [ ] **Rate Limiting**: The script doesn’t account for Spotify's API rate limiting. Making too many requests in a short period may lead to the API blocking further requests.
- [ ] **CSV Export Handling**: The script overwrites the existing CSV file every time it runs, which might result in data loss. Consider appending data or using a unique filename.
- [ ] **Hardcoded File Paths**: The script uses hardcoded file paths for exporting data (e.g., `F:\\Coding with Strangers\\bestsongever-main\\find_song\\Rec_export.csv`). This could cause issues on different systems or environments.
- [ ] **Track Duration Calculation**: The `duration_min` field calculation (`h_content.get('duration_ms', 'NA')//1000/60`) may produce incorrect values due to integer division. Consider converting to a float for accuracy.
- [ ] **No Genre Fallback**: If a track doesn't have genres, the script doesn't handle this gracefully, leaving the `genre_` fields as 'NA'. Consider a fallback or alternative handling.
- [ ] **Loop Efficiency**: The loops for fetching artist and genre data could be optimized. Currently, the same information is processed multiple times.
- [ ] **No Logging**: The script lacks logging, making it hard to debug issues or monitor its progress during execution.
- [ ] **Track ID Limitation**: The script only processes one track ID at a time. Extending it to handle multiple track IDs in one run would be beneficial.
- [ ] **Remove Unused Files**: Some files are leftover from testing and should be cleaned up.

### Updates

I want to make the script pick songs based on emotional responses. For example, if you're going to the gym and want to be hyped, it will play high-BPM songs.
