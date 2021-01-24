import lyricsgenius as lg
import get_songs as gs
import random
from pathlib import Path

CLIENT_ACCESS = 'INSERT SECRET GENIUS API HERE'


def lyrics_to_file(songs, dir_path):
    count = 0
    path = str(Path().resolve().parent)
    genius = lg.Genius(CLIENT_ACCESS, skip_non_songs=True, 
    remove_section_headers=True)

    for (title, artist) in songs: 
        try:
            song = genius.search_song(title, artist)
            name = title[:4]
            
            f = open(f'/{path}{dir_path}/{count}_{name}.txt','w')
            f.write(song.lyrics)
            f.close()
            
            print(f'Loaded lyrics for {title} - {artist} succesfully')
            count += 1
        
        except:
            print(f'Exception at {title} - {artist}, iteration: {count}')
    
    print(f'Loaded:{count} lyrics')


def partition_set(data):
    random.shuffle(data)
    n = len(data)
    ratio = 0.8
    index = int(ratio * n)

    training_set = data[:index]
    test_set = data[index:]
    
    return training_set, test_set


def build_db_for(data, label):
    training_data, test_data = partition_set(data)
    lyrics_to_file(training_data, f'/data/training/{label}'), 
    lyrics_to_file(test_data, f'/data/test/{label}')


def build_db():
    hits = gs.get_top_100_songs()
    non_hits = gs.get_non_hits()

    build_db_for(hits, 'hits')
    build_db_for(non_hits, 'non_hits')


build_db()