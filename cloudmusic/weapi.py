import urllib.request
import http.cookiejar
from .debug import ls,print_json
from .encrypt import Encrypt_post, MD5
import os,re,ssl,bs4,difflib,json
#ssl._create_default_https_context = ssl._create_unverified_context

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

def send_request(url,data):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/13.10586',
        'Content-Type':'application/x-www-form-urlencoded',
        'Referer':'https://music.163.com',
        'Host': 'music.163.com',
        #'X-Real-IP':
    }
    req = urllib.request.Request(url, data,headers=headers)
    rp = opener.open(req)
    rep = rp.read().decode("utf-8")
    '''
    for item in cookie:
        print("%s=%s"%(item.name,item.value))
    '''
    return rep

# login by cellphone
def login_by_phone(phone, pwd):
    # musicloud account
    account = {
        'phone': phone,
        'password': pwd,
        'rememberLogin': True,
        'csrf_token': "",
    }
    #encrypt Account and Password  by md5
    m = MD5.new(account['password'].encode('utf-8'))
    account['password'] = m.hexdigest()
    url = "http://music.163.com/weapi/login/cellphone"
    data = Encrypt_post(account)
    rep = send_request(url,data)
    account_info = json.loads(rep)
    return account_info["account"]["id"], account_info["profile"]["nickname"]

# return playlists
def get_user_playlists(user_id):
    post_text = {
        "uid": user_id,
        "wordwrap": 7,
        "offset": 0,
        "total": True,
        "limit": 100,
        "csrf_token": ""
        }
    url = "http://music.163.com/weapi/user/playlist"
    data = Encrypt_post(post_text)
    rep = send_request(url,data)
    playlist_dict  = json.loads(rep)
    playlist = playlist_dict['playlist']
    count = 0
    plays = []
    for play in playlist:
        plays.append([play["name"], play["id"], play["playCount"], play["trackCount"], play["creator"]["nickname"]])
        count += play["trackCount"]
    return plays, count

# return  listen records
def get_user_listen_records(user_id, time):
    key = {"week": 1, "all": 0}
    post_text = {
        "uid": user_id,
        "type": key[time],  # 1week 0 all
        "limit": 1000,
        "offset": 0,
        "total": True,
        }
    url = "http://music.163.com/weapi/v1/play/record?csrf_token="
    data = Encrypt_post(post_text)
    rep = send_request(url,data)
    record_dict = json.loads(rep)
    record = {}
    for song in record_dict[time + "Data"]:
        record[song["song"]["id"]] = song["song"]["name"]
    return record

# return songs
def get_songs_from_playlist(pl_id):
    post_text={
        "id":66731285,
        "limit":1000,
        "offset":0,
        "total":True,
    }
    url = "http://music.163.com/weapi/playlist/detail?csrf_token="
    data = Encrypt_post(post_text)
    rep = send_request(url,data)
    details = json.loads(rep)
    print_json(details)
    return details

# return comment [user_name,comment]
def get_song_comment(song_id):
    rid = "R_SO_4_" + str(song_id)
    post_text = {
        "csrf_token": "",
        "limit": "20",
        "offset": "0",
        "rid": rid,
        "total": "true"
        }
    url = "http://music.163.com/weapi/resource/comments/get" + rid
    data = Encrypt_post(post_text)
    rep = send_request(url,data)
    comments = json.loads(rep)
    print_json(comments)
    hot_cmts = []
    for item in comments["hotComments"]:
        hot_cmts.append([item["user"]["nickname"], item["content"], item["likedCount"]])
    cmt_total = comments["total"]
    return hot_cmts, cmt_total

# search music and get album
def search(keywords, type):
    #1: 单曲, 10: 专辑, 100: 歌手, 1000: 歌单, 1002: 用户, 1004: MV, 1006: 歌词, 1009: 电台, 1014: 视频, 1018:综合
    itype={"song":1,"album":10,"singer":100,"playlist":1002,"lyric":1006}
    post_text = {
        "csrf_token": "",
        "s": keywords,
        "offset":"0",
        "limit": "30",
        "type": itype[type]
        }
    url = "https://music.163.com/weapi/search/get/"
    data = Encrypt_post(post_text)
    data = Encrypt_post(post_text)
    rep = send_request(url,data)
    slist = json.loads(rep)
    #print_json(slist)
    return slist

if __name__ == "__main__":
    #uid,uname=login_by_phone("","")
    #get_user_playlists(uid)
    #get_user_listen_records(uid,"all")
    #get_songs_from_playlist("")
    #get_song_comment(481375)
    search("越长大越孤单 牛奶咖啡","album")



    