import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.espn.go')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
nexticon = xbmc.translatePath( os.path.join( home, 'resources/next.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
bitrate = __settings__.getSetting('bitrate')


def Categories():
        addPlaylist('Play The Latest','http://espn.go.com/video/format/libraryPlaylist?categoryid=2378529&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,4)
        addDir('The Latest','http://espn.go.com/video/format/libraryPlaylist?categoryid=2378529&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index','',1)
        addDir('Sports Center','http://espn.go.com/video/beta/libraryPlaylist?categoryid=5595394&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com',icon,1)
        addDir('NFL','http://espn.go.com/video/format/libraryPlaylist?categoryid=2459789&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('College Football','http://espn.go.com/video/format/libraryPlaylist?categoryid=2564308&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('MLB','http://espn.go.com/video/format/libraryPlaylist?categoryid=2521705&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('NBA','http://espn.go.com/video/format/libraryPlaylist?categoryid=2459788&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('NASCAR ','http://espn.go.com/video/format/libraryPlaylist?categoryid=2492290&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('Golf','http://espn.go.com/video/format/libraryPlaylist?categoryid=2630020&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('NHL','http://espn.go.com/video/format/libraryPlaylist?categoryid=2459791&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('MMA','http://espn.go.com/video/format/libraryPlaylist?categoryid=2881270&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('Boxing','http://espn.go.com/video/format/libraryPlaylist?categoryid=2491554&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('Racing','http://espn.go.com/video/format/libraryPlaylist?categoryid=2755879&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('College Hoops','http://espn.go.com/video/format/libraryPlaylist?categoryid=2459792&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir("Women's Basketball",'http://espn.go.com/video/format/libraryPlaylist?categoryid=3414465&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('Shows','',icon,3)


def Shows():        
        addDir('Jim Rome Is Burning','http://espn.go.com/video/format/libraryPlaylist?categoryid=2963048&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('E:60','http://espn.go.com/video/format/libraryPlaylist?categoryid=3060647&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('The Next Round','http://espn.go.com/video/format/libraryPlaylist?categoryid=5037484&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('SportsNation','http://espn.go.com/video/format/libraryPlaylist?categoryid=5092967&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('Homecoming ','http://espn.go.com/video/format/libraryPlaylist?categoryid=4083827&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('Mike and Mike','http://espn.go.com/video/format/libraryPlaylist?categoryid=2850689&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('Outside the Lines','http://espn.go.com/video/format/libraryPlaylist?categoryid=3286128&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('Road Trip','http://espn.go.com/video/format/libraryPlaylist?categoryid=3619786&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('Page 2','http://espn.go.com/video/format/libraryPlaylist?categoryid=2494144&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)
        addDir('ESPNU','http://espn.go.com/video/format/libraryPlaylist?categoryid=2491548&pageNum=0&sortBy=&assetURL=http://assets.espn.go.com&module=LibraryPlaylist&pagename=vhub_index',icon,1)


def getVideos(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://espn.go.com/video/'),
                        ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        videos = soup.findAll('div', attrs={'class' : "video-cell"})
        print len(videos)
        for video in videos:
            name = video.h5.string
            Pageurl = video.a['href']
            thumb = video.img['src']
            item = thumb.split('/')[-1].split('_thumdnail')[0]
            try:
                if int(item.split('_')[1][:6]):
                    year = '20'+thumb.split('/')[-1].split('_')[1].split('_')[0][:2]
                    date = thumb.split('/')[-1].split('_')[1].split('_')[0][2:6]
                    link = 'http://vod.espn.go.com/motion/'+year+'/'+date+'/'+item+'.smil?FLVPlaybackVersion=2.1'
            except:
                print 'trying smilurl#2>>>>'
                print 'ThumbUrl :'+thumb
                link = 'http://vod.espn.go.com/motion/'+thumb.split('/')[-3]+'/'+thumb.split('/')[-2]+'/'+item+'.smil?FLVPlaybackVersion=2.1'
                print 'smil #2---/>' + link
            addLink(name,link,thumb,2)
        if len(videos) == 12:
            url = url.replace(str(int(url.split('&')[1][-1])),str(int(url.split('&')[1][-1])+1))
            addDir('Next Page',url,nexticon,1)


def getPlaylist(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://espn.go.com/video/'),
                        ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        videos = soup.findAll('div', attrs={'class' : "video-cell"})
        playlist = xbmc.PlayList(1)
        playlist.clear()
        for video in videos:
            name = video.h5.string
            Pageurl = video.a['href']
            thumb = video.img['src']
            item = thumb.split('/')[-1].split('_thumdnail')[0]
            try:
                if int(item.split('_')[1][:6]):
                    year = '20'+thumb.split('/')[-1].split('_')[1].split('_')[0][:2]
                    date = thumb.split('/')[-1].split('_')[1].split('_')[0][2:6]
                    link = 'http://vod.espn.go.com/motion/'+year+'/'+date+'/'+item+'.smil?FLVPlaybackVersion=2.1'
            except:
                print 'trying smilurl#2>>>>'
                print 'ThumbUrl :'+thumb
                link = 'http://vod.espn.go.com/motion/'+thumb.split('/')[-3]+'/'+thumb.split('/')[-2]+'/'+item+'.smil?FLVPlaybackVersion=2.1'
                print 'smil #2---/>' + link
            try:
                url = getSmil(link)
                info = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumb)
                playlist.add(url, info)
            except:
                pass
        play=xbmc.Player().play(playlist)


def getSmil(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://espn.go.com/video/'),
                ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link)
        if bitrate == "448k":
            url = soup.meta['base']+soup('video')[0]['src'].replace('mp4:','')
        if bitrate == "948k":
            url = soup.meta['base']+soup('video')[1]['src'].replace('mp4:','')
        if bitrate == "1464k":
            url = soup.meta['base']+soup('video')[2]['src'].replace('mp4:','')
        if bitrate == "2096k":
            url = soup.meta['base']+soup('video')[3]['src'].replace('mp4:','')            
        if bitrate == "2896k":
            url = soup.meta['base']+soup('video')[4]['src'].replace('mp4:','')
        return url
            
        
def setUrl(url):
        try:
            url = getSmil(url)
            item = xbmcgui.ListItem(path=url)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
        except urllib2.HTTPError, e:
            errorStr = str(e.read())
            soup = BeautifulSoup(errorStr)
            print soup.title.string
            xbmc.executebuiltin("XBMC.Notification(ESPN Go,HTTP Error: "+soup.title.string+",10000,"+icon+")")
            pass


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params.replace('?','')
            if (params[len(params)-1]=='/'):
                params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                splitparams={}
                splitparams=pairsofparams[i].split('=')
                if (len(splitparams))==2:
                    param[splitparams[0]]=splitparams[1]
        return param


def addLink(name,url,iconimage,mode):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable', 'true')
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok


def addDir(name,url,iconimage,mode):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def addPlaylist(name,url,iconimage,mode):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
        

params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
if mode==None:
    print ""
    Categories()
        
if mode==1:
    print""
    getVideos(url)
        
if mode==2:
    print""
    setUrl(url)
    
if mode==3:
    print""
    Shows()    

if mode==4:
    print""
    getPlaylist(url)    
    
xbmcplugin.endOfDirectory(int(sys.argv[1]))