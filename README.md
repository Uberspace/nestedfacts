# Ansible Nested Facts

Ansible supports having [a directory of variables](http://docs.ansible.com/ansible/playbooks_variables.html#local-facts-facts-d)
which are loaded for every task. These facts cannot be nested in any way,
limiting their usefullness.

This script can be placed in `/etc/ansible/facts.d/` to load additional
facts. It supports loading yml from a nested directory structure as
shown below.

```
$ tree scratch
scratch
└── someone
    ├── ports.yml
    └── webserver
        └── domains.yml

$ pip install nestedfacts
$ python -m 'nestedfacts' scratch 
{
  "someone": {
    "webserver": {
      "domains": [
        "google.com", 
        "yolo.org"
      ]
    }, 
    "ports": {
      "55552": "both", 
      "62250": "tcp"
    }
  }
}
```

## Usage

By default the script loads yml from the current directory. There are
two ways to influence this: a) pass a directory to the module, as show
above. b) the more interesting way: use the script as a library.

For this purpose, a new python script in `/etc/ansible/facts.d/` needs
to be created:

```python
#!/usr/bin/env python
from nestedfacts import dump_yml_filedir
dump_yml_filedir('/etc/ansible/fancyfacts')
```

Please note that the file needs to be named `<something>.fact` and needs
executable-rights for ansible to include it.

## Errors

There are a few scenarios where a file cannot be loaded.

1. It contains invalid yml. In this case, the key is present, but set to
`null`:

```
$ tree invalid_file
invalid_file
├── foo.yml
└── invalid.yml

$ cat invalid_file/invalid.yml
{{{{{

$ python -m 'nestedfacts' invalid_file
{
  "foo": 42,
  "invalid": null
}
```

2. non-yml-files. When the script encounters something, that does not
end in `.yml`, the file is ignored completely:

```
$ tree nonyaml_dir/
nonyaml_dir/
├── foo.yml
└── somethingelse

$ python -m 'nestedfacts' nonyaml_dir/
{
  "foo": 43
}
```

3. In case the provided root is missing `{}` is returned.

4. In case a non-yml-file is provided as the root `null` is returned.

## Development

### Setup

```
virtualenv  venv --python python2
source venv/bin/activate
pip install -r requirements-dev.txt
```

You are free to play around in the `scratch`-directory, which is ignored
by git. See the example above for directory structure and invocation. If
you add or change something, you probably want to write a test for that.

### Tests

Tests are managed by [`tox`](https://tox.readthedocs.io) and tested by
the [`pytest`-module](http://doc.pytest.org). You can run them using the
`tox`-command.

## Deployment

The only file in this directory needed in production is `userfacts.py`.
Copy, clone or simlink it into your `/etc/ansible/facts.d/preferences.fact`-
directory using your favourte deployment tool. Please note that this
script needs the [`pyyaml`-module](http://pyyaml.org) to work.

### PyPI

Assuming you have been handed the required credentials, the package on
PyPI can be updated like this:

```
rm dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
```
