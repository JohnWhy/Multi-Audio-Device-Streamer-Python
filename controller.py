from playlist_json_cmds import *
import sounddevice as sd
import os

all_audio_devices = sd.query_devices()
output_devices = {}
for i in all_audio_devices:
    if i['max_output_channels'] > 1:  # input ??
        if i['name'] not in output_devices.keys():
            output_devices[i['name']] = i['index']


def get_device_index(device):
    for audio_device in output_devices.keys():
        if device in audio_device:
            return output_devices[audio_device]
    return False


def create_stream(device, playlist_name, folder):
    device = get_device_index(device)
    
    if type(device) == int:
        initialize_playlist(playlist_name, folder, device)
    else:
        print('Failed to find output device for '+playlist_name+' Playlist')

    # create player
    cmd = "start cmd /k python music_player.py "+playlist_name
    print(cmd)
    os.system(cmd)


# ex:
# create_stream('CABLE Input', 'punk', 'Punk_Playlist/')
# create_stream('Line 1', 'rap', 'Rap_Playlist/')
