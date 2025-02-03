# Sammy-at-School
This project created for the 2025 QHacks Hackathon. It's a pov-style narrative game surrounding eco-consciousness with a camera feature that allows users to scan an object and find how long it takes to biodegrade and what recycling category it belongs in. 

I started with designing the game narrative and mechanics, focusing on the daily choices in conserving water, eco-friendly materials, and recycling sorting. I developed an interactive, narrative-driven environment with multiple outcomes based on the user's choices. To make the learning immersive for players, I integrated an object-detection system using pre-trained YOLO models, and trained a couple models of my own using RoboFlow. This system identifies real-world objects through a camera. I integrated google's Gemini to categorizes them into recyclable, compostable, or non-recyclable items and state the number of years the object takes to biodegrade to help kids understand waste management visually and practically.

This projects utilizes PyGame Zero, OpenCv, YOLO, RoboFlow, Generative AI, and MediaPipe.
