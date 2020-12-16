from cloudmusic.weapi import search
import argparse
import sys

#def save_image(iurl):
def find_album(keywords):
    slist=search(keywords,"album")
    slist = slist['result']['albums']
    res=[]
    for ab in slist:
        name=ab['name']
        artist=ab['artist']['name']
        iurl=ab['picUrl']
            #img=urllib.request.urlopen(iurl)
            #return img.read()
        #print("%s %s %s\n"%(name,artist,iurl))
        res.append((name,artist,iurl))
    return res

def main():
    parser = argparse.ArgumentParser(description="Album Download from Cloudmusic")
    parser.add_argument('-q','--keywords', default='')
    args = parser.parse_args()
    #print(args)
    title = args.keywords
    res=find_album(title)
    for a,b,c in res:
        sys.stdout.write("%s %s\n%s\n"%(a,b,c))

if __name__ == '__main__':
    main()

'''
from PIL import Image
import sys
from io import BytesIO

song=sys.argv[1]
singer=sys.argv[2]
path='./'
if len(sys.argv)>3:
    path=sys.argv[3]

#搜索并下载封面
song.replace('"',"")
singer.replace('"',"")
Image.open(BytesIO(download_album(song,singer,path))).show()
'''