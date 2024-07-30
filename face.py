#import libs
import numpy as np
import cv2
import sys
from imutils.video import VideoStream
import operator
from PIL import Image, ImageFont, ImageDraw

import emoji
from fer import FER

def start():

    vs = VideoStream(src=0).start()
    data = []
    detector = FER(mtcnn=True)
    while True:
        frame = vs.read()
        pred = detector.detect_emotions(frame)
        print(pred)
        for i in pred:
            X, Y, w, h = i['box']
            H, W, _ = frame.shape
            X_1, X_2 = (max(0, X - int(w * 0.2)), min(X + int(1.1 * w), W))
            Y_1, Y_2 = (max(0, Y - int(0.2 * h)), min(Y + int(1.1 * h), H))
            emotion = max(i['emotions'].items(), key=operator.itemgetter(1))[0]
            #set emojis
            emoji1 = {"surprise": emoji.emojize(':worried:', use_aliases=True),
                    "happy": emoji.emojize(':smile:', use_aliases=True),
                    "sad": emoji.emojize(':cry:', use_aliases=True),
                    "fear": emoji.emojize(':scream:', use_aliases=True),
                    "angry": emoji.emojize(':angry:', use_aliases=True),
                    "neutral": emoji.emojize(':neutral_face:', use_aliases=True),
                    "disgust": emoji.emojize(':mask:', use_aliases=True)}
            emoji2 = emoji1.get(emotion)
            cv2.rectangle(
                img=frame,
                pt1=(X_1, Y_1),
                pt2=(X_2, Y_2),
                color=(0, 200, 0),
                thickness=2,
            )
            im_p = Image.fromarray(frame)
            # Get a drawing context
            draw = ImageDraw.Draw(im_p)
            font = ImageFont.truetype("./EmojiOneColor.otf", 40, encoding='unic')
            tick = emoji2
            draw.text((X_1 - 10, Y_1 - 40), emoji2, fill=(255, 150, 0), font=font)
            frame = np.array(im_p)
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    vs.stop()
    cv2.destroyAllWindows()
