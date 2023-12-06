import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'match_dt_task_4'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "launch"), glob("launch/*.launch.py")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nhkw0001',
    maintainer_email='henrik.lurz@web.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "task_4a_node = match_dt_task_4.task_4a:main",
            "task_4b_node = match_dt_task_4.task_4b:main",
            "task_4c_node = match_dt_task_4.task_4c:main",
            "task_4d_node = match_dt_task_4.task_4d:main",
            "milestone_4_node = match_dt_task_4.milestone_4:main"
        ],
    },
)
