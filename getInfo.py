import requests


def get_token():
    client_id = ''  # get client id from spotify api
    client_secret = ''  # get client secret from spotify api

    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    })
    auth_response_data = auth_response.json()

    access_token = auth_response_data['access_token']
    return access_token


headers = {
    'Authorization': 'Bearer {token}'.format(token=get_token())
}
BASE_URL = 'https://api.spotify.com/v1/'


def get_album_artwork_url(track,artist):
    global headers
    r = requests.get(BASE_URL+'search/?q='+track+' '+artist+'&type=track', headers=headers)
    if r.status_code == 200:
        return r.json()['tracks']['items'][0]['album']['images'][0]['url']
    else:
        print('Failed to get album artwork: '+str(r.status_code))
        headers = {'Authorization': 'Bearer {token}'.format(token=get_token())}
        print('Retrying with new token...')
        r = requests.get(BASE_URL+'search/?q='+track+' '+artist+'&type=track', headers=headers)
        print('Retry result: '+str(r.status_code))
        return r.json()['tracks']['items'][0]['album']['images'][0]['url']


def update(current, playlist):
    s = current.split(' - ')
    artist = s[0]
    if len(s) > 2:
        track = s[1]
    else:
        track = s[1][:-4]
    string = artist + ' - ' + track
    print(string)
    try:
        album_artwork_url = get_album_artwork_url(track,artist)
    except Exception as e:
        print(e)
        album_artwork_url = ''  # return some default image if album artwork can't be gathered
    ## CHANGE SONG ON playlist_CURRENTLY_PLAYING.HTML
    # Update the open path to match where your website files are kept
    # this is a hacky method updating HTML and then refreshing iframes on the website to
    # keep them updated with the currently playing song
    read = open('C:/inetpub/party/'+playlist+'_currently_playing.html','r+')
    rlist = read.readlines()
    read.close()
    rwrite = open('C:/inetpub/party/'+playlist+'_currently_playing.html','w')
    rlist[rlist.index('<h1 id="song" value=\n')+1] = '"'+string+'">\n'
    rlist[rlist.index('<h1 id="song" value=\n')+2] = string+'\n'
    for i in rlist:
        rwrite.write(i)
    rwrite.close()
    ## CHANGE ARTWORK ON playlist_ALBUM_ARTWORK.HTML
    read = open('C:/inetpub/party/'+playlist+'_album_artwork.html','r+')
    rlist = read.readlines()
    read.close()
    rwrite = open('C:/inetpub/party/'+playlist+'_album_artwork.html','w')
    rlist[rlist.index('<image id="album_artwork" src=\n')+1] = '"'+album_artwork_url+'"\n'
    for i in rlist:
        rwrite.write(i)
    rwrite.close()
