#!/usr/bin/python
# -*- coding: utf-8 -*-

#Essential library was imported
import csv
import xml.etree.ElementTree as ET
import sys
import json
from lxml import etree 



def Main(input_file,output_file,c):  #Main function call another function which have choice
    if(c == "1"):
        CsvToXml(input_file,output_file)
    if(c == "2"):
        XmlToCsv(input_file,output_file)
    if (c == "3"):
        XmlToJson(input_file, output_file)
    if (c == "4"):
        JsonToXml(input_file, output_file)
    if (c == "5"):
        CsvToJson(input_file, output_file)
    if (c == "6"):
        JsonToCsv(input_file, output_file)
    if (c == "7"):
        XmlValidatesXsd(input_file, output_file)



def CsvToXml (input_file,output_file):
    read=open(input_file, 'r')#csv file was readed.

    csv_read = csv.reader(read, delimiter='|')


    line_count=0
    data = ET.Element("departments")#elements tree used for create xml
    data.tail="\n"
    data.text = "\n\t"# essential gap was obtained
    flag = True
    tempUNI =""


    for row in csv_read:#csv read row by row



        if line_count == 0:
            words = row[0].split(";")
            line_count += 1
        else:
            row[0] = row[0].replace(";", " ;")#splitted with  gap and ';' because check GEÇEN_YIL_MİN_PUAN properly.
            row = row[0].split(";")


            if (tempUNI != row[1].strip()):

                tempUNI = row[1].strip()
                flag = True
            if(flag):

                items = ET.SubElement(data,"university")#university data and their elements set created.
                items.text = "\n\t\t"# essential gap was obtained
                items.set("name",row[1].strip())
                items.set("uType", row[0].strip())
                data[-1].text ="\n\t\t"# essential gap was obtained


                flag =False

            item1 = ET.SubElement(items, 'item')#item data and their elements set created.
            item1.text = "\n\t\t\t"# essential gap was obtained
            item1.set('id', row[3].strip())
            item1.set('faculty', row[2].strip())
            items[-1].text = "\n\t\t\t"# essential gap was obtained



            item2 = ET.SubElement(item1, 'name')#name data and their elements set created.
            item2.text = "\n\t\t\t"# essential gap was obtained
            item2.set('lang', row[5].strip())

            if(row[6].strip()==""):
                row[6]="No"
            item2.set('second', row[6].strip())
            item2.text = row[4].strip()

            item1[-1].tail = "\n\t\t\t"# essential gap was obtained


            item3 = ET.SubElement(item1, 'period')#period data and their elements set created.
            item3.tail = "\n\t\t\t"# essential gap was obtained
            item3.text = row[8].strip()
            item1[-1].tail = "\n\t\t\t"# essential gap was obtained



            item4 = ET.SubElement(item1, 'quota')#quota data and their elements set created.
            item4.tail = "\n\t\t\t"# essential gap was obtained
            item4.set("spec", row[11].strip())
            item4.text = row[10].strip()
            item1[-1].tail = "\n\t\t\t"# essential gap was obtained



            item5 = ET.SubElement(item1, 'field')#field data and their elements set created.
            item5.tail = "\n\t\t\t"# essential gap was obtained
            item5.text = row[9].strip()
            item1[-1].tail = "\n\t\t\t"# essential gap was obtained



            item6 = ET.SubElement(item1, 'last_min_score ')#last_min_score data and their elements set created.
            item6.tail = "\n\t\t\t"# essential gap was obtained
            item6.set( "order ",row[12].strip())
            item6.text = row[13].strip()
            item1[-1].tail = "\n\t\t\t"# essential gap was obtained




            item7 = ET.SubElement(item1,"grant")#grant data and their elements set created.
            item7.tail = "\n\t\t"# essential gap was obtained
            item7.text = row[7].strip()
            item1[-1].tail = "\n\t\t"# essential gap was obtained
            item7.tail = "\n\t\t"

            """
            (!!!!!!!!!!important!!!!!!!!!!!)
            
            Data has written properly by utf-8  , some ide or os can be  show bad .But it is true . when convert xml to csv it is work properly  . I used PYTHON3 and linüx . 
            decoding and encoding work properly.if you can not show properly it ,you can check it at Chorome . thank you .
            
            """
            mydata = ET.tostring(data)
            myfile=open(output_file, "w")
            myfile.write(mydata.decode("utf-8"))

            line_count += 1



