#!/usr/bin/env python

from setuptools import setup

setup(name='zattoo-channel-url-finder',
      version='1.1.0',
      description='Extract a TV channel URL from Zattoo.',
      url='https://github.com/goggle/zattoo-channel-url-finder',
      author='Alexander Seiler',
      author_email='seileralex@gmail.com',
      license='GPL',
      packages=['channel_finder'],
      package_dir={'channel_finder': 'channel_finder'},
      entry_points={
          'console_scripts': [
              'zattoo-channel-url-finder=channel_finder.channel_finder:main',
          ],
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'License :: Public Domain',
          'Programming Language :: Python :: 3.5'
          'Programming Language :: Python :: 3.6',
      ],
      install_requires=['fuzzywuzzy[speedup]'],
      python_requires='>=3',
      )
