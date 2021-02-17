import setuptools

setuptools.setup(
    name="unipass",
    version="0.1",
    license='MIT',
    author="Sangjun Jung",
    author_email="bandoche@hanmail.net",
    description="Korean custom unipass OpenAPI wrapper",
    long_description=open('README.md').read(),
    url="http://github.com/bandoche/unipass",
    packages=setuptools.find_packages(),
    install_requires=[
        'httpx==0.16.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
    ],
)
