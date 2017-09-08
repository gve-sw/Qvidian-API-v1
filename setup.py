from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='qvidianapi',
      version='0.1',
      description='A Nice Python API to Qvidian.com',
      long_description=readme(),
      url='https://github.com/Abdellbar/qvidianapi',
      author='Abdelbar Aglagane',
      author_email='abdellbar@gmail.com',
      license='Apache License 2.0',
      packages=['qvidianapi'],
      install_requires=[
          'zeep',
          'lxml',
          'HTMLParser',
      ],
      include_package_data=True,
      zip_safe=False)