def XmlToCsv(input_file,output_file):
    tree = ET.parse(input_file)#tree is created.
    root = tree.getroot()


    with open(output_file, 'w', newline='') as r:
        writer = csv.writer(r,delimiter=(";"))  #csv writer
        writer.writerow(['ÜNİVERSİTE_TÜRÜ', 'ÜNİVERSİTE', 'FAKÜLTE','PROGRAM_KODU','PROGRAM','DİL','ÖĞRENİM_TÜRÜ','BURS','ÖĞRENİM_SÜRESİ','PUAN_TÜRÜ','KONTENJAN','OKUL_BİRİNCİSİ_KONTENJANI','GEÇEN_YIL_MİN_SIRALAMA','GEÇEN_YIL_MİN_PUAN'])  # Writing Headers

        for departments in tree.iter('departments'):#tree iterated

           j=-1
           for university in departments.iter('university'):#tree iterated to university
                j+=1
                i=-1
                universityname = university.attrib.get('name')
                uType = university.attrib.get('uType')

                for item in university.iter('item'):#tree iterated to item
                    i+=1

                    id= item.attrib.get('id')
                    faculty= item.attrib.get('faculty')
                    for name in item.iter('name'):#tree iterated to name
                        lang = name.attrib.get('lang')
                        if(name.attrib.get('second')=="No"):
                            a=""
                        else:
                            a=name.attrib.get('second')
                        second= a
                        prog = root[j][i][0].text#necessary root choiced for prog

                    for period in item.iter('period'):
                        period= root[j][i][1].text#necessary root choiced for period

                    for quota in item.iter('quota'):
                        quota_spec= quota.attrib.get('spec')
                        quota = root[j][i][2].text#necessary root choiced for quota

                    for field in item.iter('field'):
                        field= root[j][i][3].text#necessary root choiced for field

                    for last_min_score in item.iter('last_min_score'):
                        last_min_scoreorder= last_min_score.attrib.get('order')
                        order = root[j][i][4].text#necessary root choiced for order

                    for grant in  item.iter('grant'):
                        grant = root[j][i][5].text#necessary root choiced for grant



                    writer.writerow([uType,universityname,faculty,id,prog,lang,second,grant,period,field,quota,quota_spec,last_min_scoreorder,order])#necessary text was written to csv file



