#!/usr/bin/env python2

import os
import json
import sys
import yaml

ROOT_DIR = sys.argv[1] if len(sys.argv) > 1 else 'scratch'
YML_FILE_SUFFIX = '.yml'


def load_yml_filedir(path, default={}):
    if not os.path.exists(path):
        return default

    if os.path.isfile(path):
        if not path.endswith(YML_FILE_SUFFIX):
            return default
        else:
            try:
                return yaml.load(open(path))
            except:
                return None

    o = {}

    for e in os.listdir(path):
        epath = os.path.join(path, e)
        key = e

        if os.path.isfile(epath) and epath.endswith(YML_FILE_SUFFIX):
            key = e[:-len(YML_FILE_SUFFIX)]

        o[key] = load_yml_filedir(epath)
    
    return o


if __name__ == "__main__":
    users = load_yml_filedir(ROOT_DIR)
    json.dump(users, sys.stdout, indent=2)
