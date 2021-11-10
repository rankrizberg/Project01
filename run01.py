#!/usr/bin/env python3
from csv import reader

def read_csv_file(csv):
    with open(csv, 'r') as read_obj:
        data_dic={}
        csv_reader = reader(read_obj)
        for row in csv_reader:
            new_key=row[2]
            if new_key  not in data_dic.keys():
                data_dic[new_key]=[]
            data_dic[new_key].append(row)
            
        #for x in data_dic:
            #print("key :{} value: {}".format(x,data_dic[x]))
        for x in data_dic:
            print("\nkey :{} ".format(x)) 
            for row in data_dic[x]:
                print(row)    
            
       # print(data_dic['Appserver'])

  
def GenerateXML(Rank):
    root=xml.Element("DeploymentInfo")
    cl=xml.Element("Files")
    root.append(cl)
    type1=xml.SubElement(cl,"SourceFile_name")
    type1.text="Readme.txt"

    sourceServer1=xml.SubElement(cl,"sourceServer")
    sourceServer1.text="ftp.myftp1.com"
     
    sourceFolder1=xml.SubElement(cl,"sourcefOLDER")
    sourceFolder1.text="C:\Publish\Framework"

    tree=xml.ElementTree(root)
    with open (Rank, "wb") as files:
        tree.write (files)

if __name__=="__main__":
    GenerateXML("Test.xml")   
read_csv_file("ftpsrv1.csv")
