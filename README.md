# 📷 BlurMeCam  
### Real-time face blurring virtual camera for privacy on video chat platforms

**BlurMeCam** is a Python-based tool that automatically **detects and blurs your face** in real time and outputs the processed video through a **virtual webcam**.  
You can safely use it on platforms like **Meet**, **Zoom**, **Discord**, **OBS**, etc.

Perfect for preventing unwanted recordings and protecting your identity online.

---

## 🚀 Features

- 🔒 **Blurs your face before it reaches the browser/app**
- ⚡ Real-time face detection using **UniFace (RetinaFace)**
- 🎥 Outputs as a **virtual webcam**  
- ⏱️ 30+ FPS depending on hardware  
- 🎛️ Toggle blur ON/OFF with a single key (`B`)
- 🛑 Quit instantly (`Q`)
- 🧠 No face recognition or storage — **detection only**
- 💻 Works on Windows, Linux, and macOS (via OBS Virtual Camera)

---

## 📦 Requirements

- Python **3.8+**
- A working webcam  
- A virtual camera backend:
  - Windows → **OBS Virtual Camera** (recommended)
  - Linux → **v4l2loopback**
  - macOS → OBS Virtual Camera

---

# 🔧 Installation

Clone the repo:

```bash
git clone https://github.com/Sidhant-Sambyal/BlurMeCam.git
cd BlurMeCam
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🎥 Virtual Camera Setup

## 🪟 Windows (Recommended: OBS Virtual Camera)

1. Install **OBS Studio**  
   https://obsproject.com/
2. Open OBS → **Start Virtual Camera**
3. BlurMeCam will automatically use OBS as its backend

If needed, you can force the backend in code:

```python
cam = pyvirtualcam.Camera(
    width=w, height=h, fps=30, backend='obs'
)
```

---

## 🐧 Linux (v4l2loopback)

Install:

```bash
sudo apt install v4l2loopback-dkms
sudo modprobe v4l2loopback video_nr=10 card_label="BlurMeCam"
```

OBS Virtual Camera also works.

---

## 🍏 macOS

Install OBS and start **OBS Virtual Camera**.

---

# ▶️ Usage

Run BlurMeCam:

```bash
python run.py
```

A preview window opens showing your blurred face.  
A new **virtual camera device** becomes available in your system.

### Controls

| Key | Action |
|-----|--------|
| **B** | Toggle blur ON/OFF |
| **Q** | Quit the application |

---

# 📡 Using BlurMeCam in apps/websites

Open any app/site:

- Google Meet  
- Zoom  
- Discord  
- Teams  
- OBS  
- Browser webcam websites  

Then select:

> **OBS Virtual Camera** (or "BlurMeCam" depending on backend)

Your blurred video will appear instantly.

---

# 🧩 Command-line Options

Change blur strength:

```bash
python run.py --strength 31
```

Change blur intensity:

```bash
python run.py --sigma 20
```

Run without preview window:

```bash
python run.py --no-preview
```

---

# 📂 Project Structure

```
blurmecam/
├── blurmecam/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── run.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Roadmap

- GUI (PyQt/Tkinter)
- Pixelation mode
- Emoji face mask mode
- Background blur
- Custom blur area
- Multi-camera support
- One-click Windows installer (.exe)

---

# 🤝 Contributing

PRs, issues, and suggestions are welcome!  
Please follow best practices for Python code quality.

---

# 🛡️ License

MIT License — free to use, modify, and distribute.

---
