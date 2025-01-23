### README.md

# 🔒 Face Detection Auto-Lock Script  

This Python script utilizes OpenCV to detect faces using your webcam and automatically locks your PC when no face is detected. It periodically captures and analyzes webcam images every 5 seconds, ensuring that the PC remains secure when the user is not present.

---

## 📋 Features

- **Real-Time Face Detection**: Uses OpenCV's Haar cascades to detect faces, eyes, and profiles.  
- **Automatic Lock**: Locks the workstation (`LockWorkStation`) if no face is detected.  
- **Efficient Monitoring**: Runs checks in a loop with minimal resource usage.  

---

## 🛠️ Requirements  

1. **Python 3.x**  
2. **OpenCV Library**  
   Install via pip:  
   ```bash
   pip install opencv-python
   ```
3. **Windows OS** (Required for `LockWorkStation` functionality)  

---

## 📂 File Requirements  

Ensure the following Haar cascade XML files are available in the same directory:  

- `frontalface.xml`  
- `eye_glasses.xml`  
- `haarcascade_frontalface_default.xml`  
- `profile.xml`  

You can download these files from OpenCV's [GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

---

## 🚀 Usage

1. Clone the repository and navigate to the directory.  
2. Run the script:  
   ```bash
   python face_detect_and_lock.py
   ```
3. The script will:  
   - Continuously monitor for faces every 5 seconds.  
   - Lock the workstation if no face is detected.  

---

## ⚙️ How It Works  

1. **Image Capture**: Captures an image using the webcam.  
2. **Face Analysis**: Analyzes the image using multiple Haar cascades to detect:  
   - Frontal faces  
   - Eyes  
   - Profile faces  
3. **Lock Condition**:  
   - If no face is detected, the script calls the `LockWorkStation` function to lock the PC.  
   - If a face is detected, the PC remains active.  
4. **Continuous Monitoring**: The process repeats every 5 seconds to ensure the system's security.

---

## 🔑 Important Notes  

- **Windows-Only Script**: The script relies on the `LockWorkStation` function, available only on Windows systems.  
- **Privacy Caution**: The webcam will capture images continuously during the script's execution. Ensure privacy considerations are addressed.  

---

## 🤖 Contributions  

Contributions are welcome! Feel free to fork this repository and submit a pull request.  

---

**Developed with ❤️ and Python** 🐍  

---

Let me know if you'd like me to include or modify anything! 
