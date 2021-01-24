import setuptools

with open('README.md') as fp:
    long_description = fp.read()


def parse_requirements_file():
    with open("requirements.txt") as fp:
        dependencies = (d.strip() for d in fp.read().split("\n") if d.strip())
        return [d for d in dependencies if not d.startswith("#")]


setuptools.setup(
    name='Lil-Fluffy-V3',
    version='BETA',
    author='Luffy404',
    description='This Bot is created by Luffy404 and can execute various Tasks',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Luffy404/Lil-Fluffy',
    packages=setuptools.find_packages,
    include_package_data=True,
    install_requires=parse_requirements_file(),
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.9',
    ]
)
