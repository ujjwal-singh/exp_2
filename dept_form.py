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
		print ''' 
					<form action='dept_reg.py' method='POST' >
						<p> Enter department code </p>
						<input type='text' name='dept_code' autofocus required='required' /> <br>
						<p> Enter department name </p>
						<input type='text' name='dept_name' required='required' /> <br> <br>
						<input type='submit' />
					</form> 
					<h3>
						<br> <br> <br> <br>
						<a href='dept.py'> Go back </a> <br> <br>
						<a href='home.py'> Go to home </a>
					</h3> '''
		tail()
	except:
		cgi.print_exception()