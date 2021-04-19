# Name: Mark Haskins
# Date: 2/15/2021
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Title: Assingmentt 0602: Surf CDM
# Link to video: https://youtu.be/vtDdhBOdFV8

from urllib.request import urlopen, Request
from urllib.parse import urljoin
from html.parser import HTMLParser
from re import findall, sub
# used to count dictionary values in print statement
from collections import Counter


visited = set()
wordFrequencyDict = {}
userAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'      #My user agent 
url = 'https://law.depaul.edu/faculty-and-staff/'
urlLength = len(url)
stopWordList = [                                                                #Created stop word list to filter out trivial words
    'a', 'about', 'above', 'across', 'after', 'afterwards', 'again',
    'against', 'all', 'almost', 'alone', 'along', 'already', 'also',
    'although', 'always', 'am', 'among', 'amongst', 'amoungst',
    'amount', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone',
    'anything', 'anyway', 'anywhere', 'are', 'area', 'areas', 'around',
    'as', 'ask', 'asking', 'asked', 'asks', 'at', 'b', 'back', 'backed',
    'backing', 'backs' 'be', 'became', 'because', 'become', 'becomes',
    'becoming', 'been', 'before', 'began', 'beforehand', 'behind', 'being',
    'beings', 'best', 'better', 'below', 'beside', 'besides',
    'between', 'beyond', 'big', 'bill', 'both', 'bottom', 'but', 'by', 'c',
    'call', 'came', 'can', 'cannot', 'cant', 'case', 'cases', 'certain',
    'certainly', 'clear', 'clearly', 'come', 'computer', 'con', 'could',
    'couldnt', 'cry', 'd', 'de', 'describe', 'detail', 'did', 'differ',
    'different', 'differently', 'do', 'does', 'done', 'down', 'downed',
    'downing', 'downs', 'dr', 'due', 'during', 'e', 'each', 'early', 'eg',
    'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'end', 'ended',
    'ending', 'ends', 'enough', 'etc', 'even', 'evenly', 'ever', 'every',
    'everybody', 'everyone', 'everything', 'everywhere', 'except', 'f', 'face',
    'faces', 'fact', 'facts', 'far', 'felt', 'few', 'fifteen', 'fifty', 'fill',
    'find', 'finds', 'fire', 'first', 'five', 'for', 'former', 'formerly',
    'forty', 'found', 'four', 'from', 'front', 'full', 'fully', 'further',
    'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally',
    'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods',
    'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'groups', 'had',
    'h', 'had', 'has', 'hasnt', 'have', 'having', 'he', 'hence', 'her',
    'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself',
    'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however',
    'hundred', 'i', 'ie', 'if', 'important', 'in', 'inc', 'indeed',
    'interest', 'interested', 'interesting', 'interests', 'into', 'is',
    'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kind',
    'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last',
    'later', 'latest', 'latter', 'latterly', 'least', 'less', 'let',
    'lets', 'like', 'likely', 'long', 'longer', 'longest', 'ltd', 'm', 'made',
    'make', 'making', 'man', 'many', 'may', 'me', 'meanwhile', 'member',
    'members', 'men', 'might', 'mill', 'mine', 'more', 'moreover',
    'most', 'mostly', 'move', 'mr', 'mrs', 'ms', 'much', 'must', 'my',
    'myself', 'n', 'name', 'namely', 'necessary', 'need', 'needed', 'needing',
    'needs', 'neither', 'never', 'nevertheless', 'new', 'newer', 'newest',
    'next', 'nine', 'no', 'nobody', 'non', 'none', 'noone', 'nor', 'not',
    'nothing', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off',
    'often', 'old', 'older', 'oldest', 'on', 'once', 'one', 'only', 'onto',
    'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering',
    'orders', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out',
    'over', 'own', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps',
    'place', 'places', 'please', 'point', 'pointed', 'pointing', 'points',
    'possible', 'present', 'presented', 'presenting', 'presents', 'problem',
    'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 're', 'really',
    'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says',
    'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees',
    'serious', 'several', 'shall', 'she', 'should', 'show', 'showed', 'showing',
    'shows', 'side', 'sides', 'since', 'sincere', 'six', 'sixty', 'small',
    'smaller', 'smallest', 'so', 'some', 'somebody', 'somehow', 'someone',
    'something', 'sometime', 'sometimes', 'somewhere', 'state', 'states', 'still',
    'such', 'sure', 'system', 't', 'take', 'taken', 'ten', 'than',
    'that', 'the', 'their', 'them', 'themselves', 'then', 'thence',
    'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon',
    'these', 'they', 'thick', 'thin', 'thing', 'things', 'think', 'thinks',
    'third', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 'through',
    'throughout', 'thru', 'thus', 'to', 'today', 'together', 'too', 'took', 'top',
    'toward', 'towards', 'turn', 'turned', 'turning', 'turns', 'twelve', 'twenty',
    'two', 'u', 'un', 'under', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses',
    'v', 'very', 'via', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', 'way',
    'ways', 'we', 'well', 'wells', 'went', 'were', 'what', 'whatever', 'when',
    'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein',
    'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who',
    'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within',
    'without', 'work', 'worked', 'working', 'works', 'would', 'x', 'y', 'year',
    'years', 'yet', 'you', 'young', 'younger', 'youngest', 'your', 'yours',
    'yourself', 'yourselves', 'z', 'pm', 'am'
]

