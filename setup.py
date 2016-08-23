from setuptools import setup, find_packages

setup(
    name='plodicator',
    version=0.1,
    author='Alex Peitsinis',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'plodicator = plodicator.indicator:main'
        ]
    },
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    include_package_data=True,
    zip_safe=False
)
