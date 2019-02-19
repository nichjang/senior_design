cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

find_package(roscpp REQUIRED)
find_package(std_msgs REQUIRED)
include_directories(${roscpp_INCLUDE_DIRS})
include_directories(${std_msgs_INCLUDE_DIRS})

# Find Gazebo
find_package(gazebo REQUIRED)
include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")

# Build our plugin
add_library(teamH8_plugin SHARED libteamH8_plugin.cc)
target_link_libraries(teamH8_plugin ${GAZEBO_LIBRARIES} ${roscpp_LIBRARIES})

add_library(laser_plugin SHARED gazebo_ros_laser.cpp)
target_link_libraries(laser_plugin ${GAZEBO_LIBRARIES} ${roscpp_LIBRARIES})


# Build the stand-alone ltest program
add_executable(teamH8 teamH8.cc)

if (${gazebo_VERSION_MAJOR} LESS 6)
  include(FindBoost)
  find_package(Boost ${MIN_BOOST_VERSION} REQUIRED system filesystem regex)
  target_link_libraries(teamH8 ${GAZEBO_LIBRARIES} ${Boost_LIBRARIES})
else()
  target_link_libraries(teamH8 ${GAZEBO_LIBRARIES})
endif()

add_executable(laser gazebo_ros_laser.cpp)

if (${gazebo_VERSION_MAJOR} LESS 6)
  include(FindBoost)
  find_package(Boost ${MIN_BOOST_VERSION} REQUIRED system filesystem regex)
  target_link_libraries(laser ${GAZEBO_LIBRARIES} ${Boost_LIBRARIES})
else()
  target_link_libraries(laser ${GAZEBO_LIBRARIES})
endif()
