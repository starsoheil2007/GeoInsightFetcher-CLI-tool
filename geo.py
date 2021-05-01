import argparse
import textwrap
import requests
import json

from functions import *

# Show all demo
show_app_demo()

# Parse Help Of Functions
parse_help_of_functions()

# Create Argument Parser
parser = argparse.ArgumentParser(description="Shows some GEO data", formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\nThis command supported: \n{}'''.format(parse_help_of_functions())))
parser.add_argument('function', metavar='F', type=str, help='Function name')
parser.add_argument('value', metavar='V', type=str, help='Parameter of command')
args = parser.parse_args()

# Check function is valid and select it
selected_command = is_in_supported_commands(args.function)
if selected_command:
    # Create request body
    body = {}
    if "other_body_params" in selected_command and type(selected_command["other_body_params"]) is dict:
        body = selected_command['other_body_params']
    body[selected_command['field_name']] = args.value
    header = {}

    # Create request header
    if "header" in selected_command and type(selected_command["header"]) is dict:
        header = selected_command['header']
    # Send request
    if selected_command["request_method"] == "GET":
        result = requests.get(selected_command["request_url"], params=body, headers=header)
    else:
        result = requests.post(selected_command["request_url"], data=body, headers=header)

    # Check request was successful
    if result.status_code == selected_command["success_status_code"]:
        result = json.loads(result.text)
        # Check for how to print result
        if "result_format" in selected_command:
            print(colored.green(create_formatted_result(selected_command["result_format"], result)))
        else:
            print(colored.green(result))
else:
    print(colored.red('Your command is not supported. Please use -h to got some help.'))
