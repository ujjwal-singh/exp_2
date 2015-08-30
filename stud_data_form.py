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
		print ''' <h1> Student data </h1>
					<form action='stud_data.py' method='POST' >
						<p> Enter roll number </p>
						<input type='text' name='roll_no' autofocus required='required' /> <br> <br>
						<input type='submit' />
					</form> <br> <br> <br> <br>
					<h2>
						<a href='home.py'> Go to home </a>
					</h2> '''
		tail()
	except:
		cgi.print_exception()