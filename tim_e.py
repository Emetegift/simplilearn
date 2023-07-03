# ## To get time that has passed and present

# import time

# epc =time.time()  ## This Set the starting time
# localtime = time.localtime(epc) ## This will give the number of seconds
# print(localtime)
# ## To get only the year
# print(localtime.tm_year)
#  ## To get date details in a more formal way,
# print(time.ctime(epc))

# # Calculate the elapsed time in seconds
# elapsed_time = time.time() - epc
# # Print the elapsed time
# print("Seconds elapsed:", elapsed_time)


## To send an email using python smtplib function
# import smtplib

# smtobj = smtplib.SMTP('smtp.gmail.com', 587)
# smtobj.ehlo()
# smtobj.starttls()
# smtobj.login('emeteokeoghene@gmail.com', 'Giftedgift94')
# smtobj.sendmail('emeteokeoghene@gmail.com', 'anisundaypaul76@gmail.com', 'Subject: Testing email\n\nThis email was sent from Python')
# smtobj.quit()

# ## Another way to write an email using python

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Email configuration
# sender_email = 'emetegift00@gmail.com'
# receiver_email = 'anisundaypaul76@gmail.com'
# subject = 'Testing email'
# message = 'This email was sent from Python by your Love!'

# # SMTP server details
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# smtp_username = 'emetegift00@gmail.com'
# smtp_password = 'Emeteemerald'

# # Create a message object
# msg = MIMEMultipart()
# msg['From'] = sender_email
# msg['To'] = receiver_email
# msg['Subject'] = subject
# msg.attach(MIMEText(message, 'plain'))

# try:
#     # Create a secure SSL/TLS connection with the SMTP server
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()
    
#     # Log in to the SMTP server
#     server.login(smtp_username, smtp_password)
    
#     # Send the email
#     server.sendmail(sender_email, receiver_email, msg.as_string())
    
#     print('Email sent successfully!')
# except Exception as e:
#     print('An error occurred while sending the email:', str(e))
# finally:
#     if 'server' in locals():
#         server.quit()


"""
*args and **kwargs
The *args syntax is used to pass a variable number of positional arguments to a function. 
The term "args" is just a convention, and you can choose any valid variable name preceded by an asterisk. 
When the function is called, the positional arguments are collected into a tuple.
Inside the function, you can iterate over the tuple or access individual elements by indexe.

 
"""
# def my_function(*args):
#     for arg in args:
#         print(arg)

# my_function('apple', 'banana', 'cherry')

"""
The **kwargs syntax is used to pass a variable number of keyword arguments to a function. 
Similarly to *args, "kwargs" is a convention, and you can choose any valid variable name preceded by two asterisks. 
When the function is called, the keyword arguments are collected into a dictionary. 
Inside the function, you can access the values of the keyword arguments using their corresponding keys.
In the example, the keyword arguments 'name', 'age', and 'city' are passed to the function my_function(),
and the function prints each key-value pair.
Using *args and **kwargs allows you to create flexible functions that can handle a varying number of arguments.
"""
# def my_function(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# my_function(name='Alice', age=25, city='New York')




"""
Creation of nested functions:
"""
def func1 ():
    x =10
    def func2 (x):
        return x + 1
    return func2(x)
result = func1()
print(result)
