import os
import json


def get_selenoid_json_config():
    path = os.path.dirname((os.path.abspath(__file__))) + "/config/browsers.json"
    with open(path, "r") as file:
        config = json.load(file)
    return config


def get_config_browsers_version():
    config = get_selenoid_json_config()
    act = {}
    for browser_name, browser_version in config.items():
        act[browser_name] = browser_version["default"]
    return act


def create_script():
    conf = get_config_browsers_version()
    with open("selenoid_images.sh", "w") as file:
        for keys, value in conf.items():
            file.write(f"docker pull selenoid/{keys}:{value}" + '\n')


create_script()