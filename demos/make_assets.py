"""Regenerate the demo figure and audio: python demos/make_assets.py."""
from pathlib import Path
import math
import struct
import wave

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

assets = Path(__file__).resolve().parents[1] / "assets"
t = [i / 1000 for i in range(1001)]
y = [math.exp(-4 * x) * math.sin(2 * math.pi * 8 * x) for x in t]
fig, ax = plt.subplots(figsize=(9, 4), layout="constrained")
ax.plot(t, y, color="#2d9f84", linewidth=2.5)
ax.set(xlabel="Time (s)", ylabel="Amplitude", xlim=(0, 1), ylim=(-1, 1))
ax.spines[["top", "right"]].set_visible(False)
ax.grid(alpha=0.2)
fig.savefig(assets / "damped-sine.svg", transparent=True)
plt.close(fig)

rate = 24000
samples = [int(6000 * math.sin(2 * math.pi * 440 * i / rate)
               * min(1, i / 240, (2 * rate - 1 - i) / 240))
           for i in range(2 * rate)]
with wave.open(str(assets / "tone.wav"), "wb") as audio:
    audio.setparams((1, 2, rate, 0, "NONE", "not compressed"))
    audio.writeframes(struct.pack(f"<{len(samples)}h", *samples))

assert len(t) == len(y) == 1001 and max(map(abs, y)) <= 1
with wave.open(str(assets / "tone.wav"), "rb") as audio:
    assert audio.getnframes() == 2 * rate and audio.getnchannels() == 1
assert (assets / "damped-sine.svg").stat().st_size > 0
