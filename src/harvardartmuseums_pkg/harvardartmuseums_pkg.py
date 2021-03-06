import pandas as pd
import json
import requests
import urllib3

def get_url_for_title(text, apikey):
    """
    This function writes a url(a string) for Harvard Art Museums API to get a dataset with all artwork titles that include a word chosen.
    
    Parameters
    ----------
    text: str
        A string that you wish to find in the titles of artwork
    apikey: str
        A string of your apikey, given by Harvard Art Museums;
        https://harvardartmuseums.org/collections/api
    
    Returns
    -------
    str
        A url to put into the get_title_classification() function, which will give you the dataset.
    
    Examples
    --------
    >>> from harvardartmuseums_pkg import harvardartmuseums_pkg
    >>> text = "cat"
    >>> apikey = "yourapikey"
    >>> harvardartmuseums_pkg.get_url_for_title(text, apikey)
    'https://api.harvardartmuseums.org/object?title=cat&apikey=yourapikey'
    """
    your_url = "https://api.harvardartmuseums.org/object?title=" + str(text) + "&apikey=" + str(apikey)
    return your_url




def get_title_classification(url):
    """
    Generates dataset of all artwork titles and their classifications that include a word chosen.
    
    Parameters
    ----------
    url : string
        A string of url, generated by get_url_for_title(text, apikey) function.
    
    Returns
    -------
    A dataframe
        The dataset of all artwork titles that include a word chosen and their classifications.
    
    Examples
    --------
    >>> from harvardartmuseums_pkg import harvardartmuseums_pkg
    >>> harvardartmuseums_pkg.get_title_classification('https://api.harvardartmuseums.org/object?title=cat&apikey=yourapikey')
    Output will be a pandas dataframe with two columns(title, classification). 
    """
    
    r = requests.get(url)
    data = r.json()
    records = data['records']
    info = data['info']

    titles = []
    classifications = []

    for record in records:
        title = record['title']
        titles.append(title)
        classification = record['classification']
        classifications.append(classification)
    
        df1 = pd.DataFrame(titles)
        df2 = pd.DataFrame(classifications)
        dataframe = pd.concat([df1, df2], axis = 1)
        dataframe.columns = ['title', 'classification']

    try:
        
        if (info['next']):
            nextpage = get_title_classification(info['next'])
            df = pd.concat([dataframe, nextpage])
            return df
    # If next page doesn't work, end function
    except:
        pass

    
    
    
def get_url_for_artist(country, gender, apikey):
    """
    This function writes a url(a string) for Harvard Art Museums API to get a dataset with all female or male artists who are from a country(culture).
    
    Parameters
    ----------
    country: str
        A string of a culture name that you wish to find in artists
    gender: str
        A string of gender (female/male) that you wish to find in artists
    apikey: str
        A string of your apikey, given by Harvard Art Museums;
        https://harvardartmuseums.org/collections/api
   
    Returns
    -------
    str
        A url to put into the get_artist() function, which will give you the dataset.
    
    Examples
    --------
    >>> from harvardartmuseums_pkg import harvardartmuseums_pkg
    >>> country='Dutch'
    >>> gender='male'
    >>> apikey = "yourapikey"
    >>> harvardartmuseums_pkg.get_url_for_artist(country, gender, apikey)
    'https://api.harvardartmuseums.org/person?apikey=yourapikey&q=culture%3ADutch%2C%20gender%3Amale'
    """
    your_url= 'https://api.harvardartmuseums.org/person?apikey=' + str(apikey) + "&q=culture%3A" + str(country) + "%2C%20gender%3A" + str(gender)
    return your_url




def get_artist(url):
    """
    Generates dataset of all female or male artists who are from a country(culture).
    
    Parameters
    ----------
    url : string
        A string of url, generated by get_url_for_artist(country, gender, apikey) function.
    
    Returns
    -------
    A dataframe
        The dataset of all female or male artists who are from a country(culture).
    
    Examples
    --------
    >>> from harvardartmuseums_pkg import harvardartmuseums_pkg
    >>> harvardartmuseums_pkg.get_artist('https://api.harvardartmuseums.org/person?apikey=d7a856a1-f4df-4726-958f-957b2762b17f&q=culture%3ADutch%2C%20gender%3Amale')
    Output will be a pandas dataframe with all the artists' information, such as gender, displayname, url, objectcount, birthplace, datebegin, dateend, culture, personid, deathplace. 
    """
    r = requests.get(url)
    data = r.json()
    records = data['records']
    info = data['info']
    d = pd.DataFrame.from_dict(records)
    df = d[['gender',"displayname", 'url', 'objectcount','birthplace',"datebegin","dateend","culture","personid","deathplace"]]

    try:
        if (info['next']):
            nextpage = get_artist(info['next'])
            new_df = pd.concat([df, nextpage])
            return new_df
    except:
        pass
    
    

def get_url_for_exhibition(after, before, apikey):
    """
    This function writes a url(a string) for Harvard Art Museums API to get a dataset with all exhibitions information, held in the selected years.
    
    Parameters
    ----------
    after: str
        A string of a starting year of a period when exhibitions were held
    before: str
        A string of an ending year of a period when exhibitions were held
    apikey: str
        A string of your apikey, given by Harvard Art Museums;
        https://harvardartmuseums.org/collections/api
    
    Returns
    -------
    str
        A url to put into the get_exhibitions() function, which will give you the dataset.
    
    Examples
    --------
    >>> from harvardartmuseums_pkg import harvardartmuseums_pkg
    >>> after = '1975'
    >>> before = '2005'
    >>> apikey = "yourapikey"
    >>> harvardartmuseums_pkg.get_url_for_exhibition(after, before, apikey)
    'https://api.harvardartmuseums.org/exhibition?after=1975&before=2005&apikey=yourapikey'
    """
    your_url= "https://api.harvardartmuseums.org/exhibition?after=" + after + "&before=" + before + "&apikey=" + apikey
    return your_url




def get_exhibitions(url):
    """
    Generates dataset of all exhibitions that were held in the selected period through get_url_for_exhibition(after, before, apikey) function.
    
    Parameters
    ----------
    url : string
        A string of url, generated by get_url_for_exhibition(after, before, apikey) function.
    
    Returns
    -------
    A dataframe
        The dataset of all exhibitions that were held in the selected period.
    
    Examples
    --------
    >>> from harvardartmuseums_pkg import harvardartmuseums_pkg
    >>> harvardartmuseums_pkg.get_exhibitions('https://api.harvardartmuseums.org/exhibition?after=1975&before=2005&apikey=yourapikey')
    Output will be a pandas dataframe with all the exhibitions' information, such as begindate, enddate, title, url, exhibitionid. 
    """
    r = requests.get(url)
    data = r.json()
    records = data['records']
    info = data['info']
    d = pd.DataFrame.from_dict(records)
    df = d[['begindate', 'enddate','title','url', 'exhibitionid']]

    try:
        if (info['next']):
            nextpage = get_exhibitions(info['next'])
            new_df = pd.concat([df, nextpage])
            return new_df
    except:
        pass