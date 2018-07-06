Option Explicit
Private WithEvents inboxItems As Outlook.Items

'Define startup processes
Private Sub Application_Startup()
  Dim outlookApp As Outlook.Application
  Dim objectNS As Outlook.NameSpace
  
  Set outlookApp = Outlook.Application
  Set objectNS = outlookApp.GetNamespace("MAPI")
  Set inboxItems = objectNS.GetDefaultFolder(olFolderInbox).Items
End Sub

'Create an event listener that is triggered when an item is added to the inbox (an email is received)
Private Sub inboxItems_ItemAdd(ByVal Item As Object)
    'MsgBox ("Running automated script")
    On Error GoTo ErrorHandler
    Dim response As String
    Dim userIsAuthorized As Boolean
    Dim requestIsValid As Boolean
    Dim command
    Dim validCommand As Integer
    Dim requesterEmailAddress As String
    Dim validCommands As Variant
    
    'Set initial value
    requestIsValid = False
    'Define the list of valid commands
    validCommands = Array("list saved searches", "run search", "run saved search", "get dashboard pdf", "list dashboard names", _
                        "list dashboard inputs", "get report pdf", "get search pdf", "disable alert", "enable alert", _
                        "list disabled alerts", "reschedule alert", "list app names", "splunkbot")
    'Get the email address of the sender
    requesterEmailAddress = senderEmailAddress(Item)
    'Check whether the sender is authorized to run Splunk searches
    userIsAuthorized = isUserAuthorized(requesterEmailAddress)
    
    'check whether the command is a valid command
    If TypeName(Item) = "MailItem" Then
        'MsgBox (Item.subject)
        For Each command In validCommands
            If InStr(LCase(Item.subject), command) = 1 Then
                requestIsValid = True
                Exit For
            End If
            Next command
    End If
    
    'MsgBox (userIsAuthorized)
    'MsgBox (requestIsValid)
    'If all conditions are met, send the request to the Splunk server and respond to sender with results
    If userIsAuthorized And requestIsValid Then
        response = postRequest(Item.subject)
        AutoReply Item, response
    End If
ExitNewItem:
        Exit Sub
ErrorHandler:
        MsgBox Err.Number & " - " & Err.Description
        Resume ExitNewItem
End Sub

'Get the sender email address
Function senderEmailAddress(Item)
    If Item.sender.AddressEntryUserType = Outlook.OlAddressEntryUserType.olExchangeUserAddressEntry Or Item.sender.AddressEntryUserType = Outlook.OlAddressEntryUserType.olExchangeRemoteUserAddressEntry Then
        Dim exchUser
        exchUser = Item.sender.GetExchangeUser
        If exchUser <> "null" Then
            senderEmailAddress = Item.sender.GetExchangeUser.PrimarySmtpAddress
            'MsgBox (senderEmailAddress)
        End If
    Else
        senderEmailAddress = Item.senderEmailAddress
    End If
End Function

'Send a post request to the Splunk Bot server
Function postRequest(params)
    Dim result As String
    Dim myURL As String, postData As String
    Dim winHttpReq As Object
    Set winHttpReq = CreateObject("WinHttp.WinHttpRequest.5.1")
     
    myURL = "http://localhost:8080"
    postData = params
     
    winHttpReq.Open "POST", myURL, False
    winHttpReq.SetRequestHeader "Content-Type", "application/x-www-form-urlencoded"
    winHttpReq.Send (postData)
     
    postRequest = winHttpReq.responseText

    'MsgBox (result)
End Function

'Reply to the sender of the email
Sub AutoReply(olItem As Outlook.MailItem, response)
    Dim olOutMail As Outlook.MailItem
    If InStrRev(response, ".pdf") = Len(response) - 3 Then
        With olItem
            Set olOutMail = olItem.ReplyAll
            With olOutMail
                .body = "See attached pdf"
                .Attachments.Add response
                .Send        'Change to .Display for testing
            End With
            Set olOutMail = Nothing
        End With
        DeleteFile (response)
    Else
        'formattedResponse = Replace(response, ", ", vbCrLf)
        With olItem
            Set olOutMail = olItem.ReplyAll
            With olOutMail
                .body = response
                .Send        'Change to .Display for testing
            End With
            Set olOutMail = Nothing
        End With
    End If
    
End Sub

'Delete already sent pdf files
Sub DeleteFile(ByVal FileToDelete As String)
    SetAttr FileToDelete, vbNormal
    Kill FileToDelete
End Sub

'Check whether the sender is authorized based off of a contact group
Function isUserAuthorized(sender)
    'MsgBox (sender)
    Dim objOutlook
    Dim objNamespace
    Dim objFolder
    Dim objList
    Dim i As Long
    isUserAuthorized = False

    Const olFolderContacts = 10
    Set objOutlook = CreateObject("Outlook.Application")
    Set objNamespace = objOutlook.GetNamespace("MAPI")
    Set objFolder = objNamespace.GetDefaultFolder(olFolderContacts)
    Set objList = objFolder.Items("Splunk Bot Authorized Users")
    
    For i = 1 To objList.MemberCount
        'MsgBox (objList.GetMember(i).Address)
        If sender = objList.GetMember(i).Address Then
            isUserAuthorized = True
            Exit For
        End If
    Next
End Function









