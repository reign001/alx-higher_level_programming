#!/bin/bash
#A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
#!/bin/bash
curl -sI http://i.imgur.com/z4d4kWk.jpg -i -H "Range: bytes=0-1023"


