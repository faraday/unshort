from setuptools import setup

setup(name='unshort',
      version="0.1",
      description=__doc__,
      long_description=open("README").read(),
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Topic :: Internet :: WWW/HTTP"
      ],
      keywords='',
      author="Cagatay Calli",
      author_email="ccalli@gmail.com",
      url="http://github.com/faraday/unshort",
      license='BSD',
      packages=['unshort'],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      )
