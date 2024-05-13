import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

# Change directory to where your index.html is located
# Example: If index.html is in the same directory as this script, you can remove this line
# and the script will serve files from the current directory by default.
# If your index.html is in a different directory, replace 'path_to_directory' with the actual directory path.
# Example: If index.html is in a folder named 'public', replace 'path_to_directory' with 'public'
# Make sure to specify the correct path relative to the location of this Python script.
# If index.html is in a subdirectory like 'public', use:
# os.chdir(os.path.join(os.path.dirname(__file__), 'public'))
# If index.html is in the same directory as this script, use:
# os.chdir(os.path.dirname(__file__))
# You may need to import the os module for this.

# Navigate to the directory where index.html is located
# os.chdir('path_to_directory')

# Create an HTTP server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    # Start the server
    httpd.serve_forever()
