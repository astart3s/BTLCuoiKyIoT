from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2

def mainFuct(countObject):
    classes = ["aeroplane", "background", "bicycle", "bird", "boat",
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
               "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
               "sofa", "train", "tvmonitor"]

    colors= np.random.uniform(0, 255, size=(len(classes), 3))

    print("[INFO] loading model...")
    net = cv2.dnn.readNetFromCaffe("config.txt", "model.caffemodel")

    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    # warm up the camera
    time.sleep(1.5)

    frameCount = 0
    while True:
        for i in range(3):
            countObject[i] = 0
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        print(frame.shape)
        (h, w) = frame.shape[:2]
        resized_image = cv2.resize(frame, (300, 300))

        blob = cv2.dnn.blobFromImage(resized_image, (1 / 127.5), (300, 300), 127.5, swapRB=True)

        net.setInput(blob)
        predictions = net.forward()

        # loop over the predictions
        for i in np.arange(0, predictions.shape[2]):
            confidence = predictions[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(predictions[0, 0, i, 1])
                if classes[idx] == "bottle":
                    countObject[0] += 1
                if classes[idx] == "chair":
                    countObject[1] += 1
                if classes[idx] == "tvmonitor":
                    countObject[2] += 1
                box = predictions[0, 0, i, 3:7] * np.array([w, h, w, h])

                (startX, startY, endX, endY) = box.astype("int")
                # Get the label with the confidence score
                label = "{}: {:.2f}%".format(classes[idx], confidence * 100)
                print("Object detected: ", label)
                cv2.rectangle(frame, (startX, startY), (endX, endY),
                              colors[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[idx], 2)

        # show the output frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        frameCount += 1
        if frameCount > 30:
            break

    cv2.destroyAllWindows()
    vs.stop()
