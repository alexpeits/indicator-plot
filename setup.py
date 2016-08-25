from setuptools import setup, find_packages

setup(
    name='indicator_plot',
    version=0.1,
    author='Alex Peitsinis',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'indicator-plot = indicator_plot.indicator:main'
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
