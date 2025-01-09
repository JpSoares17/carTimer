from roboflow import Roboflow
rf = Roboflow(api_key="SJZftFOeLKsHXPTTJUBW")
project = rf.workspace("licenseplateocr").project("cartimer")
version = project.version(1)
dataset = version.download("yolov11")
                