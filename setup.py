from setuptools import setup

setup(name='nestedfacts',
      description='This library enables users of Ansible to load nested'
                  'directories as local facts. Refer to the README for'
                  'more details.',
      author='uberspace.de',
      author_email='hallo@uberspace.de',
      url='https://github.com/uberspace/nestedfacts',
      version='0.2.0',
      license='MIT',
      packages=['.'],
      zip_safe=True,
      install_requires=[
            'pyyaml',
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'Topic :: System :: Systems Administration',
          'Topic :: Utilities',
          'Natural Language :: English',
          'Operating System :: POSIX :: Linux',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
      ],
)
