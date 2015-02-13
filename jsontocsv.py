import json

class JsonToCsv:

    def __init__(self, format, format_delimeter=",", output_delimeter=","):
        self.format = format
        self.format_delimeter = format_delimeter
        self.output_delimeter = output_delimeter

    def process_json(self, json_input):
        if (type(json_input) is not dict and type(json_input) is not list):
            raise TypeError("process_json requires json to be a dict or list")

        columns = self.format.split(self.format_delimeter)
        output = ""

        for obj in json_input:
            for key in columns:
                if key.find(".") >= 0:
                    output += str(self.nested_item(key.split("."), obj)).strip()
                elif key.find("[") >= 0:
                    key, index = self.keypath_index(key)
                    output += str(obj[key][index]).strip()
                else:
                    output += str(obj[key]).strip()
                output += ","

            output = output[0:-1] #remove trailing comma
            output += "\n"
        return output

    def nested_item(self, keypath, json_input):
        if (len(keypath) == 1):
            return json_input[keypath[0]]
        elif keypath[0].find("[") >= 0:
            key, index = self.keypath_index(keypath[0])
            return self.nested_item(keypath[1:len(keypath)], 
                json_input[key][index])
        else:
            return self.nested_item(keypath[1:len(keypath)], 
                json_input[keypath[0]])

    def keypath_index(self, keypath):
        elements = keypath.split("[")
        elements[-1] = int(elements[-1][0:-1])
        return elements[0], elements[1]