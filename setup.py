# -*- coding: utf-8 -*-
"""
Created: 7-13-2020
@author: Gerardo Cervantes
"""

import setuptools

setuptools.setup(
    name='Star-Classifier-For-Mario-64',  # Replace with your own username
    version='0.96.1',
    author='Gerardo Cervantes',
    author_email='geras22222c@gmail.com',
    description='Auto-splitter for Super Mario 64',
    long_description='Classifies amount of stars you have in game Super Mario 64. '
                     'Useful in speedruns when timing how long it takes to get each star',
    long_description_content_type='text/markdown',
    url='https://github.com/gcervantes8/Star-Classifier-For-Mario-64',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Win32 (MS Windows)',
    ],
    python_requires='~=3.4',
    install_requires=[
            'wheel',
            'pillow',
            'pyautogui',
            'mss',
            'pypiwin32',
            'pynput',
            'tensorflow == 2.5.0',
            'keras == 2.2.5'
        ]
)