class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    dataList = []
    cDataSkip = ['script', 'style']                         #skips script and style elements from content data tags 

    def __init__(self, url):
        '''initializes parser, the url, and a list'''
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        '''collects hyperlink URLs in their absolute format'''
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:urlLength] == url:             #checks the URL to see if it is base URL 
                        # remove duplicates
                        self.links.append(
                            absolute) if absolute not in self.links else self.links     #won't append duplicate links

    def handle_data(self, data):
        '''method to handle html data, returns a list of words in data tags'''
        stripData = data.strip()
        replacePuncStripData = sub(r'[^\w\s]', '', stripData)                   #regex expression to remove punctuation
        removeDigits = sub(r'[0-9]', '', replacePuncStripData)                  #regrex expression to remove digits 
        if len(removeDigits) > 0 and self.lasttag not in self.cDataSkip:        #self.lasttag is a class variable in the HTML Parser class 
            splitList = removeDigits.split()
            self.dataList.extend(splitList)
            self.lowerCaseList(self.dataList)

    def lowerCaseList(self, dataList):
        '''function to return a lower case list'''
        self.dataList = [each_dataWord.lower()
                         for each_dataWord in self.dataList]

    def getLinks(self):
        '''returns hyperlinks URLs in their absolute format'''
        return self.links

    def getWordList(self):
        '''returns list of words with stop words removed'''
        self.wordListRemoveStopWords = [
            word for word in self.dataList if word not in stopWordList]  # extend method
        return self.wordListRemoveStopWords


def openWebPage(url, userAgent):
    '''function to open web page and return html as a string'''
    headers = {'User-Agent': userAgent}
    request = Request(url, headers=headers)
    with urlopen(request) as response:
        html = response.read().decode()
    return html


def frequency(dataList):
    '''function to create and return word frequency dictionary from list'''
    global wordFrequencyDict
    for word in dataList:
        if word not in wordFrequencyDict:
            wordFrequencyDict[word] = 0
        wordFrequencyDict[word] += 1
    return wordFrequencyDict


def analyze(url, userAgent):
    '''returns list of http links in url, in absolute format'''
    htmlContent = openWebPage(url, userAgent)
    collector = Collector(url)
    collector.feed(htmlContent)
    urlList = collector.getLinks()
    wordList = collector.getWordList()
    freq = frequency(wordList)
    return urlList


def crawl(url, userAgent):
    '''a recursive web crawler that calls analyze()
       on every visited web page'''
    global visited                      #intialize visted to an empty set
    visited.add(url)                    #add url to the set
    print(url)                            
    links = analyze(url, userAgent)

    for link in links:                  # recursively continue crawl from every link in links
        if link not in visited:         # # follow link only if not visited
            try:
                crawl(link, userAgent)
            except:
                pass

def printResults(set1, dict1):
    '''function to print results'''
    visitedLinkList = list(set1)
    print("Visited Links")
    print(*visitedLinkList, sep="\n")
    k = Counter(dict1)                          
    highestValues = k.most_common(25)               #most_common method from Counter class that returns top 25 values 
    print(f"Top 25 Most Common Words at {url}")
    txt1, txt2 = 'Word', 'Occurence'
    print(f'{txt1:<20}{txt2}')
    for i in highestValues:
        print(f'{i[0]:<20}{i[1]}')


def main():
    '''main function to crawl web page and print results'''
    crawl(url, userAgent)
    printResults(visited, wordFrequencyDict)

main()
