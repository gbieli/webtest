import sqlite3
import http.server
import socketserver

conn = sqlite3.connect("test.db")

c = conn.cursor()
# c.execute("CREATE TABLE person (firstname text, lastname text)")
# c.execute("INSERT INTO person VALUES ('gery', 'bieli')")
#
# conn.commit()

for row in c.execute('SELECT * FROM person'):
    print(row)

conn.close()

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()