from setuptools import setup
from setuptools import find_packages

# NOT FINISHED YET

# find_packages will find all the packages with __init__.py
print(find_packages())

setup(
    name = "travel_planner",
    version="1.0.0",
    description="this package contains some sample hello world code",
    author = "Kokchun Giang",
    author_email="kokchun.giang@aigineer.se",
    #url
    #install_requires = []
    packages=find_packages(exclude=("test*",)),
    entry_points = {
        "console_scripts": ["hello-world-cli = hello_world.main:main"]
    }
)
