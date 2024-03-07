from setuptools import setup, find_packages

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path):
    """
    This function returns requirements list.
    """

    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements


setup(
    name='genericmlproject',
    version='0.0.1',
    description='A simple generic ml package',
    author='Hassan Hajimohammadi',
    author_email='hasanhasanhaji@gmail.com.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
