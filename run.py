#!/usr/bin/python

import getopt
import sys
import json

from jsontocsv import JsonToCsv
from omekaclient import OmekaClient

def main():

    client = OmekaClient("http://ideumtest01.omeka.net/api/", 
        "26ee48493d9b540742a35e6216da965d1187548a")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:c:h")
    except getopt.GetoptError as err:
        print str(err)
        usage()

    response, content = client.get("items", None, {"collection": 1})
    converter = JsonToCsv("element_texts[0].text,collection.id");
    csv = converter.process_json( json.loads(content) )

    output_filename = ""
    column_names = ""

    for option, arg in opts:
        if option == "-h":
            usage()
        elif option == "-o":
            output_filename = arg
        elif option == "-c":
            column_names = arg

    if len(column_names) > 0:
        line_length = csv.find("\n")
        line = csv[0:line_length]
        column_count = len(line.split(converter.output_delimeter))
        column_count_arg = len(column_names.split(","))
        if column_count_arg != column_count:
            raise SyntaxError("column names input must have same column count as output")
        else:
            formatted_column_names = []
            for name in column_names.split(","):
                formatted_column_names.append(name.strip())
            csv = "#"+",".join(formatted_column_names) + "\n" + csv

    if len(output_filename) > 0:
        write_csv(output_filename, csv)
    else:
        print csv

def usage():
    print "run.py [-c 'column names'] [-o filename]"
    exit(0)

def write_csv(filename, input):
    f = open(filename, "w")
    f.write(input)
    f.close()
    exit(0)

if __name__ == "__main__":
    main()