import base64
import json
import os
import requests
import argparse



allure_results_directory = '/allure-results'
allure_server = 'http://localhost:5050'
# project_id = 'default'
results_directory = os.path.dirname(os.path.realpath(__file__)) + allure_results_directory



project_id = "default"


def get_files_list():
    return os.listdir(results_directory)


def convert_to_base64(files):
    results = []
    for file in files:
        result = {}
        file_path = results_directory + "/" + file
        try:
            with open(file_path, "rb") as f:
                if os.path.isfile(file_path):
                    try:
                        content = f.read()
                        if content.strip():
                            b64_content = base64.b64encode(content)
                            result['file_name'] = file
                            result['content_base64'] = b64_content.decode('UTF-8')
                            results.append(result)
                        else:
                            print('Empty File skipped: ' + file_path)
                    finally:
                        f.close()
                else:
                    print('Directory skipped: ' + file_path)
        except:
            pass
    return results


def preparation_json_data():
    request_body = {
        "results": convert_to_base64(get_files_list())
    }
    return json.dumps(request_body)


def sends():
    session = requests.Session()
    response = session.post(
        allure_server + '/allure-docker-service/send-results?project_id=' + project_id + "&force_project_creation=true",
        headers={'Content-type': 'application/json'}, data=preparation_json_data())
    return response
