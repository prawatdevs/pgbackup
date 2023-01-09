from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
        name='pgbackup',
        version= '1.0',
        description='Database backup locally or to ASW SW',
        long_description=readme,
        author='Pawan',
        author_email='prawatdevs@gmail.com',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=[]
     )

