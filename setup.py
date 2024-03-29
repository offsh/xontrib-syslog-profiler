#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = '''
                        A Xonsh plugin to profile and log command execution to a syslog file. It uses the default
                        Xonsh JSON history backend modified to also log into a syslog_formated text file.
                        '''

setuptools.setup(
    name='xontrib-syslog-shell-profiler',
    version='0.1.5',
    license='MIT',
    author='Francisco Navarro',
    author_email='navarromoralesdev@gmail.com',
    description="A Xonsh plugin to profile and log command execution to a syslog file.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=['xonsh'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    url='https://github.com/grg121/xontrib-syslog-shell-profiler',
    project_urls={
        "Documentation": "https://github.com/grg121/xontrib-syslog-shell-profiler/blob/master/README.md",
        "Code": "https://github.com/grg121/xontrib-syslog-shell-profiler",
        "Issue tracker": "https://github.com/grg121/xontrib-syslog-shell-profiler/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
