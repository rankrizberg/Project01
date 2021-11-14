#!/usr/bin/env python3
import os,sys
import argparse
from csv import reader

data_dic={}

def arg_parser():
    parser = argparse.ArgumentParser(description='Process input arguments.')
    parser.add_argument('-c', action='store', dest='csv_file',help='setup name from json file', required=True)
    parser.add_argument('-o', action='store', dest='out_put',help='setup name from json file', required=True)

    args = vars(parser.parse_args())
    return args


def read_csv_file(csv):
    with open(csv, 'r') as read_obj:
        
        csv_reader = reader(read_obj)
        
        for row in csv_reader:
        
            new_kwy='_'.join(row).lower()
        
            if new_kwy  not in data_dic.keys():
                data_dic[new_kwy]=row


    
def GenerateXML(Rank,data_str):
    import xml.etree.ElementTree as ET
    data='''<?xml version="1.0" encoding="UTF-8"?>
    <DeploymentInfo>
        <Metadata Version="1.5"></Metadata>
        <Files>
            <SourceFile name="Readme.txt" sourceServer="ftp.myftp1.com" sourceFolder="C:\Publish\Framework">
                ABCD
            </SourceFile>

        </Files>
    </DeploymentInfo>
    '''
    data = data.replace('ABCD',data_str)
    tree = ET.ElementTree(ET.fromstring(data))
    tree.write(Rank, encoding = "UTF-8", xml_declaration = True)  



def buildtarget():
    tempdic={}
    index=0
    for x in data_dic:
        if data_dic[x][2]=='WebServer':
            tempdic[index]=["Webserver","c:\Webserver\FolderA"]
            index+=1
            tempdic[index]=["Webserver","c:\Webserver\FolderB"]
        if data_dic[x][2]=='AppServer':
            tempdic[index]=["Appserver","c:\Appserver\FolderA"]
            index+=1
        if data_dic[x][2]=='DBserver':
            tempdic[index]=["DBserver","c:\DBserver\C"]
            index+=1
    print(data_dic)
    return tempdic



def createxml(tempdic,out_put):
  
    import xml.etree.ElementTree as ET
    data='''<?xml version="1.0" encoding="UTF-8"?>
    <DeploymentInfo>
        <Metadata Version="1.5"></Metadata>
        <Files>
            <SourceFile name="Readme.txt" sourceServer="ftp.myftp1.com" sourceFolder="C:\Publish\Framework">
                DATA_PARSER
            </SourceFile>

        </Files>
    </DeploymentInfo>
    '''
    modifydata=""
    for x in tempdic:
       modifydata+='''                    <TargetFile ServerType="{}" TargetFolder="{}"/>\n'''.format(tempdic[x][0],tempdic[x][1])
       
    GenerateXML(out_put,modifydata)

    
    

# -----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main_args = []
    main_args = arg_parser()
    read_csv_file(main_args['csv_file'])
    createxml(buildtarget(),main_args['out_put'])
    sys.exit(0)
