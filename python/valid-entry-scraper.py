from xml.dom.minidom import parse
import csv

def getData():

    data = []
    # load and parse
    doc = parse("hdpstudent2.xsd")
    col = doc.getElementsByTagName("xs:simpleType")

    # get data
    for c in col:
        name = c.getAttribute("name")
        enumeration = c.getElementsByTagName("xs:enumeration")
        for e in enumeration:
            value = e.getAttribute("value")
            label = e.getElementsByTagName("Label")[0].firstChild.data
            data.append([name, value, label])

    return data

def cleanData(pData):

    line = []
    # word endings
    endings = ('Type','TypeExtra')

    for p in pData:

        # remove actions
        if p[0] != 'action':

            # remove endings
            for ending in endings:
                if p[0].endswith(ending):
                    name = p[0][:-len(ending)]

                    # split entity and field
                    splitName = name.split("_")

            # remove newlines when label is blank
            cLabel = p[2].strip('\n')
            # remove commas
            cleanLabel = cLabel.replace(',','')

            # create line
            line.append([','.join(splitName) + ',' + p[1] + ',' + cleanLabel])

    return line

def writeData(pLine):

    # write to file
    with open("hdpstudent2.csv","w",newline='') as f:

        for l in pLine:
            f.write(', '.join(l) + '\n')

    f.close()

def main():
    input = getData()
    sanatisedInput = cleanData(input)
    writeData(sanatisedInput)

if __name__ == "__main__":
    main()
