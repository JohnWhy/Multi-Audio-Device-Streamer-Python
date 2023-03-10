# Multi-Audio-Device-Streamer-Python

Requirements:
Requires sounddevice and soundfile

`pip install sounddevice`

`pip install soundfile`

Installation
1. Create a playlist folder containing the MP3 files you want to stream

2. Find audio device to stream through (output_devices.keys() should list all the audio output devices installed on your system)

3. Use controller.py to create an audio stream (create_stream(audio_device, playlist_name, path_to_mp3_folder))

4. Set up a broadcasting tool to listen to the audio stream (I use BUTT + IceCast)

5. Enjoy!

Updating Queue:
playlist_json_cmds.py has 2 commands which might come in handy:
- get_next(playlist_name) - to see what song is going to play next
- queue_next(playlist_name, song_to_queue) - will move a song to play next in a given playlist IF the song exists in the Playlist list (which contains all the song mp3s in the playlist folder), note: if the song is in the queue currently, it will remove it from it's position and put it in the first spot, if the song is NOT in the queue it will simply add it to the front of the line if it exists in the Playlist list.

If you need other functionality I'm sure you can add it.

Optional:
If you host a website to listen to the audio stream, getInfo might come in handy for displaying the currently playing information.  I set up an html page containing the album artwork and currently playing then use the update(mp3_file_name, playlist_name) function to update the html pages, they get refreshed in an iframe using javascript.  I use the Spotify API to get the album artwork.

To see this code in action, check out https://jpydev.net/radio where it acts as an in-character radio site set in 1998 for the GTA:C RP community: https://gta-chronicles.com/index.php
