import smtplib

from email.mime.text import MIMEText
from team import Team
from student import Student
from config_data import ConfigData

DEBUG = False
MAXPORT = 65535 #port is 16bit unsigned

'''
Checks if that config contains valid values. This is not a rigourous check;
it checks only that strings are not empty and port is in correct range.
    @params:
        cnfg = a ConfigData configuation
    @return:
        boolean - valid or not
'''
def valid_config(cnfg):
    for key, value in cnfg.email.items():
        if key == "Port":
            if value < 0 or value > MAXPORT:
                return False
        else:
            if value == "":
                return False

    return True

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
    csp = ", "
    cnfg = ConfigData()
    names = []
    tolist = []
    tostr = ""
    noerror = True

    if not valid_config(cnfg):
        print("Missing or invalid config email entries");
        return False

    for student in team.getMemberList():
        names.append(student.getName())
        tolist.append(student.getEmail())

    parsed = parse_email(cnfg.email['Source'],csp.join(names),cnfg.email['Name'])
    if(parsed[1] == "" or parsed[0] == ""):
        return False

    tostr = csp.join(tolist)

    msg = MIMEText(parsed[1])
    msg['Subject'] = parsed[0]
    msg['From'] = cnfg.email['From']
    msg['To'] = tostr

    s = smtplib.SMTP(cnfg.email['SMTPServer'],cnfg.email['Port'])
    try:
        if DEBUG:
            print(msg.as_string())
        else:
            s.ehlo()
            s.starttls()
            s.login(cnfg.email['user'],cnfg.email['password'])
            s.sendmail(cnfg.email['From'], tolist, msg.as_string())
        
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
    s1 = Student("Jared Paeschke","jpaeschk@uoregon.edu")
    s2 = Student("Garett Roberts","groberts@uoregon.edu")
    s3 = Student("Alister Macguire","aom@uoregon.edu")
    s4 = Student("Howard Lin","jpaeschk85@uoregon.edu")
    team.insertStudent(s2)
    team.insertStudent(s3)
    team.insertStudent(s1)

    if(send_email(team)):
        print("ran correctly")
    else:
        print("didn't run as expected")

if __name__== "__main__":
    test_email()
