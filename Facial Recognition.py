from deepface import DeepFace
import os

#Single File
filePath = r"C:\Users\Zach Frank\PycharmProjects\DeepFace\Targets\Opera.png"
# Path for Finding in file
FindFace_path = r"C:\Users\Zach Frank\PycharmProjects\FreeTime\Targets\Opera.jpg"
# Model Used
model_name = "Facenet"

# Compare
faces = {1: r"C:\Users\Zach Frank\PycharmProjects\FreeTime\Targets\elon1.jpg",
         2: r"C:\Users\Zach Frank\PycharmProjects\FreeTime\Targets\elon2.jpg"}


class FaceFinding:
    def __init__(self, keyNum, filePath):
        self.keyNum = keyNum
        self.filePath = filePath

    def fileFind(self):
        find = DeepFace.find(img_path=FindFace_path, db_path=r"C:\Users\Zach Frank\PycharmProjects\FreeTime\Targets")
        for Line in range(len(find.index)):
            fileName = find.iloc[Line].identity.split("\\")
            print("Match found in " + fileName[-1])
            Analyze = DeepFace.analyze(img_path=[find.iloc[Line].identity],
                                       actions=('age', 'gender', 'race', 'emotion'))
            print("\n", "Age:", Analyze['instance_1']['age'], "Gender:", Analyze['instance_1']['gender'], "Race:",
                  Analyze['instance_1']['dominant_race'], "Feeling:",
                  Analyze['instance_1']['dominant_emotion'])

    def dictFace(self, keyNum):
        for _ in faces:
            Verify = DeepFace.verify(img1_path=faces[1], img2_path=faces[2], model_name=model_name)
            if Verify['verified']:
                print("The images are verified matches")
                print(Verify)
                # os.system("open " + img_1_path)
                os.system("open " + faces[keyNum])
                Analyze = DeepFace.analyze(img_path=faces[keyNum], actions=('age', 'gender', 'race', 'emotion'))
                print("Age:", Analyze['age'], "Gender:", Analyze['gender'], "Race:", Analyze['dominant_race'],
                      "Feeling:",
                      Analyze['dominant_emotion'])
            else:
                print("No Match")
                pass
            keyNum = keyNum + 1

    def singleAnalyze(self, filePath):
        Analyze = DeepFace.analyze(img_path=[filePath], actions=('age', 'gender', 'race', 'emotion'))
        print("\n", "Age:", Analyze['instance_1']['age'], "Gender:", Analyze['instance_1']['gender'], "Race:",
              Analyze['instance_1']['dominant_race'], "Feeling:",
              Analyze['instance_1']['dominant_emotion'])


# Detect = DeepFace.detectFace(img_path=img_1_path)


# dictFace(3)
# singleAnalyze("/Users/zachary/PycharmProjects/FreeTime/Targets/face5.jpg")

Faces = FaceFinding(1, filePath)
Faces.singleAnalyze(filePath)
