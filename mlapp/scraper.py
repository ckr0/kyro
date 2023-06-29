def scraper(url):
    def clean_text(text):
        text = text.lower()                                  # lower-case all characters
        text =  re.sub(r'@\S+', '',text)                     # remove twitter handles
        text =  re.sub(r'http\S+', '',text)                  # remove urls
        text =  re.sub(r'pic.\S+', '',text) 
        text =  re.sub(r"[^a-zA-Z+']", ' ',text)             # only keeps characters
        text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text+' ')      # keep words with length>1 only
        text= re.sub("\s[\s]+", " ",text).strip()            # remove repeated/leading/trailing spaces
        return text
    from bs4 import BeautifulSoup
    import requests
    import re
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    tag = soup.body
    txt = ""
    for string in tag.strings:
        txt += string
    #print(txt)
    first = "Synopsis"
    last = "Don’t miss out on ET Prime stories!"
    f = str(re.escape(first))
    l = str(re.escape(last))
    final = re.findall(f+"(.*)"+l,txt)[0]
    #print(final)
    input_text = (clean_text(final))
    return input_text
