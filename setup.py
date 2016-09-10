from distutils.core import setup

setup(
    name='pypat',
    version='1.1',
    description='Python Design Patterns',
    author='Tyler LaBerge',
    author_email='tyler.laberge@maine.edu',
    url='https://github.com/tylerlaberge/PyPat',
    download_url='https://github.com/tylerlaberge/PyPat/tarball/v1.1',
    keywords=['design', 'pattern', 'patterns'],
    classifiers=[],
    packages=[
        'pypat',
        'pypat.creational',
        'pypat.behavioral',
        'pypat.structural'
    ],
)

