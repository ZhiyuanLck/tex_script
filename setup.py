from setuptools import setup

setup(
    name='texh',
    version='0.1',
    py_modules=['texh'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        texh=texh:texh
    ''',
)
