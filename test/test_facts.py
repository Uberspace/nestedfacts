import os.path

import pytest

import userfacts


DEFAULT_VAL = '_______dd'


@pytest.mark.parametrize("inputfile,expected", [
    ('single_file.yml', ['one', 'two', 'three!']),
    ('simple_dir', {'foo': 5, 'bar': 7}),
    ('nested_dir', {'foo': 5, 'bar': {'nesting': 'is awesome', 'or': ['is', 'it?']}}),
    ('invalid_file', {'foo': 42, 'invalid': None}),
    ('nonyaml_dir', {'foo': 43, 'somethingelse': {}}),
    ('nonyaml_file', DEFAULT_VAL),
    ('___doesnotexist', DEFAULT_VAL),
])
def test_single_file(inputfile, expected):
    data = userfacts.load_yml_filedir(os.path.join(os.path.dirname(__file__), 'data', inputfile), DEFAULT_VAL)
    assert data == expected
