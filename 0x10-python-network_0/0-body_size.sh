#!/bin/bash
#A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
#!/bin/bash
curl -sI http://www.nowhere.com:8000 | grep -i "Range: bytes=0-102" | awk '{print $2}' | tr -d '\r'

