# userfacts.py

A simple script, which loads facts like domains or ports for each user
from a nested directory structure. It is supposed to be used as a
[local fact script](http://docs.ansible.com/ansible/playbooks_variables.html#local-facts-facts-d)
within ansible.

```
$ tree scratch 
scratch
└── someone
    ├── ports.yml
    └── webserver
        └── domains.yml

$ ./userfacts.py scratch 
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
