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
		print ''' <h1> New slot registration form </h1>
					<form action='slot_reg.py' method='POST'>
						<p> Enter slot number </p>
						<input type='text' name='slot_no' autofocus required='required' />
						<p> Enter day </p>
						<input type='text' name='day' required='required' />
						<p> Enter timing </p>
						<input type='text' name='timing' required='required' placeholder='e.g. 09:10:00' />
						<p> Enter venue </p>
						<input type='text' name='venue' required='required' /> <br> <br>
						<input type='submit' />
					</form> <br> <br> <br> <br> <br> <br>
					<h2>
						<a href='slot.py'> Go back </a> <br> <br>
						<a href='home.py'> Go to home </a>
					</h2> '''
		tail()
	except:
		cgi.print_exception()