def XmlToJson(input_file,output_file):

    tree = ET.parse(input_file)#tree is created.
    root = tree.getroot()
    dataKeep=[]#array created for keep data.
    dataKeep.append(
        ['ÜNİVERSİTE_TÜRÜ', 'ÜNİVERSİTE', 'FAKÜLTE', 'PROGRAM_KODU', 'PROGRAM', 'DİL', 'ÖĞRENİM_TÜRÜ', 'BURS',
         'ÖĞRENİM_SÜRESİ', 'PUAN_TÜRÜ', 'KONTENJAN', 'OKUL_BİRİNCİSİ_KONTENJANI', 'GEÇEN_YIL_MİN_SIRALAMA',
         'GEÇEN_YIL_MİN_PUAN'])  # data was kept in dataKeep array

    for departments in tree.iter('departments'):

        j = -1
        for university in departments.iter('university'):#tree iterated to university
            j += 1
            i = -1
            universityname = university.attrib.get('name')
            uType = university.attrib.get('uType')

            for item in university.iter('item'):#tree iterated to item
                i += 1

                id = item.attrib.get('id')
                faculty = item.attrib.get('faculty')
                for name in item.iter('name'):#tree iterated to name
                    lang = name.attrib.get('lang')
                    if (name.attrib.get('second') == "No"):
                        a = ""
                    else:
                        a = name.attrib.get('second')
                    second = a
                    prog = root[j][i][0].text#necessary root choiced for second

                for period in item.iter('period'):
                    period = root[j][i][1].text#necessary root choiced for prog

                for quota in item.iter('quota'):
                    quota_spec = quota.attrib.get('spec')
                    quota = root[j][i][2].text#necessary root choiced for quota

                for field in item.iter('field'):
                    field = root[j][i][3].text#necessary root choiced for field

                for last_min_score in item.iter('last_min_score'):
                    last_min_scoreorder = last_min_score.attrib.get('order')
                    order = root[j][i][4].text#necessary root choiced for order

                for grant in item.iter('grant'):
                    grant = root[j][i][5].text#necessary root choiced for grant




                dataKeep.append([uType, universityname, faculty, id, prog, lang, second, grant, period, field, quota, quota_spec,
                     last_min_scoreorder, order])#data saved to array in everylop



    line_count = 0
    temp = ""
    temp2 = ""
    for row in dataKeep:#data readed row by row .

        if line_count == 0:
            words = ['university name', "uType", "items", "faculty", "department", 'id', 'name',
                     'lang', 'second', 'period', 'spec', 'quota',
                     'field', 'last_min_score', 'last_min_order', 'grant']#header was created.

            line_count += 1
        else:

            with open(output_file, 'a') as a:

                if ((row[1] != temp and row[2] == temp2 and temp != "" and temp2 != "") or (
                        row[1] != temp and row[2] != temp2 and temp != "" and temp2 != "")):
                    a.write("\n\t\t\t\t\t}")# essential gap was obtained
                    a.write("\n\t\t\t\t]")# essential gap was obtained
                if (row[1] == temp and row[2] == temp2):
                    a.write("\n\t\t\t\t\t},")
                if ((row[2] != temp2 and temp != "" and temp2 != "") or (
                        row[1] != temp and temp != "" and temp2 != "")):
                    a.write("\n\t\t\t}")# essential gap was obtained
                    a.write("\n\t\t]")

                if (temp != "" and row[1] != temp):
                    a.write("\n\t},\n\t\t")# essential gap was obtained

                if (row[1] != temp):
                    if (temp == ""):
                        a.write("[\n\t")
                    a.write("{\n\t\t")
                    json.dump((words[0]), a, indent=2)
                    a.write(": " + '"' + row[1].strip() + '",')#necessary data implemented to json file properly
                    a.write("\n\t\t")
                    json.dump((words[1]), a, indent=2)
                    a.write(": " + '"' + row[0].strip() + '",')#necessary data implemented to json file properly
                    a.write("\n\t\t")
                    json.dump((words[2]), a, indent=2)
                    a.write(": ")
                    a.write("\n\t\t[")# essential gap was obtained
                    temp = row[1]
                    temp2 = "-"

                if (row[2] != temp2):
                    a.write("\n\t\t\t{\n\t\t\t")# essential gap was obtained
                    a.write("\n\t\t\t\t")
                    json.dump((words[3]), a, indent=2)
                    a.write(": " + '"' + row[2].strip() + '",')#necessary data implemented to json file properly
                    a.write("\n\t\t\t\t")
                    json.dump((words[4]), a, indent=2)
                    a.write(": ")
                    a.write("\n\t\t\t\t[")# essential gap was obtained
                    a.write("\n\t\t\t\t")
                    temp2 = row[2]

                a.write("\n\t\t\t\t\t{")
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[5]), a, indent=2)
                a.write(": " + '"' + row[3].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[6]), a, indent=2)
                a.write(": " + '"' + row[4].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[7]), a, indent=2)
                a.write(": " + '"' + row[5].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[8]), a, indent=2)
                if (row[6].strip() == ""):
                    row[6] = "No"
                a.write(": " + '"' + row[6].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[9]), a, indent=2)
                a.write(": " + row[8].strip())#necessary data implemented to json file properly
                a.write(",")
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[10]), a, indent=2)
                if (row[11].strip() == ""):
                    row[11] = "null"
                a.write(": " + row[11].strip())#necessary data implemented to json file properly
                a.write(",")
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[11]), a, indent=2)
                a.write(": " + row[10].strip())#necessary data implemented to json file properly
                a.write(",")
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[12]), a, indent=2)
                a.write(": " + '"' + row[9].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[13]), a, indent=2)
                if (row[13] == "" or row[13] is None):

                    row[13] = "null"
                    a.write(": "+ row[13].strip() + ',')
                else:
                    a.write(": " + '"' + row[13].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[14]), a, indent=2)
                if (row[12] == "" or row[12] is  None):
                    row[12] = "null"
                a.write(": " + row[12].strip())#necessary data implemented to json file properly
                a.write(",")
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[15]), a, indent=2)
                if (row[7] == None):
                    row[7] = "null"
                a.write(": " + row[7].strip())#necessary data implemented to json file properly
    with open(output_file, 'a') as a:
        # essential gap was obtained
        a.write("\n\t\t\t\t\t}")
        a.write("\n\t\t\t\t]")
        a.write("\n\t\t\t}\n\t")
        a.write("\t]\n\t")
        a.write("}\n")
        a.write("]")



