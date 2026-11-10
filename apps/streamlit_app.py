"""Optional educational UI: run `streamlit run apps/streamlit_app.py`."""

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from seismic_toolkit.pipeline import run_synthetic_demo

st.set_page_config(page_title="Seismic Toolkit Demo", layout="wide")
st.title("Synthetic seismic monitoring • educational demo")
st.caption("Synthetic data only. Not validated for reservoir or operational decisions.")

dt_ms = st.sidebar.select_slider("Sampling interval (ms)", options=[0.5, 1.0, 2.0], value=1.0)
delay = st.sidebar.slider("Monitor delay (samples)", 0, 12, 4)
result = run_synthetic_demo(dt=dt_ms / 1000, delay_samples=delay)

col1, col2 = st.columns(2)
col1.metric("True shift (ms)", f"{1000 * result['true_delay_s']:.2f}")
col2.metric("Estimated shift (ms)", f"{1000 * result['estimated_delay_s']:.2f}")

x = np.arange(len(result["baseline"])) * float(result["dt"]) * 1000
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, result["baseline"], label="Baseline", lw=1)
ax.plot(x, result["monitor"], label="Monitor", lw=1, alpha=0.8)
ax.set(xlabel="Time (ms)", ylabel="Amplitude", title="Synthetic baseline and monitor")
ax.legend()
ax.grid(alpha=0.25)
st.pyplot(fig)
plt.close(fig)
