import feedparser
import logging


Topics = []
Titles= [] 


logging.basicConfig(level=logging.DEBUG)

class NewsManager ():
    
    def __init__ (self):
        fp =open ("Resource.txt","r",encoding="utf-8")
        lines =fp.readlines()
        fp.close ()
        for line in lines :
            str_split = line.split(' ')
            titles =self.getRSSTitle(str_split[1])
            for title in titles:
                Topics.append (str_split[0])
                Titles.append (title)
                #print (str_split[0] , title)
                
    def getRSSTitle (self,url):

        news = feedparser.parse (url).entries[:]
        titles = []
        for new in news:
            titles.append (new ['title'])
        return titles

    def getAllTopicAndTitle(self) :
        return Topics,Titles
    def getTitleByTopic (self,Topic):

        researchTitle =[]
        
        for i in range (0,len (Topics)):
            if Topic == Topics[i]:
                researchTitle.append (Titles[i])

        return researchTitle
        
    def updateTitle (self):
        Topics.clear()
        Titles.clear()
        fp =open ("Resource.txt","r",encoding="utf-8")
        lines =fp.readlines()
        fp.close ()
        for line in lines :
            str_split = line.split(' ')
            titles =self.getRSSTitle(str_split[1])
            for title in titles:
                Topics.append (str_split[0])
                Titles.append (title)
 
        
    



