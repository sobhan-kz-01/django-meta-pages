from setuptools import setup,find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="django-meta-pages",
    version="0.0.1",
    license='MIT',
    
    classifiers=[
    'Development Status :: 4 - Beta',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 3.1',
    'Framework :: Django :: 4.1',


],
python_requires=">=3.7",
    author="sobhan-kz-01",
    author_email="sobhan.kz01.dev@gmail.com",
    url='https://github.com/sobhan-kz-01/django-meta-pages',
    description="Django Library To Use Meta Tags And Schema Structure In Any URL Path",
    long_description=long_description,
    install_requires=[
        'Django>=3.2',
        'pillow',
      ],
      
      include_package_data=True,
    long_description_content_type="text/markdown",
    packages=find_packages(),
)