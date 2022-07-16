from djitellopy import Tello
import cv2
import time

import drone_test.constants as constants


class Drone:

    def __init__(self, name):
        self.drone = Tello()
        self.drone_name = name

    def connect(self):
        # CONNECT TO TELLO
        print(f"Connecting to drone '{self.drone_name}'")
        self.drone.connect()
        self.drone.for_back_velocity = 0
        self.drone.left_right_velocity = 0
        self.drone.up_down_velocity = 0
        self.drone.yaw_velocity = 0
        self.drone.speed = 0
        self.drone.streamoff()
        self.drone.streamon()

        print(f'Battery {self.drone.get_battery()}')

    def takeoff_move_land(self):
        if constants.start_counter == 0:
            self.drone.takeoff()
            time.sleep(8)

            self.drone.rotate_clockwise(90)
            time.sleep(3)

            self.drone.move_left(35)
            time.sleep(3)

            self.drone.land()
            constants.start_counter = 1

    def read_image(self):
        frame_read = self.drone.get_frame_read()
        drone_image_frame = frame_read.frame
        img = cv2.resize(drone_image_frame,
                         (constants.width, constants.height))
        return img

    def adjust_velocity(self):
        if self.drone.send_rc_control:
            self.drone.send_rc_control(self.drone.left_right_velocity,
                                       self.drone.for_back_velocity,
                                       self.drone.up_down_velocity,
                                       self.drone.yaw_velocity)

    def display_image(self, img):
        cv2.imshow("MyResult", img)

    def name(self):
        return self.drone_name

    def is_in_flight(self):
        if constants.start_counter == 0:
            return True
        if constants.start_counter == 1:
            return False
