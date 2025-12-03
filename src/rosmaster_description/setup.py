from setuptools import setup
import os
from glob import glob   # 이 줄 꼭 있어야 합니다

package_name = 'rosmaster_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # urdf, meshes, launch 설치
        ('share/' + package_name + '/urdf',   glob('urdf/*')),
        ('share/' + package_name + '/meshes', glob('meshes/*')),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wens',
    maintainer_email='you@example.com',
    description='UGV description package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

