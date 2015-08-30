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
			all=cur.fetchall()
			print ''' <form action='slot_edit_done.py' method='POST' >
						<h2> Old information </h2>
						<p> Slot number </p>
						<input type='text' name='old_slot_no' value='{all[0][0]}' readonly='readonly' />
						<p> Day </p>
						<input type='text' name='old_day' value='{all[0][1]}' readonly='readonly' />
						<p> Timing </p>
						<input type='text' name='old_timing' value='{all[0][2]}' readonly='readonly' />
						<p> Venue </p>
						<input type='text' name='old_venue' value='{all[0][3]}' readonly='readonly' /> <br> <br>
						<h2> New information </h2>
						<p> Slot number </p>
						<input type='text' name='slot_no' value='{all[0][0]}' autofocus required='required' />
						<p> Day </p>
						<input type='text' name='day' value='{all[0][1]}' required='required' />
						<p> Timing </p>
						<input type='text' name='timing' value='{all[0][2]}' required='required' />
						<p> Venue </p>
						<input type='text' name='venue' value='{all[0][3]}' required='required' /> <br> <br>
						<input type='submit' />
					  </form> '''.format(**locals())
		except:
			print ''' <h2> Invalid slot number </h2> '''
		print'''    <h2>
						<br> <br> <br> <br>
						<a href='slot.py'> Go back </a> <br> <br>
						<a href='home.py'> Go to home </a>
					</h2> '''
		tail()
	except:
		cgi.print_exception()