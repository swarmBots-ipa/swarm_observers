from launch import LaunchDescription
from launch_ros.actions import Node

import sys


for arg in sys.argv:
    if arg.startswith("iterations:="):
        No_of_Iteration = int(arg.split(":=")[1])
        print(No_of_Iteration)

    if arg.startswith("agents:="):
        No_of_Robots = int(arg.split(":=")[1])
        print(No_of_Robots)

def generate_launch_description():
    ld = LaunchDescription([
        Node(
            package='formation_error_observer',
            executable='main',
            arguments=[str(No_of_Iteration),str(No_of_Robots)]
            
        ),

        Node(
            package='localization_error_observer',
            executable='localization_error_observer',
            arguments=[str(No_of_Iteration),str(No_of_Robots)]
            
        )

    ])
     

    return ld