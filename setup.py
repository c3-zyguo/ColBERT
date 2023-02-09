import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='ColBERT1',
    version='0.2.0',
    author='Omar Khattab',
    author_email='okhattab@stanford.edu',
    description="Efficient and Effective Passage Search via Contextualized Late Interaction over BERT",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/c3-zyguo/ColBERT',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
