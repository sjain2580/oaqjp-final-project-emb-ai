# setup.py
from setuptools import setup, find_packages

setup(
    name='EmotionDetection',  # Your chosen package name
    version='0.1.0',          # Initial version number
    author='Sakshi Jain',       # Your name
    author_email='sjain040395@gmail.com', # Your email
    description='A Python package for detecting emotions in text using an external NLP API.',
    long_description=open('README.md').read(), # Optional: Read from README.md
    long_description_content_type='text/markdown', # Specify content type if using markdown
    url='https://github.com/sjain2580/oaqjp-final-project-emb-ai', # Optional: Link to your project repository
    packages=find_packages(), # Automatically finds all packages in the directory
    install_requires=[
        'requests',  # List your package dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', # Choose an appropriate license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', # Specify minimum Python version
)