import urllib,urllib2,re,xbmcplugin,xbmcgui

#TV DASH - by You 2008.

#def CATEGORIES():
        #addDir('Alaska HDTV','http://feeds.feedburner.com/alaskahdtv',1,'http://www.alaskahdtv.com/dropbox/ID3s/Alaska-HDTV-ID3.jpg')
                       
def INDEX(url):
        url = 'http://feeds.feedburner.com/alaskahdtv'
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        link=response.read()
        code=re.sub('\r','',link)
        code=re.sub('\n',' ',code)
        code=re.sub('\t',' ',code)
        code=re.sub('  ','',code)
        code=re.sub('\xef\xac\x81','',code)
        code=re.sub('&lt','',code)
        code=re.sub('&amp',' ',code)
        code=re.sub(';#160;','',code)
        code=re.sub(';quot;','"',code)
        response.close()
        plot=re.compile('</itunes:summary><description>(.+?);br').findall(code)
        match=re.compile('<media:content url="(.+?)" fileSize=".+?" type="video/mp4" />').findall(code)
        name=re.compile('<item><title>(.+?)</title><link>.+?</link><pubDate>.+?</pubDate>').findall(code)
        for index in range(len(match)):
                addLink(name[index],match[index],plot[index],'')

      
               
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




def addLink(name,url,iconimage,plot):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="http://www.alaskahdtv.com/dropbox/ID3s/Alaska-HDTV-ID3.jpg", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot": plot } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
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

if mode==None or url==None or len(url)<1:
        print ""
        INDEX(url)
       
elif mode==1:
        print ""+url
        INDEX(url)
        
elif mode==2:
        print ""+url
        VIDEOLINKS(url,name)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
