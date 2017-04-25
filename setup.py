from setuptools import setup, find_packages

setup(
    name = "zhiming",
    version = "0.0.1",
    packages = find_packages(),
    scripts = ['zhiming.py'],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['docutils>=0.3'],
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.md']
    },
    # metadata for upload to PyPI
    platforms = 'any',
    author = "zergl",
    author_email = "e3.gemini@qq.com",
    description = "Yet another restful framework written by Python.",
    license = 'MIT License',
    keywords = ('zhiming', 'rest', 'restful'),
    url = "http://github.com/zergl/zhiming",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
