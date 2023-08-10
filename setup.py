from setuptools import find_packages, setup

package_name = 'vicon_sub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tangjs',
    maintainer_email='tangjs@umich.edu',
    description='Simple sub to Vicon msgs',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'listener = vicon_sub.vicon_subscriber:main'
        ],
    },
)
