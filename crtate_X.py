import xml.etree.ElementTree as xml

def GenerateXML(Rank):
    root=xml.Element("DeploymentInfo")
    cl=xml.Element("Files")
    root.append(cl)
    type1=xml.SubElement(cl,"SourceFile name")
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
