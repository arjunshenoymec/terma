from setuptools import setup

setup(
    name='terma',
    version='1.0.1',
    author='Arjun Shenoy A V',
    author_email='arjunshenoyav@gmail.com',
    description='Terminal Assistant',
    long_description=open("README.md").read(),
    packages=['terma'],
    install_requires=[
        "openai",
        "prompt-toolkit >= 3.0.37",
        "pyperclip >= 1.8.2",
    ],
    entry_points={
        'console_scripts': [
            'terma=terma.app:main',
        ],
    },
)
