# Rover



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

## Tricks when making changes to URDFs
Before we start creating our URDF files there are a couple of things to be aware of when saving our changes.

If you build your workspace with colcon build --symlink-install then you don’t need to rebuild every time you update the URDF, it will be automatic EXCEPT whenever you add a new file. That file needs to get built/copied once, and after that will be kept updated.
You’ll need to quit and relaunch robot_state_publisher each time you make a change.
RViz sometimes won’t pick up all your changes straight away. In this case you'll need to hit the “Reset” button in the bottom corner. If it’s still not updating, try ticking and unticking the display items, or closing and reopening the program.


## RViz Visualiztion

Rviz is used for virtualization, any simulation (physics) must be done on Gazebo

```
ros2 launch  rviz.launch.py
```

## Gazebo simulation setup

Launch `/spawn_entity` service  and check whether it's running 

```
 ros2 launch gazebo_ros gazebo.launch.py
```
```
ros service list | grep "/spawn_entity"
```

Spawn the robot 

```
ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity rover
```
OR
```
ros2 launch sim.launch.py
```
OR 
```
./starting.sh gazebo  
```