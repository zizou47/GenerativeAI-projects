from setuptools import find_packages, setup

setup(
    name="E-commerce Bot",
    version="0.0.1",
    author="Yazid",
    author_email="yazid.ben-madani@epita.fr",
    packages=find_packages(),  
    install_requires=[
        'langchain-astradb',
        'langchain', 
        'langchain-openai',
        'datasets',
        'pypdf',
        'python-dotenv',
        'flask'
    ]
)
