from setuptools import setup, find_packages

# Read README file for long description
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "Electrophysiology data analysis tools"

setup(
    name="ephys_analysis",
    version="0.1.0",
    author="Meghan Cum", 
    author_email="meghanic96@gmail.com",  
    description="Tools for electrophysiology data analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/padillacoreanolab/ephys_analysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics :: Neuroscience :: Electrophysiology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.9",
    # No install_requires - conda environment handles all dependencies
    install_requires=[],
    
    # Optional: Only add packages not available in conda
    extras_require={
        "optional": [
            # Only add packages that aren't in your conda environment
            # or are difficult to install via conda
        ],
    },
    entry_points={
        "console_scripts": [
            # Add command-line tools if you have any
            # "ephys-tool=ephys_analysis.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)