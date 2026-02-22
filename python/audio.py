import pyaudio
import struct
import math
import cmath
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- CONFIGURATION ---
CHUNK = 1024                 
FORMAT = pyaudio.paInt16     
CHANNELS = 1                 
RATE = 44100                 

# --- PURE PYTHON FFT ---
def recursive_fft(x):
    N = len(x)
    if N <= 1: return x
    even = recursive_fft(x[0::2])
    odd =  recursive_fft(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + \
           [even[k] - T[k] for k in range(N // 2)]

# --- SETUP AUDIO ---
p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

# --- SETUP PLOT (Star CCM+ Residuals Style) ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 6))

# History containers
history_bass = []
history_mid = []
history_high = []
frames = []

# PLOTTING LINES
# Changed linewidth to 1.0 for a "fine," professional look
line_bass, = ax.plot([], [], color='#00FFFF', linewidth=1.0, label='Bass (Low)')
line_mid,  = ax.plot([], [], color='#FF00FF', linewidth=1.0, label='Mids')
line_high, = ax.plot([], [], color='#FFFF00', linewidth=1.0, label='Highs')

# Visual Styling
ax.set_title('Frequency Residuals Monitor', fontsize=14, color='white')
ax.set_xlabel('Iterations (Frames)', fontsize=10)
ax.set_ylabel('Magnitude (Log)', fontsize=10)
ax.legend(loc='upper right', fontsize=8)

# Grid: Very subtle, like engineering software
ax.grid(True, which='both', linestyle=':', linewidth=0.5, alpha=0.4)

# Initial Views
ax.set_ylim(0, 90)
ax.set_xlim(0, 200)

# --- ANIMATION LOOP ---
def update(frame):
    try:
        # 1. Read & Unpack
        raw_data = stream.read(CHUNK, exception_on_overflow=False)
        data_ints = struct.unpack(str(CHUNK) + 'h', raw_data)
        
        # 2. FFT
        fft_complex = recursive_fft(data_ints)
        
        # 3. Frequency Bands
        fft_bass = fft_complex[0:10]    # ~0 - 400Hz
        fft_mid  = fft_complex[10:50]   # ~400 - 2000Hz
        fft_high = fft_complex[50:200]  # ~2k - 8kHz
        
        # 4. Average & Log Scale
        def get_val(data):
            if not data: return 0
            avg = sum(abs(x) for x in data) / len(data)
            return math.log10(avg + 1) * 20
            
        val_bass = get_val(fft_bass)
        val_mid  = get_val(fft_mid)
        val_high = get_val(fft_high)
        
        # 5. Append History
        frames.append(frame)
        history_bass.append(val_bass)
        history_mid.append(val_mid)
        history_high.append(val_high)
        
        # 6. Update Lines
        line_bass.set_data(frames, history_bass)
        line_mid.set_data(frames, history_mid)
        line_high.set_data(frames, history_high)
        
        # 7. Auto-Scroll (Residuals Effect)
        # Keeps the leading edge in view, expanding the X-axis
        current_max_x = ax.get_xlim()[1]
        if frame > current_max_x * 0.95:
            ax.set_xlim(0, current_max_x + 100)
            
    except Exception as e:
        print(f"Error: {e}")
    
    return line_bass, line_mid, line_high

# Blit=False allows the axis to expand automatically
ani = FuncAnimation(fig, update, interval=0, blit=False)

plt.show()

# Cleanup
stream.stop_stream()
stream.close()
p.terminate()