from RSS import NewsManager

newsManager = NewsManager ()



def researchByTopic(topic):
    newsManager.updateTitle()
    titles = newsManager.getTitleByTopic(topic)
    for title in titles:
        print (topic,title)
    return titles



if  __name__=='__main__':
    researchByTopic("財經")
    researchByTopic("3C")
    researchByTopic("國際")
    researchByTopic("武漢肺炎")
    
"""
fp =open ("Resource.txt","r",encoding="utf-8")

lines =fp.readlines()

for  line in lines:
    strs = line.split(' ')
    print ('title =',strs[0],strs[1])
newsManager = NewsManager ()
title,news = newsManager.getWuhanPeopleCount()

for new in news:
    print (title,new)

newsManager.getSocietyNews()
newsManager.getFinaceNews()
newsManager.getSportNews()
newsManager.getGlobalNews()
"""
