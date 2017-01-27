from setuptools import setup, find_packages

setup(name='meta music',
      version='1',
      description='search metadata for music files',
      long_description='search metadata by fingerprinting the music file',
      author='Tal Vintrob',
      packages=find_packages(),
      install_requires=['requests', 'pyacoustid', 'eyed3'],
      entry_points={'console_scripts': ['meta=meta_music.__main__:main']},
      license='MIT',
      keywords=['meta', 'music', 'fingerprint'])
