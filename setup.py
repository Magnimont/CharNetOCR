from setuptools import setup, find_packages 
from pathlib import Path

this_dir = Path(__file__).parent

setup(
    name='CharNetOCR',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    version='1.0.2',
    author='aakash_engineer',
    packages=find_packages(include=["CharNetOCR", "CharNetOCR.*"]),
    include_package_data=True,
    package_data={
        "CharNetOCR": ["models/*.pt"]  # Include YOLO model weights
    },
    install_requires=[
        'ultralytics',
        'opencv-python',
        'numpy'
    ]
)