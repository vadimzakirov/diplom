from entropy_base import Entropy
import wave
import numpy as np
import matplotlib.pyplot as plt
import math

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

class MicrophoneEntropy(Entropy):

    def __init__(self):
        super(MicrophoneEntropy, self).__init__()

    def format_time(x, pos=None):
        global duration, nframes, k
        progress = int(x / float(nframes) * duration * k)
        mins, secs = divmod(progress, 60)
        hours, mins = divmod(mins, 60)
        out = "%d:%02d" % (mins, secs)
        if hours > 0:
            out = "%d:" % hours
        return out

    def format_db(x, pos=None):
        if pos == 0:
            return ""
        global peak
        if x == 0:
            return "-inf"

        db = 20 * math.log10(abs(x) / float(peak))
        return int(db)

    def make_samples(self):
        wav = wave.open("entropy_inputs/acoustic_noise.wav", mode="r")
        (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()

        duration = nframes / framerate
        w, h = 800, 300
        k = nframes / w / 32
        DPI = 72
        peak = 256 ** sampwidth / 2

        content = wav.readframes(nframes)
        samples = np.fromstring(content, dtype=types[sampwidth])

        plt.figure(1, figsize=(float(w) / DPI, float(h) / DPI), dpi=DPI)
        plt.subplots_adjust(wspace=0, hspace=0)
        normal_samples = []
        for n in range(nchannels):
            channel = samples[n::nchannels]
            channel = channel[0::100]
            if nchannels == 1:
                channel = channel - peak
            for elem in channel:
                elem += 32768
                if elem > 0:
                    self.list.append(1)
                else:
                    self.list.append(0)
                normal_samples.append(elem)
            print(f" Среднее -  {np.mean(normal_samples)}")
            self.list = normal_samples
        n, bins, patches = plt.hist(normal_samples, 10, facecolor='blue', alpha=0.5)
        plt.savefig("warm_outputs/full_elem_hist.png", dpi=DPI)


Mic = MicrophoneEntropy()
Mic.make_samples()
Mic.count()