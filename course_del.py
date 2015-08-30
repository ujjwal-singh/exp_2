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
		print ''' <h3> Enter course number </h3>
					<form action='course_del_done.py' method='POST'>
						<input type='text' name='course_no' autofocus required='required' /> <br> <br>
						<input type='submit'/>
					</form> <br> <br> <br> <br> <br> <br>
				<h3>
					<a href='course.py'> Go back </a> <br> <br>
					<a href='home.py'> Go to home </a>
				</h3> '''
		tail()
	except:
		cgi.print_exception()