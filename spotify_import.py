import requests

file = open("songs", 'r')
lines = file.readlines()
saved_file = open("saved", "a")

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQDGAkTq77RWVDy_t8aXWOP7sHJY9gXbkFpo1H4t5AoLhubkg9g54Wc9yZ-7JEODuPrQmHYVgR6nkkjNd_Ea7iW2T8qtYQunn4X5GEDyv9SJik0Kc3IdM_PGWjw0fLzA126KZOSgol3nCcamXPYC2_Cn7NUcJ_FXzoE-DHYqz25kaoIVuPfiCIKdGkA-5HfIKps7jffCnKGFbD0TNXVHzf54Y9ICNVVUb7fSXYfTYOi3sQ-VLRpJ2aDt' 
}

for line in lines:
    line = line[:-1]

    params = {
        'q': line,
        'type': 'track',
        'limit': '1',
    }

    response = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)
    print(response.status_code) 
    if response.status_code == 200:
        json = response.json()
        if len(json["tracks"]["items"]) < 1:
            print(json["tracks"]["items"])            
            continue
        track_uri = json["tracks"]["items"][0]["uri"]
    else:
        continue
    params = {
        'uris': track_uri,
    }

    response = requests.post('https://api.spotify.com/v1/playlists/5pKoayvE7pNi6E4BS9bOKO/tracks', params=params, headers=headers)
    if response.status_code == 201:
        print(line)
        saved_file.write(line + "\n")        
        saved_file.flush()

file.close()
saved_file.close()
