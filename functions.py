from supported_functions import functions
from pyfiglet import Figlet
from clint.textui import colored
import re


def parse_help_of_functions():
    """
        This function creates help description of function to shows in help of command
    :return: String text that shows in help text
    """
    additional_information = ''
    for function in functions:
        additional_information += '{} (Ex. {})\n'.format(function['help'], colored.green(function['example']))
    return additional_information


def is_in_supported_commands(cmd):
    """
        This function checks that command from user input is supported or not
    :param cmd: input command
    :return: False or user command
    """
    for function in functions:
        if function['command'] == cmd:
            return function
    return False


def show_app_demo():
    """
    Print demo of applications
    :return:
    """
    print(colored.cyan('====================== Welcome =================================='))
    print(colored.green('= This command shows some geo data that based on typed function ='))
    f = Figlet(font='slant')
    print(f.renderText('MADGIX Geo'))
    print(colored.blue('=          Wrote by Soheil Tayyeb Naeini on 01-05-2021          ='))
    print(colored.cyan('================================================================='))


def create_formatted_result(result_format, rest_result):
    list_has_index = re.compile("^.*\[[0-9\]]+$")
    get_array_index = re.compile("\[[0-9\]]+")
    printed_result = {}
    for item in result_format:
        indexes = result_format[item].split(".")
        if len(indexes) > 1:
            dd = rest_result
            for index in indexes:
                if list_has_index.match(index):
                    array_index = get_array_index.findall(index)
                    array_index = array_index[len(array_index) - 1]
                    index = index.replace(array_index, "")
                    array_index = int(str(array_index).replace("[", "").replace("]", ""))
                    dd = dd[index][array_index]
                else:
                    dd = dd[index]
            printed_result[item] = dd
        else:
            printed_result[item] = rest_result[result_format[item]]
    return printed_result
