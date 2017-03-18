from io import open

from setuptools import setup, find_packages

embed_video = __import__('embed_video')

setup(
    name='django-embed-video',
    version=embed_video.get_version(),
    description=embed_video.__doc__.strip(),
    long_description=open('README.rst', encoding='utf-8').read() + '\n\n' +
                     open('CHANGES.rst', encoding='utf-8').read(),
    author='Cédric Carrard',
    author_email='cedriccarrard@gmail.com',
    url='https://github.com/jazzband/django-embed-video',
    download_url='https://pypi.python.org/pypi/django-embed-video',
    license='MIT',
    packages=find_packages(exclude=('tests.*', 'tests', 'example_project')),
    install_requires=[
        'Django>=1.8',
        'requests >= 1.2.3',
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['video', 'youtube', 'vimeo', 'soundcloud']
)
