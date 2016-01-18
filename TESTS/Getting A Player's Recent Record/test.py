import urllib.request            # For importing the source code
import re                        # For separating out only relevant data
from pprint import pprint        # To show the messy html code as understandable text

dhawan = urllib.request.urlopen("http://www.espncricinfo.com/india/content/player/28235.html")  
                                 # 'dhawan' holds the source code of webpage now, but as a request page
dhawan_html = str(dhawan.read())                                                     
                                 # dhawan_html => The source code of Dhawan page, as a str object
in_file = open('dhawan_page.txt', 'r')                                               
in_file.write(dhawan_html)       # Writing that dtaa to a file in case we require it later

small_segment = re.findall('<table/sclass="engineTable">.*?</table>', dhawan_html) 
                                 # Extracts the table out of the html doc
pprint(small_segment)            # Hopefully cleanly prints to our screen
