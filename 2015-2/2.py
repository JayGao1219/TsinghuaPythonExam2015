import sys;
from bs4 import BeautifulSoup;
soup=BeautifulSoup(open('2.html'),"lxml");
if len(sys.argv)==1:
    print(soup);
else:
    a=soup.find_all('td');
    b=0;
    for i in range(0,len(a)):
        if(sys.argv[1]==a[i].get_text()):
            b=i;
            break;
    st="";

    hh=a[b].parent;
    h=hh.find_all('td');
    for i in h:
        if(i.get_text()!=sys.argv[1]):
            st+=i.get_text();
            st+=" ";

    print(st);

