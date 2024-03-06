#!/bin/bash
#A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI GET http://i.imgur.com/z4d4kWk.jpg HTTP/1.0 "Range: bytes=0-1023"
