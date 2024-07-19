from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pystealth',
    version='1.0.0',
    author='Maehdakvan',
    author_email='visitanimation@google.com',
    description='Python module for preventing detection of CDP in Selenium, Puppeteer, and Playwright.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DedInc/pystealth',
    project_urls={
        'Bug Tracker': 'https://github.com/DedInc/pystealth/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires='>=3.6'
)