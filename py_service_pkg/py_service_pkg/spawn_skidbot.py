# https://discourse.ros.org/t/spawning-a-robot-entity-using-a-node-with-gazebo-and-ros-2/9985

#!/usr/bin/env/ python3

import os
import sys
import rclpy

from rclpy.node import Node
from ament_index_python.packages import get_package_share_directory

from gazebo_msgs.srv import SpawnEntity


class SpawnRobot(Node):
    def __init__(self):
        super().__init__("gazebo_model_spawner")
        self.client = self.create_client(SpawnEntity, "/spawn_entity")

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().error("service not available, waiting again...")

        # Get urdf path
        self.urdf_file_path = os.path.join(
            get_package_share_directory("gcamp_gazebo"),
            "urdf",
            "skidbot.urdf",
        )

        self.req = SpawnEntity.Request()

    def send_req(self):
        self.req.name = "skidbot"
        self.req.xml = open(self.urdf_file_path, "r").read()
        self.req.robot_namespace = "skidbot"
        self.req.initial_pose.position.x = 1.0
        self.req.initial_pose.position.y = 0.0
        self.req.initial_pose.position.z = 0.3

        print("==== Sending service request to `/spawn_entity` ====")
        self.future = self.client.call_async(self.req)

        return self.future


def main(args=None):

    rclpy.init(args=args)

    robot_spawn_node = SpawnRobot()
    future = robot_spawn_node.send_req()

    rclpy.spin_until_future_complete(robot_spawn_node, future)

    if future.done():
        try:
            response = future.result()
        except Exception as e:
            raise RuntimeError(
                "exception while calling service: %r" % future.exception()
            )
        else:
            print("==== Service Call Done ====")
            print(f"Status_message : {response.status_message}")
        finally:
            robot_spawn_node.get_logger().warn("==== Shutting down node. ====")
            robot_spawn_node.destroy_node()
            rclpy.shutdown()


if __name__ == "__main__":
    main()
