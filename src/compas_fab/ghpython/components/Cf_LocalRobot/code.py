"""
Load robot directly from ROS.

COMPAS FAB v1.0.2
"""

from compas.scene import SceneObject
from ghpythonlib.componentbase import executingcomponent as component
from scriptcontext import sticky as st

from compas_fab.ghpython.components import create_id

from compas_robots import RobotModel
from compas_fab.robots import Robot


class ROSRobot(component):
    def RunScript(self, file_path, load):
        key = create_id(self, "robot")

        if file_path and load:
            # Load URDF from local file path
            robot_model = RobotModel.from_urdf_file(file_path)
            st[key] = Robot(robot_model)
            st[key].scene_object = SceneObject(item = st[key].model)

        robot = st.get(key, None)
        return robot
