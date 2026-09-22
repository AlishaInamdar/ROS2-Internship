from setuptools import find_packages, setup

package_name = 'day14_clients_package'

setup(
    name=package_name,
    version='1.0.0',
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
    description='ROS 2 Python package demonstrating service client communication.',
    license='MIT',
    entry_points={
        'console_scripts': [
            'service_client = day14_clients_package.service_client:main',
        ],
    },
)
