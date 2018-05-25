from setuptools import setup

requires = [
    "certifi==2018.4.16",
    "chardet==3.0.4",
    "gTTS==1.2.2",
    "gTTS-token==1.1.1",
    "idna==2.6",
    "Janome==0.3.6",
    "mutagen==1.40.0",
    "pygame==1.9.3",
    "requests==2.18.4",
    "six==1.11.0",
    "urllib3==1.22"
]

setup(
    name='japanese',
    version='0.2.1',
    descrption='Python Japanese library for Humans',
    url='https://github.com/kekeho/japanese',
    author='Hiroki Takemura',
    author_email='hirodora@me.com',
    license='MIT',
    keywords='japanese utils util',
    packages=["japanese",],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Natural Language :: Japanese'
    ],
    install_requires=requires,
)