#!C:/Python27/python

print "Content-Type: text/html"
print ""

import cgi

def head():
	print '''<html>
				<head>
					<title> Exp </title>
				</head>
				<body>'''
				
def tail():
	print '''</body>
			</html>'''
			
if __name__=="__main__":
	try:
		head()
		print ''' <h2> Student menu options </h2>
					<h3> 
						<a href='stud_form.py'> Register new student </a> <br> <br>
						<a href='stud_edit.py'> Edit a registered student's datails </a> <br> <br>
						<a href='stud_del.py'> Delete a student record </a> <br> <br> <br> <br> <br> <br> <br>
						<a href='home.py'> Go to Home </a>
					</h3> '''
		tail()
	except:
		cgi.print_exception()