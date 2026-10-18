"""Fabrique la bande-son de la vidéo Jokko : bruitages, coups de basse, musique, mixage.

Tous les sons sont synthétisés ici (aucun échantillon externe) : ils sont originaux et libres de droits.
Usage : python3 assets/audio/build_audio.py   (depuis videos/jokko)
"""
import json, re, subprocess
from html.parser import HTMLParser
import numpy as np
import pyloudnorm as pyln
from scipy import signal

SR = 48000
DUR = 40.5
N = int(SR * DUR)
rng = np.random.default_rng(20261018)
OUT = "assets/audio"

def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).reshape(-1, 2).astype(np.float64)

def save(path, x):
    x = np.clip(x, -1, 1)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f64le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s24le", path], input=x.astype(np.float64).tobytes(), check=True)

def t(sec):
    return np.arange(int(SR * sec)) / SR

def place(buf, x, at, gain=1.0, pan=0.0):
    i = int(at * SR)
    if i >= len(buf):
        return
    x = x[: len(buf) - i]
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    buf[i : i + len(x), 0] += x * gain * l * np.sqrt(2)
    buf[i : i + len(x), 1] += x * gain * r * np.sqrt(2)

meter = pyln.Meter(SR)
def lufs(x):
    return meter.integrated_loudness(x)

# ---------------------------------------------------------------- voix + temps des mots
voice = np.zeros((N, 2))
v = load("assets/voix.mp3")
voice[: len(v)] = v
L_voice = lufs(voice)

words = json.load(open("assets/words.json"))

class P(HTMLParser):
    """Repère pour chaque mot (data-w) s'il sort d'une fente ou monte lettre par lettre."""
    def __init__(self):
        super().__init__(); self.stack = []; self.kind = {}
    def handle_starttag(self, tag, attrs):
        a = dict(attrs); cls = a.get("class", "") or ""
        self.stack.append(cls)
        if "data-w" in a:
            slit = any("slit" in c.split() for c in self.stack)
            self.kind.setdefault(int(a["data-w"]), "slit" if slit else "letters")
    def handle_endtag(self, tag):
        if self.stack: self.stack.pop()
p = P(); p.feed(open("index.html").read())

# ---------------------------------------------------------------- bruitages
def tic(f, decay, bright):
    x = t(0.09)
    s = np.sin(2 * np.pi * f * x) + 0.45 * np.sin(2 * np.pi * f * 2.76 * x)
    s *= np.exp(-x / decay)
    click = rng.standard_normal(len(x)) * np.exp(-x / 0.0015) * bright
    return s + click

def souffle(dur, f0, f1, q):
    n = int(SR * dur)
    noise = rng.standard_normal(n)
    out = np.zeros(n); zi = None; step = int(SR * 0.005)
    for k in range(0, n, step):
        fc = f0 * (f1 / f0) ** (k / n)
        sos = signal.butter(2, [fc / q, min(fc * q, SR / 2.2)], btype="band", fs=SR, output="sos")
        if zi is None: zi = signal.sosfilt_zi(sos) * 0
        out[k : k + step], zi = signal.sosfilt(sos, noise[k : k + step], zi=zi)
    env = np.sin(np.pi * np.linspace(0, 1, n)) ** 1.6
    return out * env

TICS = [tic(2400, 0.010, 0.25), tic(3300, 0.006, 0.15), tic(1700, 0.016, 0.35),
        tic(4200, 0.005, 0.10), tic(1250, 0.020, 0.45), tic(2900, 0.008, 0.30)]
SOUFFLES = [souffle(0.16, 900, 3800, 1.6), souffle(0.22, 3200, 1100, 1.5), souffle(0.12, 1800, 6000, 1.8),
            souffle(0.26, 700, 2400, 1.4), souffle(0.18, 5000, 2000, 1.7), souffle(0.14, 1300, 4800, 1.5)]
