# rover

# Getting started 

This guide you through how to run the project using ROS `humble` . 

## Build 

Installing  colcon build maybe required 

```
 colcon build 
```

Set up rover image
```
firelord@FireLord:~/rover$ source install/setup.bash
firelord@FireLord:~/rover$ colcon list                                                                                                                               rover   .       (ros.ament_cmake)
```

## RViz Visualiztion

Rviz only used for virtualization the robot , any simulation must be done on Gazebo

```
ros2 launch  display.launch.py
```

## Gazebo simulation setup

Creating SDF files so Gazebo could read it 

```
gz sdf -p
```