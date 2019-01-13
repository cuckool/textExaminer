from setuptools import setup

setup(name='textExaminer',
      version='0.1',
      description='An easy to use text processing to get information but mostly useless statistics about text sources ('
                  'Twitter profile, web pages, txt documents...',
      url='https://github.com/cuckool/textExaminer',
      author='Cuckool',
      author_email='mathieu.gaucheler@gmail.com',
      license='',
      packages=['textProcessing'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)