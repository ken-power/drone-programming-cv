from drone_test.drone import Drone

import cv2


class DroneController:

    def __init__(self):
        self.drone = Drone("Unit Test Drone 1")

    def takeoff_move_land(self):

        print(f'Drone \'{self.drone.name()}\' is performing a manoeuvre')

        while True:
            # GET THE IMAGE FROM TELLO
            img = self.drone.read_image()

            # TO GO UP IN THE BEGINNING
            self.drone.takeoff_move_land()

            # # SEND VELOCITY VALUES TO TELLO
            self.drone.adjust_velocity()

            # DISPLAY IMAGE
            self.drone.display_image(img)

            # WAIT FOR THE 'Q' BUTTON TO STOP
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.drone.land()
                break

