# How to use Keylogger.pyw

1. Either fork or download the Keylogger.pyw file
2. Install Python and download all *dependencies* (*dependencies* are the *imports* at the top of the code) 
3. In ```def send_mail``` Change code to reflect the email you want to send keystrokes from its password and the receiving emails. 

   a. Change ```address```, ```password```, ```receivers```.
   
   b. Google smtp for *Gmail, Yahoo, etc* to select the *correct email server* and port for **TLS**. 
   
   c. ^ use info in b to change `s = smtplib.SMTP(` line.
4. For Linux users add the shebang line to the top of the code before running. For Windows change nothing except the emails.
5. Run the code.
6. Press ```esc``` to stop the code.
7. If you want to change ```esc``` to something else go to ```def on_release```.

# How to use Webscrapper.py

1. Either fork or download
2. Install Python and all dependencies.
3. Make sure shebang line is added at the top of the script if needed.*(On Windows OS Shebang line is not needed)*
4. Copy the full link of the website you want to scrap.
5. Run the code.
