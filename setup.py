from pathlib import Path
from setuptools import setup, find_packages


ROOT = Path(__file__).resolve().parent
README = (ROOT / "readme.md").read_text(encoding="utf-8")


setup(
    name="AppForge",
    version="0.1.0",
    description="Benchmark for LLM-driven Android app generation",
    long_description=README,
    long_description_content_type="text/markdown",
    author="AppForge Contributors",
    url="https://github.com/TongmingLAIC/AppForge",
    packages=find_packages(exclude=("examples", "documentation")),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "docker",
        "openpyxl",
        "numpy",
    ],
    extras_require={
        "example": [
            "openai==0.28",
            "anthropic",
            "tenacity",
            "dashscope",
        ],
        "local": [],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)