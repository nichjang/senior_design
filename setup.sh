# This script sets up the build environment.
PROJECT_DIR_SRC=`pwd -P`/src

# Set-up githooks.
# git config core.hooksPath .githooks

# Initialize and update submodules.
git submodule update --init --recursive

# Create a catkin workspace.
mkdir ~/catkin_ws

# Install ROS.
if [[ "$OSTYPE" == "linux-gnu" ]]; then
  # From http://wiki.ros.org/kinetic/Installation/Ubuntu
  sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

  sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

  sudo apt-get update

  # Desktop-Full Install: (Recommended) : ROS, rqt, rviz, robot-generic
  # libraries, 2D/3D simulators, navigation and 2D/3D perception
  sudo apt-get -y install ros-kinetic-desktop-full

  # In order to use rosdep, we have to initialize it.
  sudo rosdep init
  rosdep update

  # Up to now you have installed what you need to run the core ROS packages. To
  # create and manage your own ROS workspaces, there are various tools and
  # requirements that are distributed separately. For example, rosinstall is a
  # frequently used command-line tool that enables you to easily download many
  # source trees for ROS packages with one command.

  # Install hector quadrotor suite.
  sudo apt-get -y install ros-kinetic-hector-*

  # Install ardrone_autonomy.
  sudo apt-get -y install ros-kinetic-ardrone-autonomy freeglut3-dev liblapack-dev libopenblas-dev

  # Link this project to your catkin workspace.
  ln -s $PROJECT_DIR_SRC ~/catkin_ws/src

  # Install TI mmWave dependencies.
  sudo apt-get -y install ros-kinetic-tf2-sensor-msgs ros-kinetic-tf2-bullet

  # Install other dependencies.
  sudo apt-get -y install ros-kinetic-control*
  sudo apt-get -y install ros-kinetic-transmission*
  sudo apt-get -y install ros-kinetic-joint*

  # Needed for TI mmWave Driver
  sudo adduser $USER dialout

  # Build catkin workspace.
  source /opt/ros/kinetic/setup.bash
  cd ~/catkin_ws
  catkin_make

  # Setup catkin
  echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
  echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
  source ~/.bashrc
else
  echo "OS not supported"
fi
exit 0
