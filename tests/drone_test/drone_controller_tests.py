import unittest

from drone_test.drone_controller import DroneController


class DroneControllerTests(unittest.TestCase):
    """
    Test cases for the drone controller
    """

    def setUp(self) -> None:
        print("Controller Tests")

    def test_controller(self):
        controller = DroneController()
        self.assertFalse(controller.drone.is_in_flight(), "Drone should start out on the ground")

        controller.takeoff_move_land()
        self.assertTrue(controller.drone.is_in_flight(), "Drone should be in the air now")


if __name__ == '__main__':
    unittest.main()
