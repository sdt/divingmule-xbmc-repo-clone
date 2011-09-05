import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulStoneSoup
from resources import foxSportSouth as fss

__settings__ = xbmcaddon.Addon(id='plugin.video.fox.sports')
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )


def Categories():
        addDir('Fox SportSouth','',icon,4)
        addDir('Shows','',icon,3)
        addDir('Featured Videos','http://edge1.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=top%20news&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports__featuredvideo',icon,1)
        addDir('all video','http://edge4.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=VC_Supplier&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&st=1&tag=Fox%20Sports&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('NASCAR','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sf=ActiveStartDate&tag=fox%20sports_motorsports&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('NFL','http://edge4.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&tag=Fox%20Sports_NFL%20News&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('MLB','http://edge3.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&tag=fox%20sports_baseball%20news&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('NHL','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sf=ActiveStartDate&tag=fox%20sports_hockey%20news&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('NBA','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&tag=Fox%20Sports_NBA%20news&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('FOX Soccer','http://edge4.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&sf=ActiveStartDate&tag=fsc%20home&vs=1&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('Tennis','http://edge4.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&tag=tennis&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('Golf','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&tag=fox%20sports_golf&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('NCAA Football','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sf=ActiveStartDate&tag=fox%20sports_college%20fb%20news&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('NCAA Basketball','http://edge1.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sf=ActiveStartDate&tag=fox%20sports_college%20bk%20news&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('MMA-Boxing','http://edge4.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&tag=fox%20sports_fight%20video&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('Speed Channel','http://edge5.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&tag=fox%20sports_motorsports_speed&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('Fuel TV','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&tag=fox%20sports_action_fuel&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('Olympic Sports','http://edge3.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&tag=fox%20sports_olympic%20sports&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('More Sports','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=MSNVideo_Top_Cat&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&tag=fox%20sports_more%20fox%20sports&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)
        addDir('Fantasy','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&sd=-1&sf=ActiveStartDate&tag=fantasy&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_video_channel_gallery',icon,1)


def Shows():
        addDir('Online OT','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=online%20ot&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/09/14/_730_20100914192716_111_53.JPG',1)
        addDir('MMAthletics','http://edge1.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=mmathletics&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/05/11/mma_show_thumb_20100511191905_111_53.JPG',1)
        addDir('Barfly','http://edge3.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=barfly&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2011/02/24/barfly_313x150_20110224130904380_111_53.JPG',1)
        addDir('Cheapseats','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=mlb_cheapseats&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/05/11/cheapseats_show_thumb_20100511192658_111_53.JPG',1)
        addDir('Cubed','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=cubed&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/05/11/cubed_show_thumb_20100511193510_111_53.JPG',1)
        addDir('3 Wide','http://edge4.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=lwb_3wide&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/05/11/3wide_show_thumb_20100511193714_111_53.JPG',1)
        addDir('What the FOX','http://edge1.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=bloopers&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/09/24/what_the_fox_20100924151607_111_53.JPG',1)
        addDir('After Party','http://edge5.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=afterparty&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/09/07/afterparty_show_thumb_20100907200823_111_53.PNG',1)
        addDir('College Experiment','http://edge1.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=collegeexperiment&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/05/11/collegeexp_show_thumb_20100511200535_111_53.JPG',1)
        addDir('NFL on FOX','http://edge4.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=nflonfoxonly&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/05/11/nflonfox_show_thumb_20100511194049_111_53.JPG',1)
        addDir('MLB on FOX','http://edge3.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=mlbonfoxonly&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/05/11/mlbonfox_show_thumb_20100511194216_111_53.JPG',1)
        addDir('NASCAR on FOX','http://edge4.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=waltrip&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/06/09/nascaronfox_show_thumb_20100609180644_111_53.JPG',1)
        addDir('Ticket to Ride','http://edge3.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=wheelsup&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2011/01/05/tickettoride_show_thumb_313x150_01_20110105181334240_111_53.JPG',1)
        addDir('Big 12','http://edge5.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=big12&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/05/11/big12_show_thumb_20100511194443_111_53.JPG',1)
        addDir('Pac 10','http://edge4.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=pac10&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/05/11/pac10_show_thumb_20100511194609_111_53.JPG',1)
        addDir('Beyond the Box Score','http://edge5.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=horrow&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/08/13/beyond-the-box-score_20100813172043_111_53.JPG',1)
        addDir('GMs Corner','http://edge4.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=lwb_gmcorner&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/05/11/gmscorner_show_thumb_20100511195433_111_53.JPG',1)
        addDir('Qs 2 B','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=lwb_qb&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/05/11/qs2b_show_thumb_20100511200737_111_53.JPG',1)
        addDir('Inside Call','http://edge3.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=insidecall&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/09/07/inside_call_show_thumb_20100907201223_111_53.JPG',1)
        addDir('Coach Speak','http://edge2.catalog.video.msn.com/videoByTag.aspx?ff=8a&ind=1&mk=us&ns=Fox%20Sports_Gallery&ps=100&rct=1,3&tag=coachspeak&vs=0&responseEncoding=xml&template=foxsports&p=gallery_en-us_foxsports_videosgallery','http://static.foxsports.com/content/fscom/img/2010/09/15/_730_20100915154744_111_53.JPG',1)

def getVideos(url):
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                   'Referer' : 'http://img.widgets.video.s-msn.com/v/4417.00/fl/player/current/player.swf'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulStoneSoup(link, convertEntities = BeautifulStoneSoup.XML_ENTITIES)
        videos = soup('videos')[0]('video')
        # for i in soup('videofile'):
            # try:
                # bitrate = i['bitrate']
                # formatcode = i['formatcode']
                # url = i.uri
            # except:
                # pass
            # print (formatcode, bitrate, url)
        for video in videos:
            name  = video('title')[0].string
            try:
                link = video('videofiles')[0]('videofile', attrs={'formatcode' : '103'})[0]('uri')[0].string
            except:
                link = video('videofiles')[0]('videofile', attrs={'formatcode' : '1003'})[0]('uri')[0].string
            desc = video('description')[0].string
            date = video('startdate')[0].string.split('T')[0]
            description = desc+'\n'+date
            duration = video('durationsecs')[0].string
            try:
                thumb = video('file', attrs={'formatcode' : "2009"})[0]('uri')[0].string
            except:
                thumb = video('file', attrs={'formatcode' : "2001"})[0]('uri')[0].string
            addLink(name,link,description,duration,thumb)


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


def addLink(name,url,description,duration,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot":description, "Duration":duration } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,iconimage,mode):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
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
    fss.Categories()

if mode==5:
    print""
    fss.Index(name)

if mode==6:
    print""
    fss.setVideoUrl(url) 
    
xbmcplugin.endOfDirectory(int(sys.argv[1]))