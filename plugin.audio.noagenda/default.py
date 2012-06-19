import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup

addon = xbmcaddon.Addon(id='plugin.audio.noagenda')
home = addon.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )


def makeRequest(url):
        try:
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            link = response.read()
            response.close()
            return link
        except urllib2.URLError, e:
            print 'We failed to open "%s".' % url
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            if hasattr(e, 'code'):
                print 'We failed with error code - %s.' % e.code
                xbmc.executebuiltin("XBMC.Notification(No Agenda,HTTP Error: "+str(e.code)+",5000,"+icon+")")

def main():
        soup = BeautifulStoneSoup(makeRequest('http://www.mevio.com/feeds/noagenda.xml'),
                                  convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        for i in soup('item'):
            mp3_url = i.guid.string
            desc = i.description.contents[0]
            d_soup = BeautifulSoup(desc, convertEntities=BeautifulSoup.HTML_ENTITIES)
            name = d_soup.p.contents[0]+': '+d_soup.p.contents[2]
            thumb = d_soup.img['src']
            liz=xbmcgui.ListItem(name, iconImage=thumb, thumbnailImage=thumb)
            liz.setInfo( type="Audio", infoLabels={ "Title": name } )
            liz.setProperty('mimetype', 'audio')
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=mp3_url,listitem=liz)
            
main()

xbmcplugin.endOfDirectory(int(sys.argv[1]))