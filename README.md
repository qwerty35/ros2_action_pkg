# gcamp_ros2_basic

## Create Package

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r __ns:=/skidbot2

ros2 launch gcamp_gazebo gcamp_world.launch.py 
#TODO : robot state publisher

ros2 run py_topic_pkg cmd_vel_pub_node 
ros2 run py_topic_pkg laser_sub_node
ros2 run py_topic_pkg parking_node

ros2 interface show custom_interfaces/srv/AddThreeInts
# "rosfoxy" required after custom msg/srv build

ros2 run py_service_pkg gazebo_model_spawner
ros2 run py_service_pkg robot_turning_server
ros2 service call /turn_robot custom_interfaces/srv/TurningControl "{time_duration: 5, angular_vel_z: 1.0, linear_vel_x: 0.5}"
ros2 run py_service_pkg robot_turning_client


ros2 pkg create --build-type ament_cmake  cpp_srvcli     --dependencies rclcpp example_interfaces
ros2 pkg create --build-type ament_cmake  custom_interfaces

ros2 pkg create --build-type ament_python py_first_pkg   --dependencies rclpy
ros2 pkg create --build-type ament_python py_topic_pkg   --dependencies rclpy sensor_msgs geometry_msgs
ros2 pkg create --build-type ament_python py_service_pkg --dependencies rclpy gazebo_msgs

ros2 interface show geometry_msgs/msg/Twist

$ ros2 pkg create my_python_pkg --build-type ament_python rclpy
$ ros2 pkg create my_cpp_py_pkg --build-type ament_cmake
```

https://answers.ros.org/question/302037/ros2-how-to-call-a-service-from-the-callback-function-of-a-subscriber/