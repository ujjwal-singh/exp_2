#!C:/Python27/python

print "Content-Type: text/html"
print ""

import cgi
import MySQLdb

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
		db=MySQLdb.connect(host='localhost',user='root',passwd='',db='courses')
		cur=db.cursor()
		formData=cgi.FieldStorage()
		slot_no=formData.getvalue('slot_no')
		try:
			cur.execute('select * from slot where Slot_No=%s;',(slot_no))
			temp=cur.fetchall()[0][0]
			cur.execute('delete from slot where Slot_No=%s;',(slot_no))
			db.commit()
			print ''' <h2> Slot deleted successfully </h2> '''
		except:
			print ''' <h2> Invalid slot number </h2> '''
		print '''	<br> <br> <br> <br> <br> <br>  
					<h2>
						<br> <br> <br> <br> <br> <br>
						<a href='slot.py'> Go back </a> <br> <br>
						<a href='home.py'> Go to home </a>
					</h2> '''
		tail()
	except:
		cgi.print_exception()