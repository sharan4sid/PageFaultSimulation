# OS_Project
Efficient Page Replacement Algorithm Simulator

A visual simulator for comparing the performance of FIFO, LRU, and Optimal page replacement algorithms used in operating systems memory management.

Overview

This project provides both a web-based and desktop interface for simulating page replacement algorithms. Users can input a reference string and frame count to visualize how different page replacement strategies perform under the same conditions.

Features:
- Simulate First-In-First-Out (FIFO), Least Recently Used (LRU), and Optimal (OPT) algorithms
- Visual comparison of page fault counts
- Interactive chart generation
- Detailed algorithm explanations
- Modern, responsive UI

Getting Started

Prerequisites
- Python 3.7 or higher
- Web browser (for web interface)

Installation

1. Clone the repository
bash
git clone https://github.com/username/page-replacement-simulator.git
cd page-replacement-simulator


2. Install required Python packages
bash
pip install -r requirements.txt


Running the Web Interface

1. Start the Flask server:
bash
python server.py

2. Open your web browser and navigate to:
http://localhost:5001

Running the Desktop Interface
For a standalone desktop application:
bash
python gui.py


Usage

1. Enter a reference string as space-separated integers (e.g., `7 0 1 2 0 3 0 4`)
2. Set the number of frames (memory capacity)
3. Click "Run Simulation"
4. View the results showing page fault counts and comparative performance

Project Structure
page-replacement-simulator/
├── static/
│   ├── app.js        # Frontend JavaScript
│   └── fn.css        # Styling
│   └── fn.html       # Web interface
├── page_replacement.py  # Algorithm implementations
├── visualization.py     # Chart generation
├── server.py            # Flask web server
├── gui.py               # Tkinter desktop interface
├── opt.py               # Optimal algorithm implementation
└── requirements.txt     # Python dependencies

Algorithms Explained
First In First Out (FIFO)
- Replaces the page that has been in memory the longest
- Simplest to implement, but often not optimal
- Uses a queue data structure
Least Recently Used (LRU)
- Replaces the page that hasn't been accessed for the longest time
- Better performance than FIFO in most cases
- Requires tracking of page access times
Optimal (OPT)
- Replaces the page that won't be used for the longest time in the future
- Provides a theoretical benchmark (lowest possible page faults)
- Not implementable in real systems as it requires future knowledge
Performance Considerations

- FIFO: Simple but can suffer from Belady's anomaly
- LRU: Better approximation of optimal but requires more overhead
- OPT: Theoretical best-case scenario, used for benchmarking

Technical Details

- Backend: Python with Flask
- Data Visualization: Matplotlib
- Frontend: HTML, CSS, JavaScript
- Desktop GUI: Tkinter

Acknowledgments

- Inspired by operating systems coursework
- UI design influenced by modern web interfaces
- Thanks to all contributors and testers
