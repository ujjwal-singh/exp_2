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
		print ''' <form action='slot_edit_info.py' method='POST' >
					<h2> Enter slot number </h2>
					<input type='text' name='slot_no' autofocus required='required' /> <br> <br>
					<input type='submit' />
					<h2>
						<br> <br> <br> <br> <br> <br>
						<a href='slot.py'> Go back </a> <br> <br>
						<a href='home.py'> Go to home </a>
					</h2> '''
		tail()
	except:
		cgi.print_exception()