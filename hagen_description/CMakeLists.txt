cmake_minimum_required(VERSION 3.5)
project(hagen_description)
find_package(ament_cmake REQUIRED)
install(DIRECTORY urdf worlds
  DESTINATION share/${PROJECT_NAME}
)
ament_package()