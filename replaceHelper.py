from bs4 import BeautifulSoup
import re
from langdetect import detect, detect_langs


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
<head>
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
</head>"""
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
    
    quot_occurrences = soup.find_all(text="&quot;")
    
    for i in range(len(quot_occurrences)):
        occurrence = quot_occurrences[i]
        if i%2 == 0:          
        # Replaces &quot; with <q>
            occurrence.replace_with(occurrence.replace("&quot;", '<q>'))
        else:
            occurrence.replace_with(occurrence.replace("&quot;", '</q>'))
            
    

def superScriptTag(soup, fnote_dict):
    sup_occurrences = soup.find_all('sup')
    #TODO: To boe continued
    fnote_dict = {}
    fnote_count = 1

    for sup in sup_occurrences:
        sup_text = sup.text.strip()

        if sup_text.isdigit():
            if sup_text not in fnote_dict:
                fnote_dict[sup_text] = chr(fnote_count + 96)  # Use lower case letters as characters
                fnote_count += 1
                temp = ""
            else:
                temp = chr()

            sup.replace_with(soup.new_tag('sup').append(soup.new_tag('a', href="#fnote"+sup_text, id="ifnote"+sup_text).string(fnote_dict[sup_text])))
        else:
            if sup_text in fnote_dict:
                sup.replace_with(soup.new_tag('sup').append(soup.new_tag('a', href="#fnote"+str(fnote_count), id="ifnote"+str(fnote_count)).string(fnote_dict[sup_text])))
                fnote_count += 1
            else:
                sup.replace_with(soup.new_tag('sup').append(soup.new_tag('a', href="#fnote"+str(fnote_count), id="ifnote"+str(fnote_count)).string(sup_text)))
                fnote_dict[sup_text] = chr(fnote_count + 96)  # Use lower case letters as characters
                fnote_count += 1
                
        

def imgTag(soup):
    img_tags = soup.find_all('img')

    for img in img_tags:
        
        if not img.has_attr('alt') or img['alt'] == '':
            # Add 'alt' attribute with an empty value
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
        

def bookmarks(soup):
    bookmark_tags = soup.find_all('a', {'name': lambda x: x and x.startswith('bookmark')})
    
    for bookmark_tag in bookmark_tags:
        bookmark_tag.unwrap()
        

            
def saveFile(soup):
    with open('output.html', 'w') as file:
        file.write(str(soup))


if __name__ == "__main__":
    pass