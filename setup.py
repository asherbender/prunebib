from setuptools import setup

setup(
    name='prunebib',
    version='1.0',
    author='Asher Bender',
    author_email='a.bender.dev@gmail.com',
    description=("Prune BibTeX file based on LaTeX citations."),
    scripts=['prunebib'],
    install_requires=[
        'bibtexparser',         # Tested on 0.6.0
    ]
)
