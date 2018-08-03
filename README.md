# outlook-splunk-bot
A bot triggered by an Outlook email that runs Splunk searches and replies to the sender with the results

# Directions
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
    Project1(VbaProject.OTM)/MicrosoftOutlookObject/ThisOutlookSession
4. Open "ThisOutlookSession" and paste in the vba script found in this project "/src/outlookScript.vb"
5. In Microsoft Outlook create a contacts group named "Splunk Bot Authorized Users"  
6. Open Windows Command Prompt (as administrator) and navigate to where this project is located
7. Navigate to the src directory and run the following to start the local server that the VBA script will call
```
python app.py
```
8. Ask someone in your "Splunk Bot Authorized Users" to send you an email with the following subject line:
> splunkbot