def JsonToXml(input_file,output_file):
    with open(input_file) as json_file:
        data = json.load(json_file)
    keepData=[]#array created for keep essential data.
    for x in data:
        for y in x["items"]:
            for z in y["department"]:
                if (z["second"] == "No"):
                    z["second"] = ""
                keepData.append([x["uType"],#data added to array
                    x["university name"],
                        y["faculty"],
                            z["id"],
                            z["name"],
                            z["lang"],
                            z["second"],
                            z["grant"],
                            z["period"],
                            z["field"],
                            z["quota"],
                            z["spec"],
                            z["last_min_order"],
                            z["last_min_score"],
                    ])


    line_count = 0
    data = ET.Element("departments")#elements tree used for create xml
    data.tail = "\n"
    data.text = "\n\t"
    flag = True
    tempUNI = ""

    for row in keepData:#data readed row by row


            if (tempUNI != row[1].strip()):
                tempUNI = row[1].strip()
                flag = True
            if (flag):
                items = ET.SubElement(data, "university")#university data and their elements set created.
                items.text = "\n\t\t"
                items.set("name", row[1].strip())
                items.set("uType", row[0].strip())
                data[-1].text = "\n\t\t"

                flag = False

            item1 = ET.SubElement(items, 'item')#item data and their elements set created.
            item1.text = "\n\t\t\t"# essential gap was obtained
            item1.set('id', row[3].strip())
            item1.set('faculty', row[2].strip())
            items[-1].text = "\n\t\t\t"# essential gap was obtained

            item2 = ET.SubElement(item1, 'name')#name data and their elements set created.
            item2.text = "\n\t\t\t"# essential gap was obtained
            item2.set('lang', row[5].strip())

            if (row[6].strip() == ""):
                row[6] = "No"
            item2.set('second', row[6].strip())
            item2.text = row[4].strip()

            item1[-1].tail = "\n\t\t\t"# essential gap was obtained

            item3 = ET.SubElement(item1, 'period')#period data and their elements set created.
            item3.tail = "\n\t\t\t"# essential gap was obtained
            item3.text = str(row[8])
            item1[-1].tail = "\n\t\t\t"# essential gap was obtained

            item4 = ET.SubElement(item1, 'quota')#quota data and their elements set created.
            item4.tail = "\n\t\t\t"# essential gap was obtained
            if(row[11]== None):
                row[11]=""
            item4.set("spec", str(row[11]))
            if (row[10] is not None):
                item4.text = str(row[10])

            item1[-1].tail = "\n\t\t\t"# essential gap was obtained

            item5 = ET.SubElement(item1, 'field')#field data and their elements set created.
            item5.tail = "\n\t\t\t"# essential gap was obtained
            if (row[9] is not None):
                item5.text = str(row[9])

            item1[-1].tail = "\n\t\t\t"

            item6 = ET.SubElement(item1, 'last_min_score ')#last_min_score data and their elements set created.
            item6.tail = "\n\t\t\t"# essential gap was obtained
            if (row[12] == None):
                row[12] = ""
            item6.set("order ", str(row[12]))
            if (row[13] is not None):
                item6.text = str(row[13])

            item1[-1].tail = "\n\t\t\t"# essential gap was obtained

            item7 = ET.SubElement(item1, "grant")#grant data and their elements set created.
            item7.tail = "\n\t\t"# essential gap was obtained
            if(row[7] is not None):
                item7.text =str(row[7])
            item1[-1].tail = "\n\t\t"# essential gap was obtained
            item7.tail = "\n\t\t"

            """
              
            Data has written to xml properly by utf-8 
                         
            """
            mydata = ET.tostring(data)
            myfile = open(output_file, "w")
            myfile.write(mydata.decode("utf-8"))

            line_count += 1



