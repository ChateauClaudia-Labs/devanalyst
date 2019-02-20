from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='devanalyst',
      version='0.1',
      description='Tools to simulate and analyze software development lifecycles',
      long_description=long_description,
      long_description_content_type="text/markdown",      
      url='http://github.com/alejandrohd/devanalyst',
      author='Alejandro Hernandez',
      author_email='alejandro.hernandez.chaves@gmail.com',
      license='MIT',
      #packages=setuptools.find_packages(),      
      packages=['devanalyst'],
      install_requires=[
          'pandas', 'numpy', 'IPython', 'nbformat',
      ],
      setup_requires=["pytest-runner", ],
      tests_require=["pytest",],
      include_package_data=True,
      zip_safe=False,
      keywords='development efficiency analysis process simulation',
      classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Software Development',
      ],
)

    


