#!/bin/bash
#A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a request to the URL and store the response in a variable
response=$(curl -sI "$url")

# Extract the content length from the response headers
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

# Check if the content length is available in the response headers
if [ -z "$content_length" ]; then
    echo "Content-Length not found in the response headers."
    exit 1
fi

# Display the content length in bytes
echo "Size of the response body: ${content_length} bytes"

