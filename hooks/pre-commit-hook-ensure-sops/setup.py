import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pre-commit-hook-ensure-sops",
    version="1.1",
    author="Yuvi Panda",
    author_email="yuvipanda@gmail.com",
    description="pre-commit hook to ensure that files that should be encrypted with sops are in fact encrypted",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuvipanda/pre-commit-hook-ensure-sops",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "pre-commit-hook-ensure-sops = pre_commit_hook_ensure_sops.__main__:main",
        ]
    },
    install_requires=[
        "ruamel.yaml",
    ],
    test_requires=[
        "pytest",
    ],
)
