#!/usr/bin/env python2

import os
import json
import sys
import yaml

ROOT_DIR = sys.argv[1] if len(sys.argv) > 1 else 'scratch'
YML_FILE_SUFFIX = '.yml'


def load_yml_filedir(path):
    o = {}

    if os.path.isfile(path):
        try:
          return yaml.load(open(path))
        except:
          return None
  
    for e in os.listdir(path):
        epath = os.path.join(path, e)
        if os.path.isdir(epath):
            o[e] = load_yml_filedir(epath)
        elif epath.endswith(YML_FILE_SUFFIX):
            o[e[:-len(YML_FILE_SUFFIX)]] = load_yml_filedir(epath)
    
    return o


if __name__ == "__main__":
    users = load_yml_filedir(ROOT_DIR)
    json.dump(users, sys.stdout, indent=2)
