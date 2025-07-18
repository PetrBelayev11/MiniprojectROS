cmake_minimum_required(VERSION 3.5)
project(hagen_control)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)

install(PROGRAMS
  scripts/move_to_goal.py
  scripts/move_to_goal_robot2.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()