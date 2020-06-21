import rpn
import sys
from setuptools import setup

if sys.version_info.major < 3 or (sys.version_info.minor < 6
                                  and sys.version_info.major == 3):
    sys.exit('Python < 3.6 is unsupported.')

with open('README.md', encoding='utf8') as file:
    long_description = file.read()

setup(
    name='rpn',
    version=rpn.__version__,
    packages=['rpn'],
    package_data={},
    install_requires=['click'],
    license='GNU GPLv3',
    description='Reverse Polish Notation Calculator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=rpn.__author__,
    author_email='james@taran.biz',
    url='https://www.linkedin.com/in/jlaguma/',
    entry_points={'console_scripts': ['rpn = rpn.__main__:main']},
)
