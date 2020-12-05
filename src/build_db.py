import lyricsgenius as lg

CLIENT_ID = 'GeBEj1pzFpR9T_L5ALqj_PAqKgsRtcv6XamMYn_wJrMqGxerBtz88zks_N363KXA'
CLIENT_SECRET = '9LBiKDGbIBIJwB9pCqLcwVv_HtVvVvx1HyNohwziFU_s0JUkMkKflMPGjJHYeEz5M65pc2aSPNnvEJI8-1RYkg'

genius = lg.Genius(CLIENT_ID, skip_non_songs=True, 
remove_section_headers=True)

def get_lyrics(arr, k):
    c = 0
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            file.write("\n \n   <|endoftext|>   \n \n".join(s))
            c += 1
            print(f"Songs grabbed:{len(s)}")
        except:
            print(f"some exception at {name}: {c}")
