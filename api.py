# url that give o/p in form of json not html
# o/p of json: list of dictionaries  -> api end point
# api: transfer of data frontend-> backend, backend-> frontend
# json used max due to easier readability

'''
# xml format
<notes>
<note>
<to>ms</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend !< /body>
</note>

<note>
<to>Tove</to>
<from>s</from> I
<heading>Reminder</heading>
<body>Don't forget me this weekend !< /body>
</note>

<note>
<to>a</to>
<from>b</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend !< /body>
</note>
</notes>
'''


'''
# json format
{
"notes": [
{
"to": "Tove"
"from": "Jani",
"heading": "Reminder",
"body": "Don't forget me this weekend!"
},
{
"to": "Tơm",
"from": "Jerry",
"heading": "Reminder",
"body": "Don't forget me this weekend!"
},
{
"to": "Tove"
"from": "Jani",
"heading": "Reminder",
"body": "Don't forget me this weekend!"
}
]
}
'''

# map for js, similar to python dictionary


# types of API

"""
REST API: representational state transfer
Api taking data in json format: rest api
http mthds: get, post, put, delete
conditions cannot be applied, only crud operations can be performed

"""


'''
SOAP API: simple object access protocol
Api taking data in xml format: soap api
erp, banking system, payment gateway
more secure than rest api
'''


'''
GRAPHQL API: graph query language
Api taking data in json format when multiple data/fields has to be accessed at a time
optimal for searching data, only required data is fetched even without backend changes
'''


'''
gRPC API: google remote procedure call
Api taking data in binary format
used for microservices, real time communication
caches data, faster than rest and soap api
'''


'''
websocket API: full duplex communication
used for real time communication, gaming, chat applications
'''


'''
py support single & double quotes not json, json only support double quotes
py empty datatype: None, json empty datatype: null
py boolean datatype: True/False, json boolean datatype: true/false
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"


@app.route('/api/data')
def get_data():
    return [

    {

"fullname": "Aarav Sharma",
"email": "aarav.sharma@example.com",
"username": "aarav123",
"password": "password123",
"confirm_password": "password123"
    }
    ]