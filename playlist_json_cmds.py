import json

f_loc = 'json_playlists/'


def get_json(name):
    f = open(f_loc+name+'_playlist.json', 'r')
    json_object = json.load(f)
    f.close()
    return json_object


def save_json(json_name, new_json):
    njo = json.dumps(new_json)
    with open(f_loc+json_name,'w') as f:
        f.write(njo)
    return True


def initialize_playlist(playlist_name,
                        folder_loc,
                        sound_device):
    # j = get_json(playlist_name)
    j = {playlist_name: {"Folder": folder_loc,
                    "Playlist": [],
                    "Queue": [],
                    "Sound Device": sound_device
                    }}
    return save_json(playlist_name+'_playlist.json',j)


def queue_next(playlist, song):
    json_object = get_json(playlist)
    l = json_object[playlist]['Playlist']
    for i in l:
        if song.lower() in i.lower():
            for e in json_object[playlist]['Queue']:
                if e == i:
                    json_object[playlist]['Queue'].remove(i)
            json_object[playlist]['Queue'].insert(0,i)
    return save_json(playlist+'_playlist.json', json_object)


def get_next(playlist):
    json_object = get_json(playlist)
    queue = json_object[playlist]['Queue']
    if len(queue) != 0:
        return queue[0]
    else:
        return 'Queue Empty'  # this shouldn't ever happen
