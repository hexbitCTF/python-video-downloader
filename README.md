# 🎥 Universal Video Downloader  

A simple yet powerful Python script that lets you download videos from **YouTube and other supported platforms** using yt-dlp.  
You can specify the **resolution** (e.g., 720p, 1080p, or max) and the **output folder** for your downloads.  

---

## ✨ Features  
- 📥 Download videos from multiple platforms (via yt-dlp)  
- 📺 Choose resolution: 720p, 1080p, or max (best available)  
- 💾 Automatically creates a download folder  
- 🛡️ Safe filenames (no special characters)  
- 🔄 Fallback support (saves using video ID if title fails)  

---

## 🛠️ Installation  

1. Clone this repository:  
   git clone https://github.com/yourusername/universal-video-downloader.git  
   cd universal-video-downloader  

2. Install dependencies:  
   pip install yt-dlp  

---

## 🚀 Usage  

Run the script from the terminal with:  

python downloader.py -u "VIDEO_URL" [-r RESOLUTION] [-o OUTPUT_FOLDER]  

### 🔹 Arguments:  
- -u, --url → Video URL (required)  
- -r, --resolution → Resolution (default: max)  
- -o, --output → Output folder (default: downloads)  

---

## 📌 Examples  

1. Download video in **best quality available**:  
   python downloader.py -u "https://www.youtube.com/watch?v=abc123"  

2. Download video in **720p**:  
   python downloader.py -u "https://www.youtube.com/watch?v=abc123" -r 720p  

3. Download video into a custom folder:  
   python downloader.py -u "https://www.youtube.com/watch?v=abc123" -o "my_videos"  

---

## 📂 Output  
Your videos will be saved as:  

downloads/  
 └── Video_Title.mp4  

(or Video_ID.mp4 if the title fails)  

---

## ⚡ Notes  
- This tool relies on yt-dlp, which supports hundreds of sites beyond YouTube.  
- Make sure you have Python 3.7+ installed.  
- Use responsibly and respect copyright laws.  

---

## 🤝 Contributing  
Feel free to fork this repo and submit pull requests with improvements 🚀  

---

## 📜 License  
This project is licensed under the MIT License.  
