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
		old_slot_no=formData.getvalue('old_slot_no')
		slot_no=formData.getvalue('slot_no')
		day=formData.getvalue('day')
		timing=formData.getvalue('timing')
		venue=formData.getvalue('venue')
		try:
			cur.execute('delete from slot where Slot_No=%s;',(old_slot_no))
			cur.execute('insert into slot values(%s,%s,%s,%s);',(slot_no,day,timing,venue))
			db.commit()
			print ''' <h2> Slot details edited successfully. </h2> '''
		except:
			print ''' <h2> Slot number already registered </h2> '''
		print'''    <h2>
						<br> <br> <br> <br>
						<a href='slot.py'> Go back </a> <br> <br>
						<a href='home.py'> Go to home </a>
					</h2> '''
		tail()
	except:
		cgi.print_exception()