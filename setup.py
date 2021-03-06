#!/usr/bin/env python
# just fun fun

from distutils.core import setup

setup(name='ops.py',
      version='0.5',
      description='ops.py: makes web apps',
      author='Aaron Swartz',
      author_email='me@aaronsw.com',
      maintainer='Anand Chitipothu',
      maintainer_email='anandology@gmail.com',
      url=' http://opspy.org/',
      packages=['web', 'web.wsgiserver', 'web.contrib'],
      long_description="Think about the ideal way to write a web app. Write the code to make it happen.",
      license="Public domain",
      platforms=["any"],
     )