def CsvToJson(input_file,output_file):


    read = open(input_file, 'r')
    line_count = 0
    csv_read = csv.reader(read, delimiter='|')
    temp=""
    temp2=""
    for row in csv_read:#csv read row by row

        if line_count == 0:
            words = ['university name', "uType", "items", "faculty", "department", 'id', 'name',
                     'lang', 'second', 'period', 'spec', 'quota',
                     'field', 'last_min_score','last_min_order','grant']#header was created.


            line_count += 1
        else :
            row[0] = row[0].replace(";", " ;")
            row = row[0].split(";")
            with open(output_file, 'a') as a:

                if((row[1] != temp and row[2] == temp2 and temp!="" and temp2!="")or(row[1] != temp and row[2] != temp2 and temp!="" and temp2!="")):
                    a.write("\n\t\t\t\t\t}")# essential gap was obtained
                    a.write("\n\t\t\t\t]")# essential gap was obtained
                if (row[1] == temp and row[2] == temp2):
                    a.write("\n\t\t\t\t\t},")# essential gap was obtained
                if((row[2] != temp2 and temp!="" and temp2!="") or (row[1] != temp and temp!="" and temp2!="")):
                    a.write("\n\t\t\t}")# essential gap was obtained
                    a.write("\n\t\t]")

                if(temp!="" and row[1] != temp):
                    a.write("\n\t},\n\t\t")# essential gap was obtained




                if (row[1] != temp):
                    if(temp==""):
                        a.write("[\n\t")# essential gap was obtained
                    a.write("{\n\t\t")
                    json.dump((words[0]), a, indent=2)
                    a.write(": " + '"' + row[1].strip() + '",')
                    a.write("\n\t\t")# essential gap was obtained
                    json.dump((words[1]), a, indent=2)
                    a.write(": " + '"' + row[0].strip() + '",')
                    a.write("\n\t\t")# essential gap was obtained
                    json.dump((words[2]), a, indent=2)
                    a.write(": ")
                    a.write("\n\t\t[")# essential gap was obtained
                    temp = row[1]#necessary data implemented to json file properly
                    temp2="-"


                if (row[2] != temp2):
                    a.write("\n\t\t\t{\n\t\t\t")# essential gap was obtained
                    a.write("\n\t\t\t\t")
                    json.dump((words[3]), a, indent=2)
                    a.write(": " + '"' + row[2].strip() + '",')#necessary data implemented to json file properly
                    a.write("\n\t\t\t\t")
                    json.dump((words[4]), a, indent=2)
                    a.write(": ")
                    a.write("\n\t\t\t\t[")# essential gap was obtained
                    a.write("\n\t\t\t\t")
                    temp2=row[2]

                a.write("\n\t\t\t\t\t{")# essential gap was obtained
                a.write("\n\t\t\t\t\t\t")
                json.dump((words[5]), a, indent=2)
                a.write(": " + '"' + row[3].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[6]), a, indent=2)
                a.write(": " + '"' + row[4].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[7]), a, indent=2)
                a.write(": " + '"' + row[5].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[8]), a, indent=2)
                if (row[6].strip() == ""):
                    row[6] = "No"
                a.write(": " + '"' + row[6].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[9]), a, indent=2)
                a.write(": " + row[8].strip() )#necessary data implemented to json file properly
                a.write(",")
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[10]), a, indent=2)
                if (row[11].strip() == ""):
                    row[11] = "null"
                a.write(": "  + row[11].strip() )#necessary data implemented to json file properly
                a.write(",")
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[11]), a, indent=2)
                a.write(": "  + row[10].strip() )#necessary data implemented to json file properly
                a.write(",")
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[12]), a, indent=2)
                a.write(": " + '"' + row[9].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[13]), a, indent=2)
                if (row[13] == "" or row[13] is None):

                    row[13] = "null"
                    a.write(": "+ row[13].strip() + ',')
                else:
                    a.write(": " + '"' + row[13].strip() + '",')#necessary data implemented to json file properly
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[14]), a, indent=2)
                if(row[12].strip()==""):
                    row[12]="null"
                a.write(": "  + row[12].strip() )#necessary data implemented to json file properly
                a.write(",")
                a.write("\n\t\t\t\t\t\t")# essential gap was obtained
                json.dump((words[15]), a, indent=2)
                if(row[7].strip()==""):
                    row[7]= "null"
                a.write(": "  + row[7].strip() )#necessary data implemented to json file properly
    with open(output_file, 'a') as a:
        # essential gap was obtained
        a.write("\n\t\t\t\t\t}")
        a.write("\n\t\t\t\t]")
        a.write("\n\t\t\t}\n\t")
        a.write("\t]\n\t")
        a.write("}\n")
        a.write("]")


