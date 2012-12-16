from setuptools import setup

setup(
    name='scrapy-simple-http-queue',
    version='0.1.0',
    description='Allow to use scrapy with simple-http-queue',
    keywords='scrapy distributed crawl queue http sqlite python tornado',
    license='New BSD License',
    author="Francois Dang Ngoc",
    author_email='francois.dangngoc@gmail.com',
    url='http://github.com/darthbear/scrapy-simple-http-queue/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    packages=[
        'scrapy_simple_http_queue',
    ],
    install_requires=[
        'simple_http_queue',
    ],
)
