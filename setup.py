from setuptools import setup

setup(name='nestedfacts',
      version='0.1',
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
