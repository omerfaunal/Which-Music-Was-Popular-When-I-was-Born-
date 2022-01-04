import spotipy
from spotipy.oauth2 import SpotifyOAuth


def create_list(song_names, date):

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id="ID",
            client_secret="SECRET",
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    song_uris = []
    user_id = sp.current_user()["id"]
    year = date.split("-")[0]

    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Best 100 Songs", public=False)
    print(playlist)

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
