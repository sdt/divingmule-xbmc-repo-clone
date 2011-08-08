import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup
try:
    import json
except:
    import simplejson as json
import resources.lib.common as common
import resources.lib.dallas as dallas
import resources.lib.teams as teams

__settings__ = xbmcaddon.Addon(id='plugin.video.nfl')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
cdn = __settings__.getSetting('cdn')
bitrate = __settings__.getSetting('bitrate')

print 'bitrate----> '+bitrate
print 'cdn-------> '+cdn

icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
next = xbmc.translatePath( os.path.join( home, 'resources','icons','next.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )

def categories():
        addDir('All Videos','http://www.nfl.com/videos/nfl-videos',1,icon)
        addDir('Game Highlights','http://www.nfl.com/videos/nfl-game-highlights',1,icon)
        addDir('Shows','',2,icon)
        addDir('Teams','',2,icon)
        addDir('Spotlight','',2,icon)
        addDir('Events','',2,icon)
        addDir('Search','',14,xbmc.translatePath( os.path.join( home, 'resources','icons','search.png' ) ))
        addDir('Team Sites','',6,icon)
        		

def teamSite():
        addDir('Az Cardinals.com','',9,'http://farm7.static.flickr.com/6001/5984449229_fbed0e5147_m.jpg')
        addDir('Bengals.com','',10,'http://farm7.static.flickr.com/6011/6009300352_4f1f19b3bc_m.jpg')
        addDir('Buccaneers.com','',11,'http://farm7.static.flickr.com/6130/6009473824_9015669a7c_m.jpg')
        addDir('Cleveland Browns.com','',12,'http://farm7.static.flickr.com/6127/6009299438_1f1dd2bec7_m.jpg')
        addDir('Chargers.com','',13,'http://farm7.static.flickr.com/6022/5983336472_98c373d130_m.jpg')
        addDir('Dallas Cowboys.com','',15,'http://farm7.static.flickr.com/6021/5995834962_78ff72f058_m.jpg')
        addDir('Detroit Lions.com','',18,'http://farm7.static.flickr.com/6008/5988506040_a546c4983b_m.jpg')
        addDir('49ers.com','',19,'http://farm7.static.flickr.com/6140/5985014424_c9817f5c82_m.jpg')
        addDir('Giants.com','',20,'http://farm7.static.flickr.com/6123/5995276331_5b335c77de_m.jpg')
        addDir('Houston Texans.com','',21,'http://farm7.static.flickr.com/6010/5994131823_c86dca0c96_m.jpg')
        addDir('KC Chiefs.com','',22,'http://farm7.static.flickr.com/6135/5982773393_53a393e5e1_m.jpg')
        addDir('New York Jets.com','',23,'http://farm7.static.flickr.com/6127/5999958596_84ff270f61_m.jpg')
        addDir('New Orleans Saints.com','',24,'http://farm7.static.flickr.com/6125/6008924973_75bf096d30_m.jpg')
        addDir('Packers.com','',25,'http://farm7.static.flickr.com/6125/5987940779_50243f0567_m.jpg')
        addDir('Panthers.com','',26,'http://farm7.static.flickr.com/6012/6009472252_8492f9d7b2_m.jpg')
        addDir('Patriots.com','',27,'http://farm7.static.flickr.com/6133/5999408997_9dd8533670_m.jpg')
        addDir('Philadelphia Eagles.com','',28,'http://farm7.static.flickr.com/6140/5995277769_fd13323507_m.jpg')
        addDir('Raiders.com','',29,'http://farm7.static.flickr.com/6145/5982772583_6131581422_m.jpg')
        addDir('Redskins.com.com','',30,'http://farm7.static.flickr.com/6148/5995833826_2bb2981de1_m.jpg')
        addDir("Seahawks.com",'',31,'http://farm7.static.flickr.com/6002/5984451637_4f7bb3b46f_m.jpg')
        addDir('St Louis Rams.com','',32,'http://farm7.static.flickr.com/6012/5985015330_814587c665_m.jpg')
        addDir('Titans Online.com','',33,'http://farm7.static.flickr.com/6014/5994130863_839e1e630b_m.jpg')
        addDir('Vikings.com','',34,'http://farm7.static.flickr.com/6016/5988505154_0749939588_m.jpg')
        

def getSubCategories(name):
        req = urllib2.Request('http://www.nfl.com/videos/')
        req.addheaders = [('Referer', 'http://www.nfl.com/'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        if name=='Shows':
            categories = soup.findAll('div', attrs={'class' : "channels"})[0]('a')
        elif name=='Teams':
            categories = soup.findAll('div', attrs={'class' : "channels"})[1]('a')
        elif name=='Spotlight':
            categories = soup.findAll('div', attrs={'class' : "channels"})[2]('a')
        elif name =='Events':
            categories = soup.findAll('div', attrs={'class' : "channels"})[3]('a')
        for cat in categories:
            name = cat.string
            url = cat['href']
            addDir(name,url,1,icon)


def index(url,name):
        if not name=='All Videos':
            if not re.search('page=', url):
                addPlaylist('Play Featured Videos',url,4,'')
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.nfl.com/'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        videos = soup.find('ul', attrs={'id' : "video-list-items"})('li')
        for video in videos:
            name = video('h3')[0]('a')[0].string
            link = video('h3')[0]('a')[0]['href'].split('/')[3]
            thumb = video('img')[0]['src'].replace('_video_thumbnail_80_60.jpg','_video_rhr_280_210.jpg')
            try:
                desc = video('p')[1].string+' \n  '+video('p')[0].string
            except:
                desc = video('p')[0].string
            duration = video('div')[-1].string.replace('\n','').replace('\t','')
            addLink(name,link,thumb,duration,desc,3)
        try:
            page = soup.find('div', attrs={'id' : "video-list-pagination"})('a')[-1]['href']
            if not page == '?page=3':
                addDir('Next Page',url.split('?')[0]+page,1,next)
            else:
                addDir('Next Page','http://www.nfl.com/ajax/videos/v2?batchNum=1&channelId='+url.split('/')[-1].split('?')[0],5,next)
        except:
            pass


def getPage3(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.nfl.com/'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        data = json.loads(link)
        videos = data['videos']
        for video in videos:
            url = video['videoCMSID']
            name = video['briefHeadline']
            thumb = video['xSmallImage'].replace('_video_thumbnail_60_45.jpg','_video_rhr_280_210.jpg')
            desc = video['captionBlurb']
            duration = video['runTime'][:-3]
            addLink(name,url,thumb,duration,desc,3)


def getFeaturedVideos(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.nfl.com/'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        try:
            videos = soup.find('div', attrs={'id' : "featured-videos-carousel"})('ul')[0]('h3')
        except:
            videos = soup.findAll('ul', attrs={'class' : "list-items"})[0]('h3')
        playlist = xbmc.PlayList(1)
        playlist.clear()
        for video in videos:
            name = video('a')[0].string
            url = video('a')[0]['href'].split('/')[3]
            url = getVideoUrl(url)
            info = xbmcgui.ListItem(name)
            playlist.add(url, info)
        play=xbmc.Player().play(playlist)
        
        
def search():
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr,'Search')
        keyboard.doModal()
        if (keyboard.isConfirmed() == False):
            return
        newStr = keyboard.getText().replace(' ','+')
        if len(newStr) == 0:
            return
        url = 'http://search.nfl.com/videos/search-results?quickSearch='+newStr
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.nfl.com/videos'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link)
        videos = soup('li')
        for video in videos:
            try:
                name = video('a')[0]['title']
                url = video('a')[0]['href'].split('id=')[1]
                thumb = video('a')[0]('img')[0]['src'].replace('_video_thumbnail_80_60.jpg','_video_rhr_280_210.jpg')
                desc = video('p')[0].string
                duration = video('p')[1].string
                addLink(name,url,thumb,duration,desc,3)
            except:
                pass


def getVideoUrl(url):
        url = 'http://www.nfl.com/static/embeddablevideo/'+url+'.json'
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.nfl.com/'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        data = json.loads(link)
        print data

        if bitrate == "3200k":
            try:
                url = data['cdnData']['bitrateInfo'][4]['path']
            except:
                try:
                    url = data['cdnData']['bitrateInfo'][3]['path']
                except:
                    try:
                        url = data['cdnData']['bitrateInfo'][2]['path']
                    except:
                        try:
                            url = data['cdnData']['bitrateInfo'][1]['path']
                        except:
                            url = data['cdnData']['bitrateInfo'][0]['path']
        elif bitrate == "2000k":
            try:
                url = data['cdnData']['bitrateInfo'][3]['path']
            except:
                try:
                    url = data['cdnData']['bitrateInfo'][2]['path']
                except:
                    try:
                        url = data['cdnData']['bitrateInfo'][1]['path']
                    except:
                        url = data['cdnData']['bitrateInfo'][0]['path']
        elif bitrate == "1200k":
            try:
                url = data['cdnData']['bitrateInfo'][2]['path']
            except:
                try:
                    url = data['cdnData']['bitrateInfo'][1]['path']
                except:
                    url = data['cdnData']['bitrateInfo'][0]['path']
        elif bitrate == "700k":
            try:
                url = data['cdnData']['bitrateInfo'][1]['path']
            except:
                url = data['cdnData']['bitrateInfo'][0]['path']
        else:
            url = data['cdnData']['bitrateInfo'][0]['path']
            #cdn = 'rtmp://nfl.fcod.llnwd.net/a2290 app=a2290 swfUrl=http://flash.static.nfl.com/static/site/3.5/flash/video/video-detail-player.swf Playpath=vod/'
            #return cdn+url
        cdn0 = 'http://l.video.nfl.com/'           #limelightProg 700k only
        cdn1 ='http://vod.hstream.video.nfl.com/'  #akamaiHTTP  streams seem to end early
        cdn2 = 'http://a.video.nfl.com/'           #akamaiProg
        cdn3 = 'rtmp://cp86372.edgefcs.net/ondemand swfUrl=http://flash.static.nfl.com/static/site/3.5/flash/video/video-detail-player.swf'   #pathprefix="vod/gallery/" akamaiRTMP
        cdn4 = 'rtmp://nfl.fcod.llnwd.net/a2290 app=a2290 swfUrl=http://flash.static.nfl.com/static/site/3.5/flash/video/video-detail-player.swf'  # seems to only work at 700k   #pathprefix="vod/"  limelightRTMP
        liveCDN = 'rtmp://cp37426.live.edgefcs.net/live'

        if  __settings__.getSetting('cdn') == "limelight-RTMP 700k only":
            if not re.search('.mp4', url):
                playpath = ' Playpath=vod/'
            else:
                playpath = ' Playpath=mp4:vod/'
            cdn = cdn4+playpath
        elif  __settings__.getSetting('cdn') == "akamai-RTMP":
            if not re.search('.mp4', url):
                playpath = ' Playpath=vod/'
            else:
                playpath = ' Playpath=mp4:vod/'
            cdn = cdn3+playpath
        elif  __settings__.getSetting('cdn') == "limelightProg-HTTP 700k only":
            cdn = cdn0
        elif  __settings__.getSetting('cdn') == "akamai-HTTP":
            cdn = cdn1
        elif  __settings__.getSetting('cdn') == "akamaiProg-HTTP":
            cdn = cdn2
        print "Resolved URL -----> "+cdn+url
        return cdn+url


def setUrl(url):
        url = getVideoUrl(url)
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)


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


def addLink(name,url,iconimage,duration,description,mode):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "duration": duration, "Plot":description } )
        liz.setProperty('IsPlayable', 'true')
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def addPlaylist(name,url,mode,iconimage):
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
try:
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None:
        print ""
        categories()

elif mode==1:
        print ""+url
        index(url,name)

elif mode==2:
        print ""+url
        getSubCategories(name)

elif mode==3:
        print ""+url
        setUrl(url)

elif mode==4:
        print ""+url
        getFeaturedVideos(url)

elif mode==5:
        print ""+url
        getPage3(url)

elif mode==6:
        print ""
        teamSite()

elif mode==7:
        print ""
        common._index(url,fanart)

elif mode==8:
        print ""
        common._getVideoUrl(url)

elif mode==9:
        print ""
        teams.cardinals()

elif mode==10:
        print ""
        teams.bengals()

elif mode==11:
        print ""
        teams.buccaneers()

elif mode==12:
        print ""
        teams.browns()

elif mode==13:
        print ""
        teams.chargers()

elif mode==14:
        print ""
        search()

elif mode==15:
        print ""
        dallas._categories()

elif mode==16:
        print ""
        dallas._index(url)

elif mode==17:
        print ""
        dallas._getVideoUrl(url)

elif mode==18:
        print ""
        teams.lions()

elif mode==19:
        print ""
        teams.fortyniners()
        
elif mode==20:
        print ""
        teams.giants()
        
elif mode==21:
        print ""
        teams.texans()

elif mode==22:
        print ""
        teams.chiefs()

elif mode==23:
        print ""
        teams.jets()

elif mode==24:
        print ""
        teams.saints()

elif mode==25:
        print ""
        teams.packers()

elif mode==26:
        print ""
        teams.panthers()

elif mode==27:
        print ""
        teams.patriots()

elif mode==28:
        print ""
        teams.eagles()

elif mode==29:
        print ""
        teams.raiders()

elif mode==30:
        print ""
        teams.redskins()

elif mode==31:
        print ""
        teams.seahawks()

elif mode==32:
        print ""
        teams.rams()
        
elif mode==33:
        print ""
        teams.titans()

elif mode==34:
        print ""
        teams.vikings()

xbmcplugin.endOfDirectory(int(sys.argv[1]))