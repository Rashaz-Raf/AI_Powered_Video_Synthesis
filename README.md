# DYNAMIC NARRATIVES: CONTENT CREATION WITH AUTOMATED TEXT-TO-VIDEO GENERATION
An innovative approach to automated content creation, seamlessly transforming textual input into dynamic video narratives. By leveraging advanced technologies such as natural language processing (NLP), text-to-speech conversion, video synthesis, and image manipulation, this project enables the efficient creation of promotional videos, educational materials, and other multimedia content directly from text.

## Authors
- [@Rashaz Rafeeque](https://github.com/Rashaz-Raf)
- [@Jeevan A J](https://github.com/Jee-371)
- [@Rhishitha](https://github.com/rishi7736)


## Abstract
The **Object Recognition and Verbalization Tool** addresses the need for engaging and adaptive educational methods for young learners. Leveraging deep learning and natural language processing (NLP), this tool integrates **YOLO** for object detection and **Google Text-to-Speech (gTTS)** for audio output. The system encourages children to explore their surroundings, enabling seamless learning through visual recognition and verbal feedback. Unlike game-based approaches, this tool prioritizes real-world engagement, supporting cognitive development through interactive learning.

## System Overview
The project employs **YOLOv8**, a state-of-the-art object detection model trained on the COCO dataset, to scan and identify objects. The identified objects are then articulated through audio feedback using Python's `speech_recognition` and `gTTS` libraries, creating an interactive, voice-controlled experience. This approach promotes visual and auditory learning, helping children associate names with objects in real-time.

<img src="https://github.com/Dipin-Raj/Object-Recognition-Verbalization-Tool-for-Early-Childhood-Education/blob/main/Images/Flowcharts/Screenshot%202024-11-14%20005240.png" style="transform: rotate(90deg); width: 50%;"/>

## Methodology
1. **Voice Command Recognition**: The system activates through specific voice prompts like "What is this?" using a microphone and Python's `speech_recognition` library.
2. **Real-time Object Detection**: Initiated through OpenCV, the video stream captures and processes images in real-time using **YOLOv8** for object recognition.
3. **Speech Feedback**: Identified objects are described with **gTTS**, providing clear verbal feedback like "I see a cat and a book."
4. **Interactive Learning Loop**: The detected objects are highlighted with bounding boxes and labeled, delivering visual and auditory information that enhances learning.

### Methodology Flowchart
<img src="https://github.com/Dipin-Raj/Object-Recognition-Verbalization-Tool-for-Early-Childhood-Education/blob/main/Images/Flowcharts/Flowchart%20.jpg" alt="Methodology Flowchart" style="width: 50%;"/>

## Results
The tool demonstrated reliable real-time detection and audio feedback during tests, accurately identifying objects such as books, toys, and household items. The system maintained an average confidence score above 0.80, ensuring dependable recognition. Processing times ranged from **81.5ms to 145.4ms**, providing quick responses suited for child interaction.

### Sample Performance Metrics:
| Object      | Preprocess Time | Inference Time | Confidence |
|-------------|-----------------|----------------|------------|
| Apple       | 4.9ms           | 100.7ms        | 0.89       |
| Car         | 4.0ms           | 96.1ms         | 0.96       |
| Teddy Bear  | 3.0ms           | 94.6ms         | 0.89       |

### Results 1
<img src="https://github.com/Dipin-Raj/Object-Recognition-Verbalization-Tool-for-Early-Childhood-Education/blob/main/Images/Results/Screenshot%202024-11-13%20224200.png" alt="Results 1" style="width: 50%;"/>

### Results 2
<img src="https://github.com/Dipin-Raj/Object-Recognition-Verbalization-Tool-for-Early-Childhood-Education/blob/main/Images/Results/Screenshot%202024-11-13%20224219.png" alt="Results 2" style="width: 50%;"/>

## Conclusion
This tool bridges early childhood education and AI, offering personalized and interactive learning experiences. It presents a breakthrough approach by aligning object recognition with auditory responses, making learning intuitive and engaging. Future work will focus on expanding object libraries, refining voice interaction, and integrating IoT elements for broader functionality.

## Code
The full codebase for the **Object Recognition and Verbalization Tool for Early Childhood Education** is available [here](https://github.com/Dipin-Raj/Object-Recognition-Verbalization-Tool-for-Early-Childhood-Education/blob/main/Source%20Code/Object%20Recognition%20and%20Verbalization%20Tool%20for%20Early%20Childhood%20Educatio_Yolo_Final_Code.py).

## Documentation
Refer to the complete project documentation for detailed insights into the methodology, implementation, and results.

### Project Report Documentation
[Project Report Final PDF](https://github.com/Dipin-Raj/Object-Recognition-Verbalization-Tool-for-Early-Childhood-Education/blob/main/Documents/Project_Report_Final.pdf)
