from facenet_pytorch import MTCNN
from matplotlib import pyplot as plt
from PIL import Image
from numpy import asarray
import cv2
import numpy as np

# extract a single face from a given photograph
def extract_face(file_path, required_size=(224, 224)):
	# create the detector, using default weights
	mtcnn = MTCNN(select_largest=False, device='cuda:0', post_process=False)
	# load image from file
	frame = cv2.imread(file_path)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame = Image.fromarray(frame)

	# Detect face
	mtcnn(frame, save_path=file_path)
	boxes, probs, landmarks = mtcnn.detect(frame, landmarks=True)


	# Visualize
	fig, ax = plt.subplots(figsize=(16, 12))
	ax.imshow(frame)
	ax.axis('off')

	for box, landmark in zip(boxes, landmarks):
		ax.scatter(*np.meshgrid(box[[0, 2]], box[[1, 3]]))
		ax.scatter(landmark[:, 0], landmark[:, 1], s=8)
	fig.show()