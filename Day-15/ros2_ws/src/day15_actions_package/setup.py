from setuptools import find_packages, setup

package_name = 'day15_actions_package'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alisha_inamdar',
    maintainer_email='alisha@example.com',
    description='A ROS 2 Python package demonstrating Action Server and Client communication.',
    license='MIT',
    entry_points={
        'console_scripts': [
            'action_server = day15_actions_package.action_server:main',
            'action_client = day15_actions_package.action_client:main',
        ],
    },
)
