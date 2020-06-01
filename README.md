● The tool takes command line arguments according to the formats you want to convert
between them. A typical command line usage is as follows:
 <"filename"> <"input file"> <"output file/xsd file"> <"type">  

● The first argument, <"filename"> is the python file for conversion operations, <"input
file"> refers to the source filename which will be converted and the third one,
<"output file">, refer to the target filename, or XSD file. The last argument,
<"type">, defines conversion type (1=CSV to XML, 2=XML to CSV, 3=XML to JSON,
4=JSON to XML, 5=CSV to JSON, 6=JSON to CSV,7=XML validates with XSD)

● The sample command line usage converting from XML to JSON as follows:
python ConverterTool.py test.xml test.json 3

# Csv File Explanation
![image](https://github.com/oguzhankrky/Pythonic_Converter_Tool/blob/master/images/csv_file_explanation.png)
