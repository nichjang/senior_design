1.	All of the plugin files are located in 'laserTest/gazebo_ros_pkgs/gazebo_plugins/build/devel/lib'

2. 	Need to set the model path and plugin path for gazebo. I saw online that you can add default directories in '~/.bashrc', but I will let Ben decide where that should go. These are the exports I used on my computer:

export GAZEBO_MODEL_PATH=~/Desktop/laserTest/models
export GAZEBO_PLUGIN_PATH=~/Desktop/laserTest/gazebo_ros_pkgs/gazebo_plugins/build/devel/lib:$GAZEBO_PLUGIN_PATH

3. 	The way I tested it was to do:
	roslaunch gazebo_ros empty_world.launch

4.	To read the topic do:
	rostopic echo /teamH8/laser/scan -n1
	The -n1 allows you to just take 1 sample of it at a time so your terminal window is not crazy


5.	Tried to make a launch file, but failed

