from setuptools import setup

package_name = 'my_string_publisher'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    py_modules=[],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='String Publisher Node',
    license='BSD-3-Clause',
    entry_points={
        'console_scripts': [
            'StringPublisher = my_string_publisher.publisher_node:main',
        ],
    },
)