LIB = [("tic", i, s / np.abs(s).max()) for i, s in enumerate(TICS)] + [("souffle", i, s / np.abs(s).max()) for i, s in enumerate(SOUFFLES)]

def basse():
    x = t(1.1)
    f = 42 + 58 * np.exp(-x / 0.06)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.35)
    s = np.tanh(2.2 * s) + 0.25 * rng.standard_normal(len(x)) * np.exp(-x / 0.004)
    return s / np.abs(s).max()

sfx = np.zeros((N, 2))
prev = None
log = []
for i, w in enumerate(words):
    kind = "souffle" if p.kind.get(i) == "slit" else "tic"
    cands = [e for e in LIB if e[0] == kind and (e[0], e[1]) != prev]
    name, idx, s = cands[rng.integers(len(cands))]
    prev = (name, idx)
    at = w["start"] - (0.05 if kind == "souffle" else 0.02)
    place(sfx, s, max(0, at), gain=10 ** (rng.uniform(-2, 1) / 20), pan=rng.uniform(-0.35, 0.35))
    log.append((round(at, 3), w["text"], f"{name}{idx + 1}"))

# Coups de basse sur les moments forts : Jokko, 70, 20, les trois métiers, vérifiés, FCFA, Dakar, Jokko, Jokko.
FORTS = [23, 28, 33, 35, 36, 37, 42, 48, 83, 84, 109]
bass = np.zeros((N, 2))
for i in FORTS:
    place(bass, basse(), words[i]["start"] - 0.01)

# Les bruitages (souffles, tics et basses) sont réglés ensemble à 7 dB sous la voix.
fx = sfx + bass * 1.6
fx *= 10 ** ((L_voice - 7 - lufs(fx)) / 20)

# ---------------------------------------------------------------- musique (122 BPM, originale)
BPM = 122; beat = 60 / BPM; s16 = beat / 4
music = np.zeros((N, 2))
def kick():
    x = t(0.4); f = 48 + 110 * np.exp(-x / 0.03)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x / 0.16)
def clap():
    x = t(0.25); n = rng.standard_normal(len(x))
    sos = signal.butter(2, [900, 4000], btype="band", fs=SR, output="sos")
    e = sum(np.exp(-np.clip(x - d, 0, None) / 0.01) * (x >= d) for d in (0, 0.012, 0.024)) + np.exp(-x / 0.08) * 0.5
    return signal.sosfilt(sos, n) * e
def shaker(acc):
    x = t(0.06); n = rng.standard_normal(len(x))
    sos = signal.butter(2, 6000, btype="high", fs=SR, output="sos")
    return signal.sosfilt(sos, n) * np.exp(-x / 0.018) * acc
def logdrum(f):
    x = t(0.35); ff = f * (1 + 0.5 * np.exp(-x / 0.015))
    return np.tanh(1.6 * np.sin(2 * np.pi * np.cumsum(ff) / SR) * np.exp(-x / 0.12))
def pluck(freqs):
    x = t(0.45)
    s = sum(np.sin(2 * np.pi * f * x) + 0.3 * np.sin(2 * np.pi * 2 * f * x) for f in freqs)
    return s * np.exp(-x / 0.14) * (1 - np.exp(-x / 0.003)) / len(freqs)

hz = lambda m: 440 * 2 ** ((m - 69) / 12)
CHORDS = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]   # la m – fa – do – sol
ROOTS = [45, 41, 48, 43]
K, C = kick(), clap()
nb = int(DUR / beat) + 1
for b in range(nb):
    tb = b * beat; bar = b // 4; ch = bar % 4
    if tb > DUR - 0.5: break
    intro = b < 4
    place(music, K, tb, 0.9 if not intro else 0.5)
    if b % 4 in (1, 3) and not intro: place(music, C, tb, 0.35, pan=0.1)
    for k in range(4):
        place(music, shaker(0.6 if k % 2 else 0.3), tb + k * s16, 0.25, pan=-0.3 + 0.2 * k)
    if not intro:
        for k, step in enumerate([0, 3, 6]):        # basse syncopée façon log drum
            if (b + k) % 2 == 0 or k == 0:
                place(music, logdrum(hz(ROOTS[ch] - 12 + (7 if k == 2 else 0))), tb + step * s16 / 2, 0.55)
    for k in (2, 3):                                  # accords en contretemps
        place(music, pluck([hz(m + 12) for m in CHORDS[ch]]), tb + k * s16, 0.22, pan=0.25 if k == 2 else -0.25)

