'''
@author Jared Paeschke
created: Fri May 12, 2017

inform takes a Team of Students and emails them a notification that
they have been placed on a team together.

Modifications:

Jared Paeschke on May 14,
Created prompt for username and password.
'''

import os
import smtplib
import getpass
import argparse

from email.mime.text import MIMEText
from team import Team
from student import Student
from config_data import ConfigData

curpath    = os.path.dirname(os.path.abspath(__file__))

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

    targetfile = curpath + "/" + filename
    try:
        f = open(targetfile,'r')
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
def send_email(team, usr="", passwrd=""):
    csp = ", "
    cnfg = ConfigData()
    names = []
    tolist = []
    tostr = ""
    noerror = True

    if not valid_config(cnfg):
        print("Missing or invalid config email entries");
        return False

    for student in team.members:
        names.append(student.name)
        tolist.append(student.email)

    parsed = parse_email(cnfg.email['Source'],csp.join(names),cnfg.email['Name'])
    if(parsed[1] == "" or parsed[0] == ""):
        return False

    tostr = csp.join(filter(None,tolist))

    msg = MIMEText(parsed[1])
    msg['Subject'] = parsed[0]
    msg['From'] = cnfg.email['From']
    msg['To'] = tostr

    s = smtplib.SMTP(cnfg.email['SMTPServer'],cnfg.email['Port'])
    try:
        s.ehlo()
        s.starttls()
        if usr == "" or passwrd == "":
            usr = input('Login: ')
            passwrd = getpass.getpass()
            
        index = usr.find("@")
        if index != -1:
            usr = usr[:index]

        s.login(usr,passwrd)
        if DEBUG:
            print(msg.as_string())
        else:
            s.sendmail(cnfg.email['From'], tolist, msg.as_string())
        
    except Exception as e:
        print("Error: {}".format(e))
        noerror = False
    finally:
        s.quit()

    return noerror

'''
Parses the output file from the team builder program to retrieve the
teams and the member names and email addresses for each member.
    @params:
        file - file to be parsed
    
    @returns
        teams - a list of Team Objects
'''
def parse_team_file(file):
    member_lines = False
    teams = []
    min = 10
    max = 15
    t = Team(min,max)
    try:
        f = open(file,'r')
        for line in f:
            if member_lines:
                if line.startswith('\n'):
                     member_lines = False
                     teams.append(t)
                else:
                     email_split = line.split(';')
                     name_split = email_split[0].split()
                     
                     if email_split[1] == '\n':
                         email_split[1] = ''
                     
                     fn = name_split[2].strip()
                     ln = name_split[1].strip()
                     em = email_split[1].strip()
                     
                     s = Student(fn + ' ' + ln[:-1], em) #chop off the ',' in ln
                     t.insertStudent(s)
            else:
                if line.startswith('members'):
                    member_lines = True
                    t = Team(min,max)
        f.close()
    except Exception as e:
        print(e)

    return teams

'''
Sends email to teams, usuable via cmdline. 
    @Params
        args - an Argument parser
    @returns
        void
'''
def send_email_cmdline(args):
    member_lines = False
    targetfile = curpath + '/' + args.team_output
    teams = parse_team_file(targetfile)
    
    usr = input('Username: ')
    pswd = getpass.getpass()
    
    print('Sending emails, this may take several seconds...\n')
    for t in teams:
        send_email(t,usr,pswd)

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

    if not send_email(team):
        print("didn't run as expected")

if __name__== "__main__":
    if DEBUG:
        test_email()
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument('team_output', help='An output file from the team builder, path is relative to inform.py.')
        args       = parser.parse_args()
        send_email_cmdline(args)
