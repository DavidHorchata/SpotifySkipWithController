def skipSong(spotifyObject, device_id):

    current = spotifyObject.current_playback()
    if not current:

        spotifyObject.start_playback(device_id=device_id)

    spotifyObject.next_track(device_id=device_id)




def incrementVolume(spotifyObject, device_id):
    current = spotifyObject.current_playback()
    
    newVolume = current['device']['volume_percent'] + 2


    spotifyObject.volume(newVolume,device_id)
    