#!/bin/bash
#A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
#!/bin/bash
curl -sI http://i.imgur.com/z4d4kWk.jpg HTTP/1.0 "Range: bytes=0-1023"


