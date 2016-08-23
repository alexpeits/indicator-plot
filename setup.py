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
        'numpy==1.11.1',
        'matplotlib==1.5.1',
        'sympy==0.7.6.1'
    ],
    include_package_data=True,
    zip_safe=False
)
