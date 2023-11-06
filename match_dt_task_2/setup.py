import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'match_dt_task_2'

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
    maintainer_email='nhkw0001@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "task_2a_node = match_dt_task_2.task_2a:main",
            "task_2b_node = match_dt_task_2.task_2b:main",
            "task_2c_node = match_dt_task_2.task_2c:main",
            "task_2d_node = match_dt_task_2.task_2d:main",
            "task_2e_node = match_dt_task_2.task_2e:main",
            "task_2f_node = match_dt_task_2.task_2f:main",
            "task_2g_node = match_dt_task_2.task_2g:main",
            "task_2h_node = match_dt_task_2.task_2h:main",
            "task_2i_node = match_dt_task_2.task_2i:main",
            "milestone_1_node = match_dt_task_2.milestone_1:main"
        ],
    },
)
