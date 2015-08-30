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
		print ''' <h1> New course registration form </h1>
					<form action='course_reg.py' method='POST'>
						<p> Enter course number </p>
						<input type='text' name='course_no' autofocus required='required' />
						<p> Enter course name </p>
						<input type='text' name='course_name' required='required' />
						<p> Enter instructor name </p>
						<input type='text' name='inst_name' required='required' />
						<p> Enter slot </p>
						<input type='text' name='slot' required='required' /> <br> <br>
						<input type='submit' />
					</form> <br> <br> <br> <br> <br> <br>
					<h3>
						<a href='course.py'> Go back </a> <br> <br>
						<a href='home.py'> Go to home </a>
					</h3> '''
		tail()
	except:
		cgi.print_exception()