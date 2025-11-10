"""Setup script for SynarkOS."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="synarkos",
    version="0.1.0",
    author="SynarkOS Team",
    author_email="team@synarkos.ai",
    description="Enterprise-grade multi-agent AI orchestration framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/synarkos/synarkos",
    packages=find_packages(exclude=["tests*", "docs*", "examples*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
        "anthropic>=0.18.0",
        "pydantic>=2.0.0",
        "requests>=2.31.0",
        "aiohttp>=3.9.0",
        "python-dotenv>=1.0.0",
        "tenacity>=8.2.0",
        "redis>=5.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.0.0",
            "ruff>=0.1.0",
            "mypy>=1.5.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "synarkos=synarkos.__main__:main",
        ],
    },
    keywords="ai agents multi-agent orchestration llm gpt autonomous",
    project_urls={
        "Documentation": "https://docs.synarkos.ai",
        "Source": "https://github.com/synarkos/synarkos",
        "Bug Reports": "https://github.com/synarkos/synarkos/issues",
    },
)
