from setuptools import find_packages, setup

package_name = 'day11_python_package'

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
    description='A ROS 2 Python package demonstrating Publisher and Subscriber communication.',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher = day11_python_package.publisher:main',
            'subscriber = day11_python_package.subscriber:main',
        ],
    },
)