# léger filtre pour arrondir, fondu d'entrée et de sortie
sos = signal.butter(2, 9000, btype="low", fs=SR, output="sos")
music = signal.sosfilt(sos, music, axis=0)
fade = np.ones(N); fi, fo = int(0.3 * SR), int(1.6 * SR)
fade[:fi] = np.linspace(0, 1, fi); fade[-fo:] = np.linspace(1, 0, fo) ** 2
music *= fade[:, None]

# Niveau de la musique hors voix : 4 dB sous la voix ; elle baisse de 12 dB quand tu parles.
music *= 10 ** ((L_voice - 4 - lufs(music)) / 20)
mono = np.abs(voice).mean(axis=1)
win = int(0.02 * SR)
env = np.sqrt(np.convolve(mono ** 2, np.ones(win) / win, mode="same"))
talking = (20 * np.log10(env + 1e-9) > -45).astype(float)
look = int(0.08 * SR)                                 # anticipe de 80 ms
talking = np.maximum(talking, np.concatenate([talking[look:], np.zeros(look)]))
duck = np.zeros(N); g = 0.0
att, rel = np.exp(-1 / (0.04 * SR)), np.exp(-1 / (0.35 * SR))
for k in range(N):
    target = talking[k]
    g = target + (g - target) * (att if target > g else rel)
    duck[k] = g
music *= (10 ** (-12 * duck / 20))[:, None]

# ---------------------------------------------------------------- mixage + mastering à -14 LUFS
def limiter(x, ceil_db=-1.5, look_ms=5, rel_ms=80):
    ceil = 10 ** (ceil_db / 20)
    peak = np.abs(x).max(axis=1)
    la = int(look_ms * SR / 1000)
    need = np.minimum(1, ceil / np.maximum(peak, 1e-9))
    need = np.minimum.accumulate(np.concatenate([need, np.ones(la)])[::-1].reshape(-1)) if False else need
    # minimum glissant sur la fenêtre d'anticipation
    from scipy.ndimage import minimum_filter1d
    need = minimum_filter1d(need, size=2 * la + 1, origin=0)
    g = np.empty_like(need); cur = 1.0; r = np.exp(-1 / (rel_ms * SR / 1000))
    for k in range(len(need)):
        cur = need[k] if need[k] < cur else need[k] + (cur - need[k]) * r
        g[k] = cur
    return x * g[:, None]

mix = voice + fx + music
gain_db = -14 - lufs(mix)
for _ in range(4):
    out = limiter(mix * 10 ** (gain_db / 20))
    err = -14 - lufs(out)
    if abs(err) < 0.05: break
    gain_db += err

save(f"{OUT}/sfx.wav", fx)
save(f"{OUT}/musique.wav", music)
save(f"{OUT}/mix.wav", out)
with open(f"{OUT}/bruitages.txt", "w") as f:
    f.write("temps(s)\tmot\tson\n" + "\n".join(f"{a}\t{b}\t{c}" for a, b, c in log))

print(f"voix          {L_voice:6.2f} LUFS")
print(f"bruitages     {lufs(fx):6.2f} LUFS  (écart {lufs(fx) - L_voice:+.1f} dB)")
print(f"musique       {lufs(music):6.2f} LUFS (avec baisse sous la voix)")
print(f"mix final     {lufs(out):6.2f} LUFS")
