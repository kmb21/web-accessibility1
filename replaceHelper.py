from bs4 import BeautifulSoup
import tkinter as tk
import re
import html
from langdetect import detect_langs, DetectorFactory


def htmlTag(soup):
    """
    This function modifies the html tag at start of document.
    Adds a language attribute to the tag.
    Args:
        soup (Object): A beautiful soup object
    """
    html_tag = soup.html
    if "lang" not in html_tag.attrs:
        text = soup.get_text()
        # Detects the language probabilities
        DetectorFactory.seed = 0
        lang_probs = detect_langs(text)
        # Sorts the language probabilities in descending order
        lang_probs.sort(key=lambda x: x.prob, reverse=True)
        # Get the main language (highest probability)
        main_language = lang_probs[0].lang
        html_tag["lang"] = main_language
    
    
def headTag(soup):
    """
    Modifies the content within the head tag of the html document.
    Adds the standard style syntax for documents
    Args:
        soup (Object): A beautiful soup object
    """
    new_head_text = """
<title>Chapter Number Chapter title | Book Title</title>
<meta charset="utf-8">
<style>
body {
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
    """
    Summary: Searches the html file for a span tags with attribute font-weight: bold; style
    and replaces the span tag with a strong tag
    Args:
        soup (Object): A beautiful soup object
    """
    bold_tags = soup.find_all("span", style="font-weight:bold;") #searches for all span tags with
    #the font_weight: bold; 
    for tag in bold_tags:
        if tag.string is not None:
            new_tag = soup.new_tag('strong') #Creates a new strong tag
            new_tag.string = tag.string #Sets the content within the strong tag to the content of the span tag
            tag.replace_with(new_tag) #Replaces the span tag with the strong tag
        
        
    
def italicTag(soup):
    """
    Searches the html file for all span tags with font-style: italic; and replaces them with em tags
    Args:
        soup (Object): A beautiful soup object
    """
    bold_tags = soup.find_all("span", style="font-style:italic;")        
    for tag in bold_tags:
        if tag.string is not None:
            new_tag = soup.new_tag('em')
            new_tag.string = tag.string
            tag.replace_with(new_tag)
        
        
def standardSpan(soup):
    """_summary_
    Searches the html tag for span tags based on their class attribute. 
    It uses regular expressions to generate a pattern and optimize the search.
    Args:
        soup (Object): A beautiful soup object
    """
    spans_to_remove = soup.find_all('span', class_=re.compile('^font'))

# unwrap the identified spans from the HTML
    for span in spans_to_remove:
        span.unwrap()
        
    leftOverSpans = soup.find_all("span")
    for span in leftOverSpans:
        span.unwrap()
        
def spacingNSBP(soup): 
    """
    Replaces all &nsbp with a whitespace
    Args:
        soup (Object): A beautiful soup object
    """ 
    nbspOccurrences = soup.find_all(text=lambda text: text and ('\xa0' in text or '&nbsp;' in text))

    for occurrence in nbspOccurrences:
        # Replaces &nbsp; with a space
        occurrence.replace_with(occurrence.replace('\xa0', " ").replace('&nbsp;', " "))
        

def divTag(soup):
    """
    Searches the html document for <div> tags that contain only one child element
    Args:
        soup (Object): A beautiful soup object
    """
    divOccurrences = soup.find_all('div')
    for divTag in  divOccurrences:
        divTag.unwrap()
        
# def quotTags(soup):
#     """
#     Replaces all curly quotes with q tags
#     """
#     open_q_tag = soup.new_tag("q")
#     closing_q_tag = soup.new_tag("/q")
#     for text_node in soup.find_all(text=True):
#         text_node.replace_with(text_node.replace('“', '<q>').replace('”', '</q>'))


            
    

def superScriptTag(soup, seentags):
    ##when it finds a non numerical sup tag text, add a comment alerting the user to check it with original
    ##document
    """
    Adds ifnotes and fnotes to supercript tags
    Args:
        soup (Object): A beautiful soup object for the html file
        seentags (Dictionary): A dictionary storing the seen ifnotes to avoid instances of the same sup tags
                               pointing to different instances
    """
    sup_occurrences = soup.find_all('sup')

    for sup in sup_occurrences:
        sup_text = sup.text.strip()
        modified_sup_text = sup_text  # Used to hold any modified version of sup_text

        if sup_text in seentags:
            modified_sup_text += chr(96 + seentags[sup_text])  # Appending 'a', 'b', 'c', ...
            seentags[sup_text] += 1
        else:
            seentags[sup_text] = 1

        new_sup_tag = soup.new_tag('sup')
        a_tag = soup.new_tag('a', href=f"#fnote{modified_sup_text}", id=f"ifnote{modified_sup_text}")
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
    """
    Replaces all other un
    Args:
        soup (_type_): _description_
    """
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
    """
    Replaces ; with &colon;
    Not very necessary 
    """
    for text in soup.find_all(text=True):
        modified_text = text.replace(";", "&colon;")
        text.replace_with(modified_text)

def replaceCopySymbol(soup):
    """
    Replaces © symbol with Copyright symbol
    Args:
        soup (Object): Beautiful soup object for the html file
    """
    for text_node in soup.find_all(text=True):
        updated_text = text_node.replace('©', '&copy;')
        text_node.replace_with(updated_text)
        
def tableTags(soup):
    """
    Removes any td tags with a tthe vertical align: middle style
    Args:
        soup (Object): Beautiful soup object for the html file.
    """
    for td_tag in soup.find_all('td', style="vertical-align:middle;"):
        td_tag.unwrap()
        
def accents(soup):
    # Define a list of accented characters (you can expand this list if necessary)
    accented_chars = ['À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï',
                      'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'U+00d7', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß',
                      'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï',
                      'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ']

    for text_node in soup.find_all(text=True):
        if any(char in text_node for char in accented_chars): #Checks for any condition
            escaped_text = html.escape(text_node)
            text_node.replace_with(escaped_text)
    return soup

        
def mdash(soup):
    for text_node in soup.find_all(text=True):
        modified_text = text_node.replace('--', '&mdash;')
        text_node.replace_with(modified_text)
#add bibliography, 
#add &dollar;
#&percnt

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