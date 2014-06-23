from bs4 import BeautifulSoup
import requests
import json
 
 
"""
FUNCTION: 
            scrapeMemberNames
PARAMETERS: 
            url : str
            do not forget quotation marks
            Utilize meetup.com's members API to access members database of groups.
            Input whatever parameters into API console 
                group_urlname: PyLadies (unique name in group's URL)
                page: 200 (number of entries to include)
                only: name (only return member name)
            Utilize returned signed URL
RETURNS:
            listonames : List of names to traverse through
        
EXAMPLE: 
            scrapeMemberNames('') # insert API url inside this quote
            output: [u'Alison Link',
                     u'Angie',
                     u'Anna Mandy', .....]
 
"""
def scrapeMemberNames(url):
    listonames = list() #create empty list; to return
    
    #extract all text from page
    rawdata    = requests.get(url).text
    #put all text into a BeautifulSoup Object
    souped     = BeautifulSoup(rawdata) 
    #isolate everything contained in <p></p>
    ptag       = souped.p.string 
    #convert json dictionary into python dictionary
    diction    = json.loads(ptag)
    #isolate data stored by 'results' key
    ourresults = diction['results']
 
    #loop through 'results' through every 'name' element and append each corresponding datum to list
    for name in ourresults:
        listonames.append(name['name'])
        
    return listonames
 
#Example code, lists all members of PyLadies
scrapeMemberNames('') # insert API url inside this quote