def JsonToCsv(input_file,output_file):

    with open(input_file) as json_file:
        data = json.load(json_file)


    f = csv.writer(open(output_file, "w"),delimiter=(";"))


    f.writerow(["ÜNİVERSİTE_TÜRÜ","ÜNİVERSİTE","FAKÜLTE","PROGRAM_KODU","PROGRAM","DİL","ÖĞRENİM_TÜRÜ","BURS","ÖĞRENİM_SÜRESİ","PUAN_TÜRÜ","KONTENJAN","OKUL_BİRİNCİSİ_KONTENJANI","GEÇEN_YIL_MİN_SIRALAMA","GEÇEN_YIL_MİN_PUAN"])
    # Writing Headers
    for x in data:
        for y in x["items"]:#data writed to array
            for z in y["department"]:
                if (z["second"] == "No"):
                    z["second"] = ""
                f.writerow([x["uType"],
                    x["university name"],
                        y["faculty"],
                            z["id"],
                            z["name"],
                            z["lang"],
                            z["second"],
                            z["grant"],
                            z["period"],
                            z["field"],
                            z["quota"],
                            z["spec"],
                            z["last_min_order"],
                            z["last_min_score"],
                    ])


def XmlValidatesXsd(input_file,output_file):#input file should take xml output file should take xsd name .


    
    xml_file = etree.parse(input_file)
    xml_validator = etree.XMLSchema(file=output_file)

    is_valid = xml_validator.validate(xml_file)

    print(is_valid)#valid true or false was printed.
    


Main(sys.argv[1],sys.argv[2],sys.argv[3])#main function are called.
