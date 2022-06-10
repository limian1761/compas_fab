"""
Create a position and an orientation constraint from a robot configuration.

COMPAS FAB v0.25.0
"""
import math

from ghpythonlib.componentbase import executingcomponent as component


class ConstraintsFromTargetConfiguration(component):

    DEFAULT_TOLERANCE_METERS = .001
    DEFAULT_TOLERANCE_RADIANS = math.radians(1)

    def RunScript(self, robot, target_configuration, tolerance_above, tolerance_below, group_name):
        if robot and target_configuration:
            tolerance_above = tolerance_above or self._generate_default_tolerances(robot.get_configurable_joints(group_name))
            tolerance_below = tolerance_below or self._generate_default_tolerances(robot.get_configurable_joints(group_name))

            constraints = robot.constraints_from_configuration(
                configuration=target_configuration,
                tolerances_above=tolerance_above,
                tolerances_below=tolerance_below,
                group=group_name
            )

            return constraints

    def _generate_default_tolerances(self, joints):
        return [
            self.DEFAULT_TOLERANCE_METERS if j.is_scalable()
            else self.DEFAULT_TOLERANCE_RADIANS
            for j in joints
        ]

