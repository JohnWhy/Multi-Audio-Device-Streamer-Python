import sounddevice as sd
import soundfile as sf
import sys
from playlist_json_cmds import *
import random
import os
# from getInfo import *
playlist = sys.argv[1]

# get json file
songs = []
q = []
songs_dir = ''
device = ''


def create_queue():
    global songs, q, device, songs_dir, last_song
    j = get_json(playlist)
    songs_dir = j[playlist]['Folder']
    songs = os.listdir(j[playlist]['Folder'])
    j[playlist]['Playlist'] = songs  # keep playlist for searching
    q = songs # create copy of playlist
    random.shuffle(q)
    j[playlist]['Queue'] = q
    device = j[playlist]['Sound Device']
    print('New Queue Created: '+str(save_json(playlist+'_playlist.json', j)))
    return True


create_queue() # create initial queue


def get_next_song():
    j = get_json(playlist)
    next_song = j[playlist]['Queue'].pop(0)
    save_json(playlist+'_playlist.json', j)
    is_last = False
    if len(j[playlist]['Queue']) == 0:
        is_last = True
    return next_song, is_last


def stream(audio_device):
    global playlist
    while True:
        try:
            current_song, is_last = get_next_song()
            print('Now playing: '+current_song)
            if is_last:
                create_queue()
            # update(current_song, playlist)  # uncomment out if displaying some info on website
            audio1 = songs_dir+current_song
            data1, fs1 = sf.read(audio1, dtype='float32')
            sd.play(data1, fs1, device=audio_device)
            sd.wait()  # wait for stream to finish before continuing
        except Exception as e:
            print(e)
            create_queue()  # restart entire queue after printing error
            # usually errors on some bad file being in folder
            # this is a hacky method to keep the stream going
            pass


stream(device)
