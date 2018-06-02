from nodemcu import node
from simplehttpserver import server
import psycopg2
import os

print('starting PostgreSQL connection')
try:
    con = psycopg2.connect(host='localhost', database='nodemcu', user='postgres', password='admin')
    cur = con.cursor()
except psycopg2.Error as e:
    print("Cannot connect to database", e)

print('starting nodemcu')
try:
    node = node.Node(con)
except:
    print("Error on create node instance")

print('starting server...')
try:
    #web_dir = os.path.join(os.path.dirname(__file__), 'interfaceWEB')
    #os.chdir(web_dir)
    server_address = ('', 8081)
    #httpd = HTTPServer(server_address, server.Server)
    serv= server.Server(server_address,'interfaceWEB', node)
    #httpd.serve_forever()
except:
    print("Error on create http server")

serv.run()
print('running server...')