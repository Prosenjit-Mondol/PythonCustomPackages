from setuptools import setup, find_packages # type: ignore


setup(
    name="prosen",
    version="0.0.4",
    author="Prosenjit Mondol",
    author_email="prosenjit1156@gmail.com",
    url="https://www.youtube.com/@prosen2001",
    description="An application that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Inddependent",
    ],
    install_requires=["click","pytz"],
    entry_points={"console_scripts": ["prosen = src.main:main"],},

)