from setuptools import setup, find_packages

setup(
    name='llm_cost_estimator',
    version='0.0.1',
    description='Estimate costs of batch text generation for OpenAI models',
    author='Gabriel Simmons',
    packages=find_packages(),
    install_requires=[
        "tiktoken",
    ],
)