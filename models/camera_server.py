import cv2

'''
This server:
    Input: Camera address
    Process: Start a camera thread
    Output: Run an overridden process function for each frame
'''


class CameraServer(object):

    camera_address = None
    cam = None
    result = None
    in_progress = False

    def __init__(self, camera_address):
        self.camera_address = camera_address

    def get_status(self):
        return self.in_progress

    # Must be overridden
    def processs(self, frame):
        raise NotImplementedError

    def run(self):
        print('[Camera Server] Camera is initializing ...')
        if self.camera_address is not None:
            self.cam = cv2.VideoCapture(self.camera_address)
        else:
            print('[Camera Server] Camera is not available!')
            return

        # to save result as video
        self.result = cv2.VideoWriter('result.mp4',
                         cv2.VideoWriter_fourcc(*'MP4V'),
                         20, (608,342))
        while True:
            self.in_progress = True

            # Grab a single frame of video
            ret, frame = self.cam.read()
            if ret is True:
                self.processs(frame)
            else:
                break
        self.in_progress = False
