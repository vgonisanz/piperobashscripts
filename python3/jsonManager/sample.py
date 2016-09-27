from jsonManager import JsonManager
import sys
import os

# Sample functions
#############################################################
def abort_exe( exit_message ):
    print(exit_message)
    print("Aborting...")
    sys.exit(0)
    return

def process_key(self, key, newvalue):
    print("Changing key: %s with value: %s" % (key, newvalue))

def testinfo(self):
    print("testinfo")

def try_wrong_file():
    print("-- try_wrong_file ------------------------------------------")
    # Create instance
    parser = JsonManager('parser')
    # Try to parse wrong file
    successful, json_data = parser.read_json_from_file("wrong_file.json")
    print("successful? %s" % successful)
    print("------------------------------------------------------------")
    return

def try_read_file():
    print("-- try_read_file ------------------------------------------")

    # Configure variables to provide to class sample
    #############################################################
    jsonkeys = ['a', 'b', 'd']
    input_path = os.path.join(os.getcwd(), "input/")

    # Create instance
    parser = JsonManager('parser')
    # Set array with keys
    parser.set_key_array(jsonkeys)
    # Set input path
    parser.set_input_path(input_path)
    # Parse json file
    successful, json_data = parser.read_json_from_file("test.json")
    print("successful? %s" % successful)

    # Get a value if exist or print error
    value = parser.get_value(json_data, 'f')
    print("Value is: %s" % value)
    # Print and get a value
    value = parser.print_json_value(json_data, 'a')
    # Print all json values
    parser.print_all_json_values(json_data)
    # Print only values in array
    parser.print_arraykey_json_values(json_data, jsonkeys)
    print("------------------------------------------------------------")
    return

def try_create_file():
    print("-- try_create_file ------------------------------------------")
    output_path = os.path.join(os.getcwd(), "output/")
    json_values_array = []
    json_values_array.append(["key1", "value1"])
    json_values_array.append(["key2", "value2"])
    json_values_array.append(["key3", "value4"])

    # Create instance
    parser = JsonManager('parser')
    parser.set_output_path(output_path)

    # Try to create json object
    successful, json_data = parser.create_json_object_from_list(json_values_array)
    parser.print_all_json_values(json_data)
    print("successful? %s" % successful)
    parser.write_json("test_output.json", json_data)
    print("------------------------------------------------------------")
    return

def try_process_with_external_function():
    print("-- try_process_with_external_function ------------------------------------------")
    # Process default
    #parser.process_function()
    # Overload processing with function
    #parser.set_process_function(process_key)
    # Call new process function
    #parser.process_function("key", "value")
    print("------------------------------------------------------------")

def initialize():
    scriptname = sys.argv[0]
    pathname = os.path.dirname(sys.argv[0])
    full_path_name = os.path.abspath(pathname)
    print('Executing: ', scriptname)
    # Create output path if needed
    output_path = os.path.join(full_path_name, "output/")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

if __name__ == '__main__':
    # Initialize
    ###########################################################
    initialize()

    # Use class
    ###########################################################
    try_wrong_file()
    try_read_file()
    try_create_file()

    # parser.test()
    print("Finish.")
