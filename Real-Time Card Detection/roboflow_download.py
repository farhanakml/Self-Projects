from roboflow import Roboflow
rf = Roboflow(api_key="")
project = rf.workspace("augmented-startups").project("playing-cards-ow27d")
version = project.version(4)
dataset = version.download("yolov8")