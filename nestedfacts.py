#!/usr/bin/env python

import os
import os.path
import json
import sys
import yaml


def _load_yml_filedir(path):
    """
    Internal function. Do not use.
    Loads all YML-files from the given directory, recursively.
    This function excepts the path to exist.
    """
    YML_FILE_SUFFIX = '.yml'
    bpath = os.path.basename(path)

    if os.path.isdir(path):
        result = {}

        for entry in os.listdir(path):
            epath = os.path.join(path, entry)
            key, value = _load_yml_filedir(epath)

            if not key:
              continue

            result[key] = value

        return bpath, result
    elif os.path.isfile(path):
        if os.path.abspath(path) == os.path.abspath(sys.argv[0]):
            return None, None  # ignore script itself

        if path.endswith(YML_FILE_SUFFIX):
          bpath = bpath[:-len(YML_FILE_SUFFIX)]

          try:
              return bpath, yaml.load(open(path))
          except:
              return bpath, None
        else:
          return None, None



def load_yml_filedir(root_dir):
    """ load the given directory and return the data as a dict """
    if os.path.exists(root_dir):
        return _load_yml_filedir(root_dir)[1]
    else:
        return {}


def dump_yml_filedir(root_dir):
    """ load the given directory and print the data as formatted json """
    result = load_yml_filedir(root_dir)
    json.dump(result, sys.stdout, indent=2)


if __name__ == "__main__":
    root_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    dump_yml_filedir(root_dir)
