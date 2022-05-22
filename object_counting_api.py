import cv2
import numpy as np

# from utils import COLORS, intersect, get_output_fps_height_and_width


class ObjectCountingAPI:

    def __init__(self, options):
        self.options = options

    def count_objects_on_video(self, cap, targeted_classes=[], output_path="the_output.avi", show=False):
        ret, frame = cap.read()
        # fps, height, width = get_output_fps_height_and_width(cap)

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # output_movie = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while ret:
            #     objects = self.tfnet.return_predict(frame)

            #     if targeted_classes:
            #         objects = list(filter(lambda res: res["label"] in targeted_classes, objects))

            #     results, labels_quantities_dic = self._convert_detections_into_list_of_tuples_and_count_quantity_of_each_label(
            #         objects)

            #     self._draw_detection_results(frame, results, labels_quantities_dic)

            #     self._write_quantities(frame, labels_quantities_dic)

            #     output_movie.write(frame)

            if show:
                cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            ret, frame = cap.read()

        cap.release()
        cv2.destroyAllWindows()
