# Digant Kumar
# Program that prints out a summary of the emails sent by either Lay or Skilling

import os        # To traverse the directory
import email     # To parse over the emails
def email_from(suspects):
    file_path = ["C:\\Users\\Digant\\Downloads\\Enron\\lay-k\\sent", "C:\\Users\\Digant\\Downloads\\Enron\\skilling-j\\sent"]
    for path in file_path:               # Traversing through the file path 1 by 1
        for root,dirs,files in os.walk(path):
            for file in files:
                new = path + "\\" + file           # Concatinating the files
                file_open = open(new,"r")
                content = file_open.read()
                text = email.message_from_string(content)       # Reading the entire email
                sentby = text['from']
                subject = text['Subject']
                date = text['Date']
                to = text['to']
                for key,val in suspects.items():                 # Checking if the email exists in the suspects dictionary, if it does, prints the summary
                    if sentby in val:
                        print("[%s] %s -> %s " % (date[5:15], sentby, to.split(",")[0]))
                        print("Subject : %s" %(subject))

red_flags = {"lay-k": ["kenneth.lay@enron.com", "klay@enron.com"],"skilling-j": ["skilling@enron.com", "jeff.skilling@enron.com"]}
print(email_from(red_flags))