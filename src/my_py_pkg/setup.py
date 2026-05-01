from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='omi',
    maintainer_email='omkarhonrao108@gmail.com',
    description='ROS2 Python nodes using custom interface',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'hardware_pub = my_py_pkg.hardware_publisher:main',
            'hardware_sub = my_py_pkg.hardware_subscriber:main',
        ],
    },
)
