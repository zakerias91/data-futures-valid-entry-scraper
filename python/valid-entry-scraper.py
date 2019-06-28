import xml.dom.minidom
import csv

def main():
    
    # load and parse
    doc = xml.dom.minidom.parse("hdpstudent2.xsd")
    col = doc.getElementsByTagName("xs:simpleType")

    # word endings
    endings = ('Type','TypeExtra')

    with open("hdpstudent2.csv","w",newline='') as csv_f:

        for c in col:
            entry = c.getElementsByTagName("xs:enumeration")
                
            for i, e in enumerate(entry):
                name = c.getAttribute("name")
                label = c.getElementsByTagName("Label")
                        
                # remove endings
                for ending in endings:
                    if name.endswith(ending):
                        n = name[:-len(ending)]

                        # split entity and fields
                        ef = n.split("_")

                # remove actions
                if c.getAttribute("name") != 'action':
                    
                    # remove newlines when label is blank
                    clean_label = label[i].firstChild.nodeValue.strip('\n')
                    
                    line = ','.join(ef) + ',' + e.getAttribute("value") + ',' + clean_label
                    csv_f.write(line + '\n')
    
    csv_f.close()

if __name__ == "__main__":
    main()
