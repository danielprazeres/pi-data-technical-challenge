from setuptools import setup, find_packages

setup(
    name="character-api",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn==0.24.0",
        "sqlalchemy==2.0.23",
        "pydantic==2.5.2",
        "python-dotenv==1.0.0",
        "pytest==7.4.3",
        "httpx==0.25.2"
    ],
) 