---
step: 0
date: "9/27/2025 · Step 00"
title: "Not Boiling the Ocean"
tag: "base/"
image: "timeline/step-0.svg"
summary: "My goal was to turn my PiCar-X into an autonomous system whose, perception, work representation, planning, and control are modules I can explain and debug myself"
---


<figure class="wrap-right">
  <img src="/classical-autonomy-stack/timeline/step-1.svg" alt="Vehicle interface sketch">
  <figcaption>The three-verb Vehicle contract.</figcaption>
</figure>

This was my first real hands-on experience with a robot in a very long time so please bear with me as I enthusiastically share potentially basic concepts. 

I had previosly tried creating an autonomy stack for a drone inside of gazebo few months ago which ended up dead. Poor goal setting sling-shot me down a rabbit hole of never ending learning and setup nonesense until it became one of those "half finished projects" people are always talking about. 

**I learned a ton, what was a bit disappointing was not to having a finished project.** 

Therefore to make this new project enjoyable and feasible, I decided to write some clear goals. 

**Learning Goals**

- Coordinate frames and transforms 
- Camera calibration and geometry
- Odemetry and state estimation
- Sensor noise and uncertainty
- Occupancy/free-space representations
- A*, RRT, path following
- Feedback control and failure isolation

You might be wondering how I came up with such a clear set of learning goals? 
Thankfully this time I already had a good idea of what I wanted to build so all I did was work backwards from my a good begineer project to find the skills I needed. 

In the past, a mentor or teacher would give you a small project using their vast knowldge on a specific subject. Today we have ChatGPT so I used that.

**Project Goal**


> "Build a small autonomous car that can stay within lanes created out of electrical tape and avoid parked vehicles while it makes its way to its destination using computer vision.

Very simple.

Its called ChatGPT. I told it what I wanted to be able to do and it gave me a list of 

So now that my learning goals were set and I new what steps to take to create my own autonomy stack, I needed to determine what robot would be best such that I wouldn't be having to deal with complicated hardware. 

PiCar-X per their website is 

> an AI-driven self-driving robot car for the Raspberry Pi platform, upon which the Raspberry Pi acts as the control center. 
> The PiCar-X’s 2-axis camera module, ultrasonic module, and line tracking modules can provide the functions of color/face/traffic-signs detection, automatic obstacle avoidance, automatic line tracking, etc. 

Perfect!

Here is my little road map:

1. **Build your own hardware abstraction layer**
    - Create a vehicle interface for steering, velocity, camera, range sensing, and stop behavior so autonomy code never talks directly with PiCar-X SDK. 
2. **Calibrate and model the robot**
    - Measure steering response, turning radius, camera intrinsics/extrinsics, velocity versus command, and stopping distance. Plot commanded versus measured behavior. 
3. **Create a world representation**
    - Detect road boundaries and obstacles, but output an intermediate free-space or local map rather than steering directly from pixels. 
4. **Plan, control, and quantify performance**
    - 


