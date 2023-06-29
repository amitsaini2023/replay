import requests
import re
import json
import urllib3
from urllib.parse import quote,unquote

def encode_url(url):
    encoded_url = quote(url, safe='')
    return encoded_url


def decode_url(url):
    decoded_url =unquote(url)
    return decoded_url

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#######playlist######
def fetch_playlist(imdb):
    url = f"https://navy-issue-i-239.site/play/{imdb}"
    headers = {
        "Referer": "1"
    }
    method = "GET"
    response = requests.request(method, url, headers=headers)
    response_text = response.text

    # Extract the value of playerConfigs using regex
    pattern = r'let playerConfigs = (.*?);'
    match = re.search(pattern, response_text)

    if match:
        player_configs = match.group(1)
        data_dict = json.loads(player_configs)
        file_str = data_dict['file']
        file_value = file_str.replace("/playlist/", "")
        key_value = data_dict['key']

        # Create a dictionary
        result = {
            'playlist_id': file_value,
            'playlist_pass': key_value
        }
        return result
    else:
        return ("playlist not found!!!.")


#######video_language######)
def fetch_language(playlist_id,playlist_pass):
    url = f"https://navy-issue-i-239.site/playlist/{playlist_id}"

    headers = {
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-csrf-token": f"{playlist_pass}",
        "Referer": "1"
    }

    method = "POST"

    response = requests.post(url, headers=headers)

    result=response.text
    # print(type(result))
    data_dict = json.loads(result)
    return data_dict



########video_url#########
def fetch_url(lang_url,key_value):
    url = f"https://navy-issue-i-239.site/playlist/{lang_url}.txt"
    headers = {
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "Referer": "https://navy-issue-i-239.site/play/tt12758060",
        "x-csrf-token": f"{key_value}"
    }

    response = requests.post(url, headers=headers, verify=False)
    result=response.text
    return result


######convert_url_standard#######
def convert_url(url):
    result = url.replace("https://i-cdn-0.navy-issue-i-239.site", "https://cdn4507.navy-issue-i-239.site")
    return result


#######video_quality########
def fetch_quality(url):
    headers = {
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://navy-issue-i-239.site/"
    }

    response = requests.get(url, headers=headers)
    result=response.text
    quality_list = re.findall(r'\./([\w/]+)',result )
    return quality_list

 #######video_quality_available#########
def changequality(url,variable):
    index = url.rfind("index.m3u8")
    if index != -1:
        new_string = url[:index] + f"{variable}.m3u8"
        return new_string
    else:
        return "Invalid string format. 'index.m3u8' not found."

#######readyurl#####
def readyurl(url):
    constant_value1 = "9999999999"
    constant_value2 = "1.1.1.1"

    # Split the URL by ':' to extract the parts
    parts = url.split(':')

    # print(parts)
    parts[2]=constant_value1
    parts[3]=constant_value2
    # print(parts)
    newstr=':'.join(parts)
    return newstr


######myplayer#########
def myplayer(value):
    ######0#########
    imdb=f'{value}'

    ######1##########
    playlist=fetch_playlist(imdb)
    playlist_id=playlist['playlist_id']
    playlist_pass=playlist['playlist_pass']

    #######2#########
    language_option=fetch_language(playlist_id,playlist_pass) ###list of dict###
    try:
        language_id = (language_option[0]['file'])[1:]
    except TypeError:
        language_id = (language_option[1]['file'])[1:]
    
 
    #######3#########
    play_url=fetch_url(language_id,playlist_pass)
    val=convert_url(play_url)
    value=readyurl(val)
    # encoded_url = encode_url(value)
    # download=encoded_url
    play=changequality(value,'720/index')
    # result_list=[play,download]
    # return result_list
    return play





