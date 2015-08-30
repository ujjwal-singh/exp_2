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
		roll_no=formData.getvalue('roll_no')
		try:
			cur.execute('select Name,Dept_Code,Course_No from student where Roll_no=%s;',(roll_no))
			all=cur.fetchall()
			name=all[0][0]
			dept_code=all[0][1]
			course_no=all[0][2]
			dept_name=""
			try:
				cur.execute('select Dept_Name from department where Dept_Code=%s;',(dept_code))
				all=cur.fetchall()
				dept_name=all[0][0]
			except:
				dept_name="Department not registered  (Dept. code -- "+dept_code+")" 
			print ''' <h2> Student record </h2> '''
			print ''' <table border='1' style='width:60%'>
					<tr>
						<td> Name -- {name} </td>
						<td> Roll no. -- {roll_no} </td>
					</tr>
					<tr>
						<td> Department -- {dept_name} </td>
						<td> </td>
					</tr>
				 </table> '''.format(**locals())

#		print ''' <p> Student Name   -- {name} </p> 
#				 <p> Department Name -- {dept_name} </p>'''.format(**locals())

			print ''' <h2> Courses </h2> '''
			print ''' <table border='1' style='width:60%' >
					<tr>
						<td> Serial no. </td>
						<td> Course Name </td>
						<td> Instructor </td>
					</tr> '''
			i=1
			l=course_no.split(",")
			for course_no in l:
				course_name=""
				instructor=""
				try:
					cur.execute('select Course_Name,Instructor from course where Course_No=%s;',(course_no))
					all=cur.fetchall()
					course_name=all[0][0]
					instructor=all[0][1]
				except:
					course_name="Course not registered  (Course code -- "+course_no+")"
					instructor="Course not registered  (Course code -- "+course_no+")"
				print ''' <tr>
							<td> {i} </td>
							<td> {course_name} </td>
							<td> {instructor}  </td>
						</tr> '''.format(**locals())
				i+=1
			print ''' </table> '''
		
#			print ''' <p> Course Name -- {course_name} </p>
#					  <p> Instructor  -- {instructor}  </p> '''.format(**locals())
#		print ''' <p> {name} </p> 
#				 <p> {dept_name} </p>'''.format(name=name,dept_name=dept_name)
		except:
			print ''' <h2> Student not registered </h2> '''
		print ''' <br> <br> <br> <br>
					<h2>
						<a href='stud_data_form.py'> Go back </a> <br> <br>
						<a href='home.py'> Go to home </a>
					</h2> '''
		tail()
	except:
		cgi.print_exception()