from setuptools import setup, find_packages

# Define the name of the package
package_name = "wakeup"

# Define the version of the package
package_version = "0.1.0"

# Define the console script entry point
entry_point = f"{package_name}={package_name}.cli:main"

# Call the setup function to define the package
setup(
    name=package_name,
    version=package_version,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": [entry_point]},
)
