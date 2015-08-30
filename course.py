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
		print ''' <h2> Course menu options </h2> <br> <br> </h2>
					<h3>
						<a href='course_form.py'> Register new course </a> <br> <br>
						<a href='course_edit.py'> Edit a course </a> <br> <br>
						<a href='course_del.py'> Delete a course </a> <br> <br> <br> <br> <br> <br>
						<a href='home.py'> Go to home </a>
					</h3> '''
		tail()
	except:
		cgi.print_exception()