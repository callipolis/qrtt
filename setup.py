from setuptools import setup, find_packages


setup(name='qrtt',
      version='0.0.7',
      description='Quantitative research and trading tools.',
      url='https://qrtt.org',
      author='Leopold W.',
      author_email='lsw@lwco.com',
      packages=find_packages(exclude=("tests", "tests_dev")),
      install_requires=['pandas', 'numpy', 'matplotlib', 'seaborn'],
      )
