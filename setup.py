from setuptools import setup, find_packages
def readme():
  with open('README.md', 'r') as f:
    return f.read()
setup(
  name='Library_explode',
  version='0.0.1',
  author='gog1usss',
  author_email='greengewot@gmail.com',
  description='Im trying to know how to do libraries in python',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='your_url',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'your_github'
  },
  python_requires='>=3.6'
)