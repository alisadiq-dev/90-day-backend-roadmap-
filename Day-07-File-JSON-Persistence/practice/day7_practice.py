"""
what is jason:
- JavaScript Object Notation
uses:
used to store and exchange data between a server and a web application 
- JASON = is a data exchange format 
===== here the jason format ====== 
{"Students":[{"name":"John", "age":30, "city":"New York"},
{"name": "Ali", "age":22, "city": "London"}]}

=== here the XML format ===
<Students>
    <Student>
        <name>John</name>
        <age>30</age>
        <city>New York</city>
    </Student>
    <Student>
        <name>Ali</name>
        <age>22</age>
        <city>London</city>
    </Student>
</Students>

======== jason  =====
- java script object notation
- txt base data format 
- light wait 
- easy to use 

=== data type allowed in jason ===
. String 
. Number 
. Object 
. Array 
. Boolean 
. Null

========= file handling =========
# file modes
- r: read
- w: write
- a: append
- r+: read and write
- w+: write and read
- a+: append and read
- x : create a new file and open it for reading it 

====== the file if it exists ======
- b: binary mode
- t: text mode
- +: update mode ( read and write)

=====. file methode =======
- read() : read the file
- write() : write the file
- append() : append the file
- close() : close the file
- flush() : flush the file
- tell() : tell the file position
- seek() : seek the file position
- rename() : rename the file
- remove() : remove the file
- copy() : copy the file
- move() : move th file
- readlines() : read th file line by line
- readline() : read th file line by line
- readable() : check if the file is readable
- writable() : check if the file is writable
- seekable() : check if the file is seekable
- isatty() : check if the file is a terminal
"""
fopen = open("example.txt", "r")
print(fopen.readline())
for data in fopen.readlines():
    print(data, end=" ")

""" agr hum nay file ko read mode main open kiya hai to hum usko close karna padega 
- or agr hum nay file ko read mode ma open keya ha or hum write karna chaty han tu wo file ko empty akr day ga ye bhut sensitive case ha 
- agr hum "a" apeend use kary gy open file ma tu phir be error day ga lekin file ko empty nahi karen ga 
"""


# ====== 25-50m: Learn JSON serialization/deserialization ====
"""
- serilization = convert the object into a json string = encoding 
- deserilization = convert the json string into a object = decoding

@dataclass 
class person:
    name : str
    age : int
Ali = person("Ali", 22)
print(Ali)

its look like in jason string 
{
    "name": "Ali",
    "age": 22
}