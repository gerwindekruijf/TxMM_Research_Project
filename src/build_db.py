import lyricsgenius as lg
import billboard_songs as bb

CLIENT_ID = 'GeBEj1pzFpR9T_L5ALqj_PAqKgsRtcv6XamMYn_wJrMqGxerBtz88zks_N363KXA'
CLIENT_SECRET = '9LBiKDGbIBIJwB9pCqLcwVv_HtVvVvx1HyNohwziFU_s0JUkMkKflMPGjJHYeEz5M65pc2aSPNnvEJI8-1RYkg'

genius = lg.Genius(CLIENT_ID, skip_non_songs=True, 
remove_section_headers=True, excluded_terms=["(Remix)", "(Live)"])


def get_lyrics():
    hits = bb.get_top_100_songs()
    non_hits = bb.get_non_hits()
    songs = hits.update(non_hits)

    for title, artist in songs:
        try:
            songs = genius.search_song(title, artist)
            for song in songs:
                song.lyrics
                # file.write("\n \n   <|endoftext|>   \n \n".join(s))
                c += 1
            print(f"Songs grabbed:{len(c)}")
        except:
            print(f"some exception at {title} - {artist}")
