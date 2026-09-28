from setuptools import find_packages, setup

package_name = 'day16_parameters_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alisha_inamdar',
    maintainer_email='alishainamdar179@gmail.com',
    description='A ROS 2 Python package demonstrating ROS 2 Parameters.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'parameter_demo = day16_parameters_package.parameter_demo:main',
        ],
    },
)
