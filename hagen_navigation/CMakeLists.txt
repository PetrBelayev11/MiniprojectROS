cmake_minimum_required(VERSION 3.10)
project(hagen_navigation)
find_package(ament_cmake REQUIRED)
install(DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)
ament_package()