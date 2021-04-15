#!/usr/bin/python
import pymysql
import sys
import cgi

import cgitb
cgitb.enable()

print("Content-type: text/html\n")

print("<html><head>")
print("<title>COVID-19 Protein Homepage </title>")
print("<body>")

### Header and direction tabs
print("<h1>Food Compound, Nutrition and COVID-19 Protein Interactions</h1>")

print("<hr>")
print("<br>")

print("""<div id='nav_bar'>
		<nav>
		<a href='function1.py' style="background-color: #f0f0f0; width: 200px; padding: 10px; border: 25px #66757F;">Food Compound Rank</a>
		<a href='function1.py' style="background-color: #f0f0f0; width: 200px; padding: 10px; border: 25px #66757F;">Food Compound-Human Protein Interaction</a>
		<a href='function1.py' style="background-color: #f0f0f0; width: 200px; padding: 10px; border: 25px #66757F;">High-Impact Food for Viral Protection</a>
		<a href='function1.py' style="background-color: #f0f0f0; width: 200px; padding: 10px; border: 25px #66757F;">Age-Related Proteins</a>
		<a href='function1.py' style="background-color: #f0f0f0; width: 200px; padding: 10px; border: 25px #66757F;">StringDB</a>
		<a href='function1.py' style="background-color: #f0f0f0; width: 200px; padding: 10px; border: 25px #66757F;">User-Defined Query</a>
		</nav>
</div>""")


#Function Module


print("</body></html>")