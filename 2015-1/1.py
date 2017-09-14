import sys
import xmltodict,json
a=sys.argv[1];
b=sys.argv[2];
file1=open(a);
file2=open(b,'w');
x=''
while 1:
    line=file1.readline();
    if not line:
        break;
    x+=line;

if(a=='1.xml'):
    o=xmltodict.parse(x);
    file2.write(json.dumps(o,indent=1));
else:
    o=xmltodict.unparse(eval(x));
    file2.write(o);
