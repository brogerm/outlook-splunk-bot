# outlook-splunk-bot
A bot triggered by an Outlook email that runs Splunk searches and replies to the sender with the results

# Outlook Setup
1. Enable macros in Microsoft Office
   1. select "File" in the top left
   2. select "Options"
   3. select "Customize Ribbon"
   4. on the right hand side, check the box that says "Developer"
   5. press "OK". You should now see a "DEVELOPER" tab along the top
   6. select the "DEVELOPER" tab
   7. select "Macro Security" and select "Notifications for all macros", then press "OK"
2. Open the macros editor (in the developer tab click on "Visual Basic")
3. You should see a file structure similar to the following
   > Project1(VbaProject.OTM)/MicrosoftOutlookObject/ThisOutlookSession
4. Open "ThisOutlookSession" and paste in the vba script found in this project "/src/outlookScript.vb"
5. Press the save button
6. In Microsoft Outlook create a contacts group named "Splunk Bot Authorized Users"

# System Setup
1. Set the following environment variables with their respective values
   > SPLUNK_USERNAME

   > SPLUNK_PASSWORD
2. Edit /src/app.py with the base url of your splunk instance. For example:
   > baseurl = 'https://localhost:8089'
   
# Running
1. Make sure Outlook is running then open Windows Command Prompt (as administrator) and navigate to where this project is located
2. Navigate to the src directory and run the following to start the local server that the VBA script will call
```
   python app.py
```
3. Ask someone in your "Splunk Bot Authorized Users" to send you an email with "splunkbot" as the subject line
4. Confirm the reply email was sent
