import json
from decorators.coroutine_decorator import coroutine_decorator
'''
Takes the output of the consolidator as its input and outputs the analytics in the form of JSON data.
'''
@coroutine_decorator
def output_writer():
    while True:
        data = yield
        with open('./output/output.data', 'a', encoding='utf-8') as output_file:
            json_data = json.dumps(data, indent=4)
            output_file.write(json_data + '\n \n')

