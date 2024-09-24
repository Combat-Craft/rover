#!/usr/bin/bash

WORKING_DIR=$(pwd)  # Get the current working directory

# Function to install required ROS packages
function install() { 
    sudo apt install ros-humble-joint-state-publisher -y
    sudo apt install ros-humble-joint-state-publisher-gui -y
    #Maybe missing some rviz package idk
}

# Function to build the workspace
function build(){ 
    echo "Building the workspace..."
    colcon build  # Build the workspace
    colcon list | grep "rover"
    echo "Done" 
}

# Function to launch RViz
function rviz() {
    echo "Launching RViz..."
    ros2 launch rover rviz.launch.py
}

# Main program logic: process CLI arguments
source $WORKING_DIR/.env
case "$1" in
    install)
        install  # Call install function
        ;;
    build)
        build  # Call build function
        ;;
    rviz)
        rviz  # Call rviz function
        ;;
    *)
        echo "Usage: $0 {install|build|rviz}"
        exit 1
        ;;
esac
