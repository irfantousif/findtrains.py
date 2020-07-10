src=['hyderabad','delhi','khammam','america' ]
s=input("enter src")
dest=['hyderabad','delhi','khammam','america']
d=input("enter destination")
train1={"train no":(123456),"train name":("link"),"train time":'1.00-1.30',"src":("hyderabad"),"dest":("delhi")}
train2={"train no":(234567),"train name":("konark"),"train time":"1.30-1.45","src":("delhi"),"dest":("hyderabad")}
train3={"train no":(134566),"train name":("passenger"),"train time":"1.45-1.55","src":("hyderabad"),"dest":("khammam")}
train4={"train no":(657568),"train name":("amaravati"),"train name":"2.00-2.30","src":("khammam"),"dest":("hyderabad")}
train5={"train no":(656677),"train name":("andra "),"train name":"2.30-2,45","src":("delhi"),"dest":("khammam")}
train6={"train no":(567899),"train name":("bharath"),"train name":"2.45-3.00","src":("khammam"),"dest":("delhi")}
val=train1.get("src")
val1=train1.get("dest")
val2=train2.get("src")
val3=train2.get("dest")
val4=train3.get("src")
val5=train3.get("dest")
val6=train4.get("src")
val7=train4.get("dest")
val8=train5.get("src")
val9=train5.get("dest")
val10=train6.get("src")
val11=train6.get("dest")
if((s==val) & (d==val1)):
        print(train1)
if((s==val2) & (d==val3)):
        print(train2)
if((s==val4) & (d==val5)):
        print(train3)
if((s==val6) & (d==val7)):
        print(train4)
if((s==val8) & (d==val9)):
        print(train5)
if ((s==val10) & (d==val11)):
        print(train6)
else:
        print("SORRY! THE TRAINS ARE NOT AVALIABLE")






