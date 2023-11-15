import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'match_dt_task_3'

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
            "task_3a_node = match_dt_task_3.task_3a:main",
            "task_3b_node = match_dt_task_3.task_3b:main",
            "task_3c_node = match_dt_task_3.task_3c:main",
            "task_3d_node = match_dt_task_3.task_3d:main",
            "task_3e_node = match_dt_task_3.task_3e:main",
            "task_3f_node = match_dt_task_3.task_3f:main",
            "task_3g_node = match_dt_task_3.task_3g:main",
            "task_3h_node = match_dt_task_3.task_3h:main"
        ],
    },
)
