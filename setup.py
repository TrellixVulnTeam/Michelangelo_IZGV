import io
import os
import subprocess

from setuptools import setup, find_packages

cwd = os.path.dirname(os.path.abspath(__file__))

version = '1.0.0'
try:
    if not os.getenv('RELEASE'):
        from datetime import date
        today = date.today()
        day = today.strftime("b%Y%m%d")
        version += day
except Exception:
    pass

def create_version_file():
    global version, cwd
    print('-- Building version ' + version)
    version_path = os.path.join(cwd, 'encoding', 'version.py')
    with open(version_path, 'w') as f:
        f.write('"""This is encoding version file."""\n')
        f.write("__version__ = '{}'\n".format(version))

requirements = [
    'numpy',
    'tqdm',
    'nose',
    'portalocker',
    'Pillow',
    'scipy',
    'requests',
]

if __name__ == '__main__':
    create_version_file()
    setup(
        name="michelangelo",
        version=version,
        author="Younghan Kim",
        author_email="godppkyh@mosqtech.com",
        url="",
        description="Michelangelo: Model Framework in PyTorch",
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        license='MIT',
        install_requires=requirements,
        packages=find_packages(exclude=["tests", "experiments"]),
        package_data={ 'encoding': [
            'LICENSE',
            'lib/cpu/*.h',
            'lib/cpu/*.cpp',
            'lib/gpu/*.h',
            'lib/gpu/*.cpp',
            'lib/gpu/*.cu',
        ]},
    )
