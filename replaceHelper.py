from bs4 import BeautifulSoup
import tkinter as tk
import re
from langdetect import detect_langs


def htmlTag(soup):
    html_tag = soup.html
    if "lang" not in html_tag.attrs:
        text = soup.get_text()
        # Detects the language probabilities
        lang_probs = detect_langs(text)
        # Sorts the language probabilities in descending order
        lang_probs.sort(key=lambda x: x.prob, reverse=True)
        # Get the main language (highest probability)
        main_language = lang_probs[0].lang
        html_tag["lang"] = main_language
    
    
def headTag(soup):
    new_head_text = """
<title>Chapter Number Chapter title | Book Title</title>
<meta charset="utf-8">
<style>
body {
    font-size: 16px;
    font-family: Verdana, "sans-serif";
} p {
    line-height: 1.5em;
} ul {
    list-style-type:none;
} .bib {
text-indent:-2em;
margin-left:0em;
line-height: 1.5em;
    }
</style>
"""
    head_tag = soup.head

    # Clears the existing content within the head tag
    head_tag.clear()

    # Appends the new head text to the head tag
    head_tag.append(BeautifulSoup(new_head_text, 'html.parser'))
    
    

def strongTag(soup):
    bold_tags = soup.find_all("span", style="font-weight:bold;")
    for tag in bold_tags:
        if tag.string is not None:
            new_tag = soup.new_tag('strong')
            new_tag.string = tag.string
            tag.replace_with(new_tag)
        
        
    
def italicTag(soup):
    bold_tags = soup.find_all("span", style="font-style:italic;")        
    for tag in bold_tags:
        if tag.string is not None:
            new_tag = soup.new_tag('em')
            new_tag.string = tag.string
            tag.replace_with(new_tag)
        
        
def standardSpan(soup):
    spans_to_remove = soup.find_all('span', class_=re.compile('^font'))

# unwrap the identified spans from the HTML
    for span in spans_to_remove:
        span.unwrap()
        
    leftOverSpans = soup.find_all("span")
    for span in leftOverSpans:
        span.unwrap()
        
def spacingNSBP(soup):   
    nbspOccurrences = soup.find_all(text=lambda text: text and ('\xa0' in text or '&nbsp;' in text))

    for occurrence in nbspOccurrences:
        # Replaces &nbsp; with a space
        occurrence.replace_with(occurrence.replace('\xa0', " ").replace('&nbsp;', " "))
        

def divTag(soup):
    divOccurrences = soup.find_all('div')
    for divTag in  divOccurrences:
        divTag.unwrap()
        
def quotTags(soup):
    ## CHANGE FUNCTIONALIT. Abby does not add &quot; to document.
    
    quot_occurrences = soup.find_all(text="&quot;")
    
    for i in range(len(quot_occurrences)):
        occurrence = quot_occurrences[i]
        if i%2 == 0:          
        # Replaces &quot; with <q>
            occurrence.replace_with(occurrence.replace("&quot;", '<q>'))
        else:
            occurrence.replace_with(occurrence.replace("&quot;", '</q>'))
            
    

def superScriptTag(soup, seentags):
    ##when it finds a non numerical sup tag text, add a comment alerting the user to check it with original
    ##document
    sup_occurrences = soup.find_all('sup')

    for sup in sup_occurrences:
        sup_text = sup.text.strip()

        if sup_text in seentags:         
            sup_text += chr(96 + seentags[sup_text])  # Appending 'a', 'b', 'c', ...
            seentags[sup_text] += 1
        else:
            seentags[sup_text] = 1

        new_sup_tag = soup.new_tag('sup')
        a_tag = soup.new_tag('a', href=f"#fnote{sup_text}", id=f"ifnote{sup_text}")
        a_tag.string = sup_text
        new_sup_tag.append(a_tag)

        sup.replace_with(new_sup_tag)

   
        

def imgTag(soup):
    #img should be enclosed in a figure tag and figcaption should be commented
    
    img_tags = soup.find_all('img')

    for img in img_tags:
        
        if not img.has_attr('alt') or img['alt'] == '':
            # Adds 'alt' attribute with an empty value
            img['alt'] = ""
            
def unnecessaryTags(soup):
    tag_replacements = {
    'div': '',
    'b': 'strong',
    'i': 'em',
    'emptytag': '',
    }

    for old_tag, new_tag in tag_replacements.items():
        tags = soup.find_all(old_tag)
        for tag in tags:
            if tag.string is not None:
                new_tag_obj = soup.new_tag(new_tag)
                # Transfer the contents of the old tag to the new tag
                new_tag_obj.string = tag.string
                tag.replace_with(new_tag_obj)
                


def brTags(soup):
    br_tags = soup.find_all("br", {"clear": "all"})
    
    for br_tag in br_tags:
        br_tag.unwrap()
        

def replaceEllipsis(soup):
    for text in soup.find_all(text=True):
        modified_text = text.replace("...", "&hellip;")
        text.replace_with(modified_text)

def replaceSemicolon(soup):
    ##No that common
    ##
    for text in soup.find_all(text=True):
        modified_text = text.replace(";", "&colon;")
        text.replace_with(modified_text)
  
##look for copy right symbols and replace with &copy;
#add bibliography, 
##for tables, remove td tags with style attribute\
##mdash is -- sometimes, so search for instances of this
##Check for accents and replace the accordingly.
##see you can figure out what to do regarding end of page

def bookmarks(soup):
    bookmark_tags = soup.find_all('a', {'name': lambda x: x and x.startswith('bookmark')})
    
    for bookmark_tag in bookmark_tags:
        bookmark_tag.unwrap()
        

            
def saveFile(soup, path):
    with open(path, 'w') as file:
        file.write(str(soup))


if __name__ == "__main__":
    pass