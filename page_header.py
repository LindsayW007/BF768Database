#!/usr/bin/python
import pymysql
import sys
import cgi

import cgitb
cgitb.enable()

print("Content-type: text/html\n")

print("<html>")
print("""<head>
	<title>COVID-19 Protein Homepage </title>
	<style>
	.help{
	position:relative;
	top:-20px;
	right:0px;
	background-color: #8ebf42;
	color: #000000;
	padding: 7px;
	line-height:40px;
	font-size:15px;
	white-space:nowrap;
	}
	
	.text{
	position:relative;
	top: -20px;
	background-color: #D3D3D3;
	line-height:40px;
	color:#000000;
	padding: 7px;
	font-size:15px;
	white-space:nowrap;
	}
	
	h1{
	background-color: #93BFEA;
	font-size:35px;
	text-align:center;
	padding: 20px;
	}
	
	p{
	font-style:normal;
	font-weight:normal;
	font-size:15px;
	}
	
	table {
	font-size: 15px;
    border-collapse: collapse;
    border-spacing: 0;
    width: 100%;
    }

    th, td {
    font-size: 15px;
  	border: none;
  	text-align: left;
  	padding: 8px;
	}

	tr:nth-child(even){
	font-size: 15px;
	background-color: #f2f2f2
	}

	th {
	font-size: 15px;
  	background-color: #4CAF50;
  	color: white;

	</style>
	</head>""")
print("<body>")

#Header for the database, could be a hyperlink back to the homepage 
print("""<h1><br><a style='text-decoration: none; color:#000000;' class='title' 
href='https://bioed.bu.edu/cgi-bin/students_21/ziyiwang/homepage.py'>
Food Compound, Nutrition and COVID-19 Protein Interactions</a></h1>""")
print("<hr>")
print("<br>")

print("""<div id='nav_bar' class='navigation'>
		<nav>
		<a class='text' href='https://bioed.bu.edu/cgi-bin/students_21/xwang30/occurence1.py'>Food Compound Occurence Rank</a>
		<a class='text' href='https://bioed.bu.edu/cgi-bin/students_21/xwang30/interaction2.py'>Food Compound-Human Protein Interaction</a>
		<a class='text' href='https://bioed.bu.edu/cgi-bin/students_21/llouck01/food_download.py'>High-Impact Food for Viral Protection</a>
		<a class='text' href='https://bioed.bu.edu/cgi-bin/students_21/ziyiwang/vhi_string.py'>VHI-Relationship</a>
		<a class='text' href='https://bioed.bu.edu/cgi-bin/students_21/ziyiwang/age_protein.py'>Age-Related Proteins</a>
		<a class='help' href='https://bioed.bu.edu/cgi-bin/students_21/llouck01/help_page.py' target='_blank'>Help Manual</a>
		</nav>
</div>""")

