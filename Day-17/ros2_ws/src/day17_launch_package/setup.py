from setuptools import find_packages, setup

package_name = 'day17_launch_package'

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
        (
            'share/' + package_name + '/launch',
            ['launch/launch_demo.py']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alisha_inamdar',
    maintainer_email='alishainamdar179@gmail.com',
    description='A ROS 2 Python package demonstrating Launch Files.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = day17_launch_package.publisher_node:main',
            'subscriber_node = day17_launch_package.subscriber_node:main',
        ],
    },
)
