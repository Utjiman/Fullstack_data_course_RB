from setuptools import setup
from setuptools import find_packages

# NOT FINISHED YET

# find_packages will find all the packages with __init__.py
print(find_packages())

setup(
    name="travel_planner",
    version="1.0.0",
    description="""
    This package is used for travel planning in public transport. 
    It has backend code, frontend code and utils.  
    """,
    author="Kokchun",
    author_email="YOUR_EMAIL@mail.com",
    # url
    install_requires=["streamlit", "pandas", "duckdb"],
    packages=find_packages(exclude=("test*", "explorations")),
    entry_points={"console_scripts": ["dashboard = utils.run_dashboard:run_dashboard"]},
)
