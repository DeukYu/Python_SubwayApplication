import json, requests

def FindAddress(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
    headers = {"Authorization": "KakaoAK 2bcd0816537bcb95f84c7c844bb925cd"}
    result = json.loads(str(requests.get(url, headers=headers).text))
    #print(result)
    match_first = result['documents'][0]['road_address']

    return [float(match_first['y']), float(match_first['x'])]


def FindAddress2(addr):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query=' + addr
    headers = {"Authorization": "KakaoAK 2bcd0816537bcb95f84c7c844bb925cd"}
    result = json.loads(str(requests.get(url, headers=headers).text))
    #print(result)
    match_first = result['documents'][0]

    return [float(match_first['y']), float(match_first['x'])]


def Translation(text):
    url = 'https://kapi.kakao.com/v1/translation/translate?src_lang=en&target_lang=kr&query=' + text
    headers = {"Authorization": "KakaoAK 2bcd0816537bcb95f84c7c844bb925cd"}
    result = json.loads(str(requests.get(url, headers=headers).text))
    #print(result)

    return result['translated_text'][0][0]
