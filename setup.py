from distutils.core import setup
setup(
  name = 'beatnik',
  packages = ['beatnik'],
  version = '0.4',
  license='MIT',
  description = 'beatnik interpreter',
  author = 'Experimental Informatics',
  author_email = 't.liu@khm.de',
  url = 'https://github.com/experimental-informatics/beatnik',
  keywords = ['beatnik', 'esoteric programming language', 'stack-based'],
  install_requires=[
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
