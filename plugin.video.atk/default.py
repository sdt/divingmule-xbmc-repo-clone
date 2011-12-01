import urllib
import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon

__settings__ = xbmcaddon.Addon(id='plugin.video.atk')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )

def categories():
        base_url = 'http://www.americastestkitchen.com/video/index.php?document_activeCategoryName_2_10_0_mv='
        addDir('Most Recent','http://www.americastestkitchen.com/video',1,icon)
        addDir('Season 11',base_url+'episode&document_season_i=11',1,icon)
        addDir('Season 10',base_url+'episode&document_season_i=10',1,icon)
        addDir('Season 9',base_url+'episode&document_season_i=9',1,icon)
        addDir('Season 8',base_url+'episode&document_season_i=8',1,icon)
        addDir('Season 7',base_url+'episode&document_season_i=7',1,icon)
        addDir('Season 6',base_url+'episode&document_season_i=6',1,icon)
        addDir('Season 5',base_url+'episode&document_season_i=5',1,icon)
        addDir('Season 4',base_url+'episode&document_season_i=4',1,icon)
        addDir('Season 3',base_url+'episode&document_season_i=3',1,icon)
        addDir('Season 2',base_url+'episode&document_season_i=2',1,icon)
        addDir('Season 1',base_url+'episode&document_season_i=1',1,icon)
        addDir('Recipe Clips',base_url+'recipe',1,icon)
        addDir('Equipment Clips',base_url+'testing',1,icon)
        addDir('Taste Test Clips',base_url+'tasting',1,icon)
        addDir('Science Clips',base_url+'science',1,icon)
        

def index(url):
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                   'Referer' : 'http://www.americastestkitchen.com/'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('<img src="(.+?)" class="document_image" title="(.+?)"/></a>\n        <strong><a href="(.+?)" class="video_link">(.+?)</a></strong>\n        <p class="episode">(.+?)</em></p>').findall(link)
        for thumb, title, url, name, episode in match:
            swf = ' swfUrl=http://www.americastestkitchen.com/flowplayer/plugins/flowplayer.rtmp-3.1.3.swf'
            pageUrl = ' pageUrl=http://www.americastestkitchen.com/video/'+url
            Playpath = ' Playpath=mp4:episode-ATKTV_'+episode.split('Ep. ')[1]+'-16x9-1000.m4v'
            tcUrl = 'rtmp://bostoncp.flash.internapcdn.net/bostoncp/_definst_/'
            finalurl = tcUrl+Playpath+pageUrl+swf
            addLink(title, finalurl, thumb)
            
        page = re.compile('<a href="(.+?)">Next</a>').findall(link)
        if len(page) > 0:
            addDir('Next Page','http://www.americastestkitchen.com/video/index.php'+page[0],1,xbmc.translatePath( os.path.join( home, 'resources', 'next.png' ) ))

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


def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
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

if mode==None or url==None or len(url)<1:
    print ""
    categories()

elif mode==1:
    print ""
    index(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))