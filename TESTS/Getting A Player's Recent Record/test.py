import urllib.request            # For importing the source code
import re                        # For separating out only relevant data
from pprint import pprint        # To show the messy html code as understandable text

dhawan = urllib.request.urlopen("http://www.espncricinfo.com/india/content/player/28235.html")  
                                 # 'dhawan' holds the source code of webpage now, but as a request page
dhawan_html = str(dhawan.read())                                                     
                                 # dhawan_html => The source code of Dhawan page, as a str object
in_file = open('dhawan_page.txt', 'w')                                               
in_file.write(dhawan_html)       # Writing that data to a file in case we require it later

dhawan_table = re.findall('<table class="engineTable">.*?</table>', dhawan_html) 
                                 # Extracts the table out of the html doc
print(len(dhawan_table))            # Hopefully cleanly prints to our screen, and it does
out_file = open('dhawan_recent.txt', 'w')
                                 # To store the table, actually not needed, but still if need arises
out_file.write(dhawan_table[3])
                                 # The webpage has 4 such tables, but our interest lies in only the 4th one
runs_list_tags = re.findall('<td class="left" nowrap="nowrap">[0-9]+</td>', dhawan_table[3])
                                 # We store all the tags that contain runs
pprint(runs_list_tags)           # Just for checking

runs = []
for tag in runs_list_tags:
   runs.append( int( re.findall('[0-9]+', tag)[0] ) )
   
pprint(runs)



# So, if given a player's html page we should be able to return a list containing his recent runs, and maybe also the bowling figures
