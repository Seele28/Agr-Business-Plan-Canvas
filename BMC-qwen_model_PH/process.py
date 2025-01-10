import os
import json



def parse_answer(answer):
    if isinstance(answer, str):
        # Parse string to JSON
        parsed_ans = json.loads(answer)
    elif isinstance(answer, list):
        # If it's a list (chat history), get the last bot message
        for msg in reversed(answer):
            if isinstance(msg, dict) and 'content' in msg:
                parsed_ans = json.loads(msg['content'])
                break
    else:
        # If it's already a dict
        parsed_ans = answer

    # Ensure all values are lists
    for k, v in parsed_ans.items():
        if not isinstance(v, list):
            parsed_ans[k] = [v]

    return parsed_ans

def load_examples():
    # Define the directory containing the JSON files
    directory = 'dataProcess/data'

    # Initialize an empty list to hold the JSON strings
    json_strings = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                # Read the file content and append to the list
                json_strings.append(file.read())

    # Now json_strings contains all the JSON file contents as strings
    # for i, json_str in enumerate(json_strings):
    #     print(f"Content of file {i+1}: {json_str[:100]}...")  # Print first 100 characters of each file for verification
    return json_strings

def extract_json_content(string):
    start = string.find('{')
    end = string.rfind('}')
    if start == -1 or end == -1:
        raise ValueError("No valid JSON object found in the string")
    return string[start:end+1]