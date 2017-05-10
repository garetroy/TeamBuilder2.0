import smtplib

from email.mime.text import MIMEText
from team import Team
from student import Student
from config_data import ConfigData

DEBUG = False
CSP = ", "

'''
Parsed the template email file into an email to be sent. 
	@params:
		filename - string the points to the template file
		reciever - a string that is inserted into the template
		sender - a string that is inserted into the tmeplate
	@returns:
		(string,string) - tuple with subject and body respectively
'''
def parse_email(filename,receiver,sender):
	hasSubject = False
	subject = ""
	body = ""
	keywords = {"[receiver]":receiver, "[sender]":sender}
	
	try:
		f = open(filename,'r')
		for line in f:
			if line.startswith('##'):
				pass
			elif not hasSubject:
				subject = line
				hasSubject = True
			else:
				body = body + line
		f.close()
	except Exception as e:
		print(e)

	for key,value in keywords.items():
		subject = subject.replace(key,value)
		body = body.replace(key,value)
	
	return (subject, body)


'''
Send email to members of team. Most paramters are gathered via the
config file. To change the smptp server, port, sender email, sender 
name, or template filename do so through the config file.
	@params:
		team - a team object
	@returns:
		boolean - true/false on success
'''
def send_email(team):
	cnfg = ConfigData()
	names = []
	emails = []
	emailstr = ""
	noerror = True

	for student in team.getMemberList():
		names.append(student.getName())
		emails.append(student.getEmail())

	parsed = parse_email(cnfg.email['Source'],CSP.join(names),cnfg.email['Name'])
	if(parsed[1] == "" or parsed[0] == ""):
		return False

	emailstr = CSP.join(emails)

	msg = MIMEText(parsed[1])
	msg['Subject'] = parsed[0]
	msg['From'] = cnfg.email['From']
	msg['To'] = emailstr

	s = smtplib.SMTP(cnfg.email['SMTPServer'],cnfg.email['Port'])
	try:
		if DEBUG:
			print(msg.as_string())
		else:
			s.sendmail(cnfg.email['From'], emailstr, msg.as_string())
	except SMTPRecipientsRefused as e:
		print("All recipients were refused: {}".format(emailstr))
		noerror = False
	except SMTPSenderRefused as e:
		print("The server refused from address: {}".format(cnfg.email['From']))
		noerror = False
	except SMTPDataError as e:
		print("Server replied with an unexpected error code")
		noerror = False
	except Exception as e:
		print("Error: {}".format(e))
		noerror = False
	finally:
		s.quit()

	return noerror

'''
Test method for inform.py, attempt to send email to sample students.
'''
def test_email():
	
	team = Team(3,4)
	s1 = Student("Jared Paeschke","mahananaka@gmail.com")
	s2 = Student("Garett Roberts","groberts@uoregonfakery.edu")
	s3 = Student("Alister Macguire","aom@uoregonfakery.edu")
	#s4 = Student("Howard Lin","howardl@uoregon.edu")
	team.insertStudent(s1)
	team.insertStudent(s2)
	team.insertStudent(s3)

	if(send_email(team)):
		print("ran correctly")
	else:
		print("didn't run as expected")

if __name__== "__main__":
	test_email()
