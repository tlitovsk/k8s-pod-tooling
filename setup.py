from setuptools import setup

setup(name='k8s-pod-tooling',
      version='0.1',
      description='implements tooling for the dockerfile ink8s',
      url='',
      author='Tolik Litovsky',
      author_email='anatoly.lit@gmail.com',
      license='GPLv3',
      packages=['k8s-pod-tooling'],
      zip_safe=False,
      install_requires=["dockerfile_parse"])