#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl GET http://www.example.com HTTP/1.0 -i -H "Range: bytes=0-199"

