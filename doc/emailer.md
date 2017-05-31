## Inform Teams

  After you have created teams it is natural that you will want notify
  those individuals on the team who their new teammates are. In this project
  we have included a simple text only emailer to handle this for you. You can
  do this through cmdline or through the GUI that has been created. 
  Regardless of how you wish to use the emailer you must first configure the
  email settings in the config directory.

### Configure

  To configure the emailer find the config.json file located within the config
  directory. Open this and locate the email settings. The following is an 
  explanation of each setting.

  ```
  Name:         the name you want to appear in the message as the sender.
  From:         the email address you are using to send out the emails.
  Source:       this points to the email template that is used for the email.
  SMTPServer:   the SMTP server that you want to use.
  Port:         the port of the SMTP server.
  ```

### Command Line Usage

  To email the created teams you will want to first run the program to
  generate teams. When you do this you will have a text file of output.
  Using this output is how you will email the teams out. From the main
  directory of the repository run the command

  ```
  python3 src/inform.py ../output.txt
  ```

  In the above hypothetical the output.txt is located in the main 
  directory. The inform.py will look for the file relative to its
  location on the file system. This is why in the example above the
  argument points to the parent directory.

  You will next see a prompt requesting your login/password for the
  SMTP server. After supplying them the emails will be sent. The
  format of the email is determined by the email template. Details
  on changing this is located below.

### GUI Usage

  To access the emailer within the GUI version of the program, you start it
  as normal. Once you have generated the teams and adjusted them a you want,
  to email the teams first select all the teams that you want to email.
  Next locate the email button at the lower edge of the window. Hit it and
  then a new window will appear asking for the login/passsword for the
  SMTP server specified in the config settings. After entering this info
  hit send and the emails will be sent. The format of the email(s) is 
  determined by the email template. Details on changing this is located 
  below.

### Email Template

  There is an emailtemplate.txt located in to config directory. This template
  controls what the emails that are sent out looks like. You may change this
  up as you wish but it is limited currently to plain text. Instructions
  on what you can do to alter the template are located within the file.
