cmake_minimum_required(VERSION 3.10)
project(hagen_robot_diff_drive)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(gazebo_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(ament_index_python REQUIRED)

install(
  DIRECTORY launch models
  DESTINATION share/${PROJECT_NAME}/
)

install(
  PROGRAMS
    scripts/spawn_robot.py
    scripts/diff_drive_control.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()