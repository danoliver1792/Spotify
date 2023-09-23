import spotipy
from spotipy.oauth2 import SpotifyOAuth
import matplotlib.pyplot as plt

# configuring Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id='',
        client_secret='',
        redirect_uri='http://localhost:8080/callback',
        scope='user-top-read'
    )
)

try:
    # getting the most listened to tracks
    top_tracks = sp.current_user_top_tracks(time_range='long_term', limit=10)

    # extracting track name and play count
    track_names = [track['name'] for track in top_tracks['items']]
    play_counts = [track['popularity'] for track in top_tracks['items']]

except spotipy.SpotifyOAuth as e:
    print(f'Error: {e}')

# demonstrating the data graphically
plt.figure(figsize=(4, 2))
plt.barh(track_names, play_counts, color='skyblue')
plt.xlabel('Reproductions')
plt.ylabel('Tracks')
plt.title('Top 10 - Tracks')
plt.gca().invert_yaxis()
plt.show()
