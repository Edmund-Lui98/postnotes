# postnotes
Using TCP connections to create a post it notes server


Format of messages sent by client and server:

To start server:

py server.py [port number] [board width] [board height] [default color] [color 2]… [color n]

Example:

py server.py 4554 100 200 red white blue orange

To start client:

py client.py


Format of request messages

Functions:
Connect
Disconnect
Post
Get
Pin
Unpin
clear

Connect:
Description: connects to the server specifying the name and port number

Type in console:
CONNECT [Server Name][Port number]

Example:
CONNECT localhost 4554

Disconnect:
Description: when connected to the server, this function will disconnect the client and server

Type in console:
DISCONNECT

Post:
Description: will post the following note to the server board
Type in console:
POST [x coordinate] [y coordinate] [width] [height] [color] [message]
Example:
POST 5 10 2 2 white hey there
POST 7 20 5 8 blue how are you doing?

Get:
Description: Asks the server for all notes given conditions by the user. 

Use cases:
color=[color] ← gets notes with this color
refersTo=[string] ← gets notes that includes the string
contains= [int] [int] ← gets notes that fall within the given coordinates
PINS= [int] [int] ← gets all notes that are pinned 

Type in console: 
GET [arg(1)] [arg(2)]... [arg(n)]

Example:
GET
GET color=white
GET refersTo=Brian color=white

Pin:
Description: Will pin the following notes that fall within the coordinate

Type in console:
PIN [x coordinate],[y coordinate]

Example:
PIN 4,5

Unpin:
Description: Will unpin the following notes that fall within the coordinate

Type in console:
UNPIN [x coordinate],[y coordinate]

Example:
UNPIN 10,7

Clear:
Description: will clear all notes that are not pinned

Type in console:
CLEAR


Format of response messages
After getting the note, the console will display:

msg: [string of message]
pinned status: [False or an int >0 that represents the # of pins]
xposition: [x coordinate of the pin]
yposition: [y coordinate of the pin]
width: [width of the note]
height: [height of the note]
color: [color of the note]

Example:

msg: hey there 
pinned status: False
xposition: 5
yposition: 10
width: 2
height: 2
color: white

msg: How are you doing? 
pinned status: 3
xposition: 23
yposition: 7
width: 6
height: 9
color: blue

 
Synchronization policies

This project uses a total of 2 python files: client.py, server.py

Client.py
	This python file prompts user to connect to a server by using the connect command, giving a server name and server port number. This then connects to the server side and sends the command of the user to the server side as an encoded string. The server will then return the output and decode it for the user. 

Server.py
	This python file initializes the server and gets ready to take the command given by the client and will strip the command and executes the proper command. This file includes two classes which are a “Note” class to keep track of the message, status, position, width, height, and color and a “Notes” class that will store all the Note objects and call the functions mentioned above. This will then execute the function and return the desired output. 

Error handling on server and client

If user tries to retrieve notes when there are none or when the condition doesn’t satisfy any of the notes then the server will return: “no notes”

If user tries to type in any function such as POST or GET without connecting to a server first, the client will prompt the user to “please connect to server name and port number”
