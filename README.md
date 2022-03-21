# apache-airflow-task-status-email-alerts
This template will help you automate the email according to Task status i.e Success or Failure. If the task fails, the user will receive a task failure email alert and if task performs as required then it will send a success email alert.

# Follow below steps before coding:

1. Generate Google App Password by vising below link:
https://accounts.google.com/signin/v2/challenge/pwd?continue=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&service=accountsettings&osid=1&rart=ANgoxcfhiTXz6dNMPbv57cd7L5xFJkwSbK7rWCrEYUmSKymgcC11gZfJTexo8nqogK16wcIFw19FA12DYindJX1Ipe0sg3FrGw&TL=AM3QAYY1Q3-4n8u0l_dqj3kOSUooqTifZrTKbPee1lsQfwehiux9ebNzfl-xU19b&flowName=GlifWebSignIn&cid=1&flowEntry=ServiceLogin

NOTE: This generates 16 character unique password authorized by Google to mock the original password or two-factor authentication. Copy the password and save it somewhere. 

2. Edit the airflow.cfg file: 

[email]
email_backend = airflow.utils.email.send_email_smtp


[smtp]
smtp_host = smtp.googlemail.com
smtp_starttls = True
smtp_ssl = False
smtp_user = YOUR_EMAIL_ADDRESS
smtp_password = 16_DIGIT_APP_PASSWORD
smtp_port = 587
smtp_mail_from = YOUR_EMAIL_ADDRESS
