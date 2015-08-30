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
		print ''' <h2> Slot menu options </h2> <br> <br>
					<h3>
						<a href='slot_form.py'> Register new slot </a> <br> <br>
						<a href='slot_edit.py'> Edit a registered slot </a> <br> <br>
						<a href='slot_del.py'> Delete a slot </a> <br> <br> <br> <br> <br> <br>
						<a href='home.py'> Go to home </a> 
					</h3> '''
		tail()
	except:
		cgi.print_exception()