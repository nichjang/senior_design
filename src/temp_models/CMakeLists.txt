cmake_minimum_required(VERSION 2.8.3)
project(gazebo_models)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  roscpp
  std_msgs
)

find_package(gazebo REQUIRED)

link_directories(${GAZEBO_LIBRARY_DIRS})
include_directories(
  ./include
  ${std_msgs_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
  ${GAZEBO_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIR}
)

add_library(laser_plugin src/gazebo_ros_laser.cpp)
target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES} ${GAZEBO_LIBRARIES})



# Build our plugin
add_library(teamH8_plugin src/libteamH8_plugin.cc)
target_link_libraries(teamH8_plugin 
  ${GAZEBO_LIBRARIES}
  ${roscpp_LIBRARIES}
)

# Build the stand-alone ltest program
add_executable(teamH8 teamH8.cc)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES cvg_sim_gazebo
#  CATKIN_DEPENDS gazebo
  DEPENDS
    roscpp
    gazebo_ros
)
