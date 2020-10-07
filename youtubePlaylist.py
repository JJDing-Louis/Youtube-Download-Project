from pytube import Playlist
import os
playlist='https://www.youtube.com/playlist?list=PL-g0fdC5RMbrYH6ie-_KvV-QCIfQ_8BLW'
pl = Playlist(playlist)
pathdir='playlist'
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)
pl.download_all(pathdir)
print('下載完成!')
#a=pl.parse_links()
#pllist=[]
#for thing in a:
#    print(thing)
#    print(type(thing))
#    pllist.append(thing)



#print(a)
#print(type(a))
#print(len(a))

