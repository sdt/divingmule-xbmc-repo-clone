import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.mdc')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )


def Categories():
        addDir('Adam Carolla','http://www.mydamnchannel.com/AdamCarolla',1,'http://content.MyDamnChannel.com/datastore/channels/ACSlogo032111210311095430.jpg')
        addDir('Animation Block','http://www.mydamnchannel.com/Animation_Block/Season_1/TasteofAnimationBlock_1191.aspx',1,'http://content.mydamnchannel.com/datastore/channels/abpmdcbanner100509103446.gif')
        addDir('Back On Topps','http://www.mydamnchannel.com/Back_On_Topps/Season_2/Ep1Rejuvenated_2238.aspx',1,'http://content.mydamnchannel.com/datastore/channels/backontopps070509122251.png')
        addDir('Celebrity Autobiograp…','http://www.mydamnchannel.com/Celebrity_Autobiography/Celebrity_Autobiography/WillForteReadsTommyLee_4721.aspx',1,'http://content.mydamnchannel.com/datastore/channels/celebbiobanner-1100510122421.jpg')
        addDir('Childrens Hospital','http://www.mydamnchannel.com/childrenshospital',1,'http://content.mydamnchannel.com/datastore/channels/chevergreenlogo101110010104.jpg')
        addDir('Cookin With Coolio','http://www.mydamnchannel.com/Cookin__with_Coolio/Cookin_with_Coolio/3SpinachEvenYourKidsWillEat_568.aspx',1,'http://content.mydamnchannel.com/datastore/channels/coolioheader2120810023147.jpg')
        addDir('Daily Grace','http://www.mydamnchannel.com/grace',1,'http://content.mydamnchannel.com/datastore/channels/dgbanner250810121229.jpg')
        addDir('Don Was','http://www.mydamnchannel.com/Don_Was/2010_Detroit_All_Star_Revue/IngrayImmigrantSong_6712.aspx',1,'http://content.mydamnchannel.com/datastore/channels/donwas070509122624.png')
        addDir('Easy To Assemble','http://www.mydamnchannel.com/Easy_to_Assemble/Season_2/EasyToAssemble1WhatsinStore_2978.aspx',1,'http://content.mydamnchannel.com/datastore/channels/etabannernew020610124008.jpg')
        addDir('Gigi','http://www.mydamnchannel.com/Gigi__Almost_American/Gigi_Episodes/Episode1SpeakLearnEnglish_6886.aspx',1,'http://content.mydamnchannel.com/datastore/channels/gigilogousa110211120900.jpg')
        addDir('Go Sukashi!','http://www.mydamnchannel.com/gosukashi',1,'http://content.mydamnchannel.com/datastore/channels/sukashibanner2011070211021726.jpg')
        addDir('Harry Shearer','http://www.mydamnchannel.com/harryshearer',1,'http://content.mydamnchannel.com/datastore/channels/hs-banner230810091642.jpg')
        addDir('Horrible People','http://www.mydamnchannel.com/Horrible_People/Season_1/Episode1_533.aspx',1,'http://content.mydamnchannel.com/datastore/channels/horriblepeople070509010037.png')
        addDir('The Iceman Chronicles','http://www.mydamnchannel.com/Iceman_Chronicles/The_Iceman_Chronicles/TheIcemanChroniclesEpisode1_4083.aspx',1,'http://content.mydamnchannel.com/datastore/channels/icemanlogo170210090306.jpg')
        addDir('Jimmy Kimmel','http://www.mydamnchannel.com/jimmykimmel',1,'http://content.mydamnchannel.com/datastore/channels/JKLchannellogo230511123521.jpg')
        addDir('Bruce McCall','http://www.mydamnchannel.com/Brucemccall',1,'http://content.mydamnchannel.com/datastore/channels/mccalllogo3290611025146.jpg')
        addDir('Mark Malkoff','http://www.mydamnchannel.com/markmalkoff',1,'http://content.mydamnchannel.com/datastore/channels/mm-faceban190810092137.jpg')
        addDir('Pilot Season','http://www.mydamnchannel.com/Pilot_Season/Pilot_Season/1ThatWasThenThisisNow_1350.aspx',1,'http://content.mydamnchannel.com/datastore/channels/pilotseasonbluest070509010411.png')
        addDir('Portlandia','http://www.mydamnchannel.com/Portlandia_s_Damn_Channel/Portlandia/PortlandiaDreamofthe90s_6661.aspx',1,'http://content.mydamnchannel.com/datastore/channels/portlandialogonodate120411084710.jpg')
        addDir('PromoSexual','http://www.mydamnchannel.com/promosexual',1,'http://content.mydamnchannel.com/datastore/channels/promosexual070509011250.png')
        addDir('Slacktory','http://www.slacktory.com',1,'')
        addDir('Spärhusen','http://www.mydamnchannel.com/Sparhusen/Sp%C3%A4rhusen/Sp%C3%A4rhusenEpisode1_2977.aspx',1,'http://content.mydamnchannel.com/datastore/channels/sparhusenbanner130909021559.jpg')
        addDir('Spinal Tap','http://www.mydamnchannel.com/spinaltap',1,'http://content.mydamnchannel.com/datastore/channels/spinaltapbanner040609093238.jpg')
        addDir('Spook House Dave!','http://www.mydamnchannel.com/spookhousedave',1,'http://content.mydamnchannel.com/datastore/channels/shdbannerlogo280610093317.jpg')
        addDir('Status Kill','http://www.mydamnchannel.com/Status_Kill/Status_Kill/StatusKillPart1LogIn_6221.aspx',1,'http://content.mydamnchannel.com/datastore/channels/skbannercamo051010074603.jpg')
        addDir('Stella','http://www.mydamnchannel.com/Stella/STELLA/Birthday_1110.aspx',1,'http://content.mydamnchannel.com/datastore/channels/stellabanner070509010902.png')
        addDir('SUBWAY Fresh Artists','http://www.mydamnchannel.com/subway',1,'http://content.mydamnchannel.com/datastore/channels/subfreshbanner070311102832.jpg')
        addDir('SUPEREGO','http://www.mydamnchannel.com/SUPEREGO/SUPEREGO/Episode1GonzoTherapy_5293.aspx',1,'http://content.mydamnchannel.com/datastore/channels/egobanner3300610123449.jpg')
        addDir('The Temp Life','http://www.mydamnchannel.com/thetemplife',1,'http://content.mydamnchannel.com/datastore/channels/templogonew061210094459.jpg')
        addDir('Versailles','http://www.mydamnchannel.com/Versailles/Versailles/VersaillesEpisode1_7043.aspx',1,'http://content.mydamnchannel.com/datastore/channels/versaillesbanner2200611074351.jpg')
        addDir('Wainy Days','http://www.mydamnchannel.com/Wainy_Days/Season_2/16ThePickup_494.aspx',1,'http://content.mydamnchannel.com/datastore/channels/wdblueban151110020037.jpg')
        addDir('Webventures...','http://www.mydamnchannel.com/Webventures_of_Justin_and_Alden/The_Webventures_of_Justin___Alden/TheWebventuresofJustinAldenEp1AQuestionableQuest_4573.aspx',1,'http://content.mydamnchannel.com/datastore/channels/TridentMDCChannelBanner2270410124344.jpg')
        addDir('You Suck at Photoshop','http://www.mydamnchannel.com/You_Suck_at_Photoshop/Season_1/YouSuckAtPhotoshop1DistortWarpandLayerEffects_1373.aspx',1,'http://content.mydamnchannel.com/datastore/channels/ysapfinger070509010726.png')

def getVideos(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.mydamnchannel.com/'),
                ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13')]
        response = urllib2.urlopen(req)
        link=response.read()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        videos = soup.findAll('li', attrs={'class' : "videolist clearfix "})
        for video in videos:
            name = video('img')[0]['alt']
            url = 'http://www.mydamnchannel.com'+video('a')[0]['href']
            try:
                thumb = video('img')[0]['src']
            except:
                thumb = ''
            addLink(name,url,2,thumb)


def setVideoUrl(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.mydamnchannel.com/'),
                ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13')]
        response = urllib2.urlopen(req)
        link=response.read()
        video = re.compile('so.addVariable\("thefile", "(.+?)"\)').findall(link)
        url = 'http://content.mydamnchannel.com/datastore/smallflvs/'+video[0]
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


def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable', 'true')
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
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
    setVideoUrl(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))