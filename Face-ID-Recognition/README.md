## Building a Facial Identity Recognition System

Here we will build an application that can recognize if two faces belong to the same person, based on optical pictures (i.e. regular images, not infrared images) of their face.

To build this application we will leverage the below models.
* OWL-ViT : Zero-shot object detection is supported by the OWL-ViT model which uses a different approach. OWL-ViT is an open-vocabulary object detector. It means that it can detect objects in images based on free-text queries without the need to fine-tune the model on labeled datasets.
* Clip-ViT-L-14: This is the Image & Text model CLIP, which maps text and images to a shared vector space. 

Here, we will use the first model to detect the face in the image and use the second model to compare the faces.

We will create a Gradio app and deploy it in HuggingFace to try out with practical examples.

### References
* https://huggingface.co/docs/transformers/main/en/tasks/zero_shot_object_detection
* https://huggingface.co/sentence-transformers/clip-ViT-L-14
