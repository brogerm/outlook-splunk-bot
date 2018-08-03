# outlook-splunk-bot
A bot triggered by an Outlook email that runs Splunk searches and replies to the sender with the results

# Directions
1. Enable macros in Microsoft Office
  a. select "File" in the top left
  b. select "Options"
  c. select "Customize Ribbon"
  d. on the right hand side, check the box that says "Developer"
  e. press "OK". You should now see a "DEVELOPER" tab along the top
  f. select the "DEVELOPER" tab
  g. select "Macro Security" and select "Notifications for all macros", then press "OK"
2. Open the macros editor (in the developer tab click on "Visual Basic")
3. You should see a file structure similar to the following
    Project1(VbaProject.OTM)/MicrosoftOutlookObject/ThisOutlookSession
4. Open "ThisOutlookSession" and paste in the vba script found in this project "/src/outlookScript.vb"
5. Open Windows Command Prompt (as administrator) and navigate to where this project is located
6. Run the following to start the local server that the VBA script will call
```
python app.py
```
