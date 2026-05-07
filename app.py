import streamlit as st

st.set_page_config(
    page_title="AIFLA Learning Lab",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;800&family=JetBrains+Mono:wght@400;600&display=swap');

/* ── GLOBAL FONT & BASE ── */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    color: #e2e8f0 !important;
}
code, pre, .stCode {
    font-family: 'JetBrains Mono', monospace !important;
}

/* ── BACKGROUNDS ── */
.stApp { background-color: #080c14; }
section[data-testid="stSidebar"] {
    background-color: #0d1220 !important;
    border-right: 1px solid #1e2d45;
}
/* Force sidebar inner content background */
section[data-testid="stSidebar"] > div {
    background-color: #0d1220 !important;
}

/* ── HIDE STREAMLIT CHROME ── */
#MainMenu, footer { visibility: hidden; }
/* Keep header visible so the sidebar toggle button works */
header { visibility: visible !important; }
header * { visibility: visible !important; }
/* But hide the inner deploy/share buttons we don't want */
[data-testid="stToolbar"] { visibility: hidden !important; }

/* ── SIDEBAR TOGGLE BUTTON — always visible ── */
/* Collapsed state: the arrow tab on the left edge */
[data-testid="collapsedControl"] {
    visibility: visible !important;
    display: flex !important;
    background-color: #0ea5e9 !important;
    border-radius: 0 10px 10px 0 !important;
    width: 28px !important;
    min-height: 48px !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 3px 0 12px rgba(0,212,255,0.3) !important;
    z-index: 9999 !important;
    position: fixed !important;
    top: 50% !important;
    left: 0 !important;
    transform: translateY(-50%) !important;
    cursor: pointer !important;
}
[data-testid="collapsedControl"] svg,
[data-testid="collapsedControl"] * {
    fill: #ffffff !important;
    color: #ffffff !important;
    visibility: visible !important;
}
[data-testid="collapsedControl"]:hover {
    background-color: #0284c7 !important;
    width: 32px !important;
}
/* Open state: collapse arrow inside sidebar */
[data-testid="baseButton-headerNoPadding"] {
    visibility: visible !important;
    color: #e2e8f0 !important;
    background: #1e2d45 !important;
    border-radius: 6px !important;
    padding: 4px !important;
}
[data-testid="baseButton-headerNoPadding"]:hover {
    background: #0ea5e9 !important;
}
[data-testid="baseButton-headerNoPadding"] svg {
    fill: #e2e8f0 !important;
    visibility: visible !important;
}

/* ── SIDEBAR TEXT — force all text bright ── */
section[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}
/* Radio button labels */
section[data-testid="stSidebar"] .stRadio label,
section[data-testid="stSidebar"] .stRadio span,
section[data-testid="stSidebar"] .stRadio p {
    color: #e2e8f0 !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
}
/* Selected radio option highlight */
section[data-testid="stSidebar"] .stRadio [data-checked="true"] span,
section[data-testid="stSidebar"] .stRadio [aria-checked="true"] span {
    color: #00d4ff !important;
    font-weight: 700 !important;
}

/* ── MAIN CONTENT TEXT ── */
.stApp p, .stApp span, .stApp div,
.stApp label, .stApp li {
    color: #e2e8f0;
}
h1, h2, h3, h4, h5, h6 { color: #f1f5f9 !important; }

/* ── METRIC WIDGET — fix invisible label/value ── */
[data-testid="stMetric"] {
    background: #0d1220;
    border: 1px solid #1e2d45;
    border-radius: 10px;
    padding: 14px 16px;
}
[data-testid="stMetricLabel"] p,
[data-testid="stMetricLabel"] span,
[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.04em !important;
}
[data-testid="stMetricValue"],
[data-testid="stMetricValue"] *  {
    color: #00d4ff !important;
    font-size: 1.8rem !important;
    font-weight: 800 !important;
}

/* ── SELECTBOX ── */
.stSelectbox label, .stSelectbox p { color: #e2e8f0 !important; }
.stSelectbox > div > div {
    background: #0d1220 !important;
    border-color: #1e2d45 !important;
    color: #e2e8f0 !important;
}
.stSelectbox > div > div > div { color: #e2e8f0 !important; }

/* ── SLIDER ── */
.stSlider label, .stSlider p { color: #e2e8f0 !important; }
.stSlider [data-testid="stTickBarMin"],
.stSlider [data-testid="stTickBarMax"] { color: #64748b !important; }

/* ── CHECKBOX ── */
.stCheckbox label, .stCheckbox span, .stCheckbox p { color: #e2e8f0 !important; }

/* ── MULTISELECT ── */
.stMultiSelect label, .stMultiSelect p { color: #e2e8f0 !important; }
.stMultiSelect > div > div { background: #0d1220 !important; border-color: #1e2d45 !important; }
.stMultiSelect span { color: #e2e8f0 !important; }

/* ── TEXT INPUT ── */
.stTextInput label, .stTextInput p { color: #e2e8f0 !important; }
.stTextInput input {
    background: #0d1220 !important;
    border-color: #1e2d45 !important;
    color: #e2e8f0 !important;
}

/* ── TEXT AREA ── */
.stTextArea label, .stTextArea p { color: #e2e8f0 !important; }
.stTextArea textarea {
    background: #0d1220 !important;
    border-color: #1e2d45 !important;
    color: #e2e8f0 !important;
}

/* ── DATAFRAME ── */
.stDataFrame { border-color: #1e2d45 !important; }
[data-testid="stDataFrameResizable"] { color: #e2e8f0 !important; }

/* ── BUTTONS ── */
.stButton > button {
    background: linear-gradient(135deg, #0ea5e9, #6366f1) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.85 !important; }
.stButton > button p { color: #ffffff !important; }

/* ── ALERT / INFO BOXES ── */
.stInfo, .stInfo * { color: #93c5fd !important; }
.stSuccess, .stSuccess * { color: #86efac !important; }
.stWarning, .stWarning * { color: #fcd34d !important; }
.stError, .stError * { color: #fca5a5 !important; }
.stInfo { background: #0d1a2e !important; border-color: #0ea5e955 !important; }
.stSuccess { background: #0d2e1a !important; border-color: #22c55e55 !important; }
.stWarning { background: #2e1f0d !important; border-color: #f59e0b55 !important; }
.stError { background: #2e0d0d !important; border-color: #ef444455 !important; }

/* ── CODE BLOCKS ── */
.stCodeBlock, pre, code {
    background: #0d1220 !important;
    color: #7dd3fc !important;
    border: 1px solid #1e2d45 !important;
}

/* ── CONCEPT BOX (custom HTML) ── */
.concept-box {
    background: #0d1220;
    border: 1px solid #1e2d45;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
}
.concept-box h4 { color: #00d4ff !important; margin-top: 0; }
.concept-box p { color: #cbd5e1 !important; line-height: 1.6; }

/* ── TOOL HEADER ── */
.tool-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid #1e2d45;
}
.tool-badge {
    background: linear-gradient(135deg, #0ea5e9, #6366f1);
    color: #ffffff !important;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.05em;
}

/* ── PIPELINE STEPS ── */
.pipeline { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin: 16px 0; }
.pipe-step {
    background: #0d1220;
    border: 1px solid #1e2d45;
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 0.85rem;
    color: #cbd5e1 !important;
}
.pipe-step.active {
    border-color: #00d4ff;
    color: #00d4ff !important;
    box-shadow: 0 0 12px #00d4ff22;
}
.pipe-arrow { color: #475569 !important; font-size: 1.2rem; }

/* ── SECTION HEADERS (st.markdown "####") ── */
.stMarkdown h4 { color: #e2e8f0 !important; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 20px 0 10px 0;'>
        <div style='font-size:2rem;'>🧠</div>
        <div style='font-size:1.2rem; font-weight:800; color:#e2e8f0;'>AIFLA Lab</div>
        <div style='font-size:0.75rem; color:#475569; margin-top:4px;'>AI Concept Explainers</div>
    </div>
    <hr style='border-color:#1e2d45; margin: 10px 0 16px 0;'>
    """, unsafe_allow_html=True)

    LEVELS = {
        "🟢 L1 — Neural Networks":      ("L1", "#22c55e"),
        "🔵 L2 — Data & Bias":          ("L2", "#0ea5e9"),
        "🟣 L3 — CNN Visualizer":        ("L3", "#a78bfa"),
        "🟡 L4 — Prompt Engineering":    ("L4", "#fbbf24"),
        "🟠 L5 — RAG Pipeline":          ("L5", "#f97316"),
        "🔴 L6 — Agentic Workflows":     ("L6", "#f43f5e"),
        "⚪ L7 — HTML / CSS / JS Lab":   ("L7", "#e2e8f0"),
    }

    selected = st.radio(
        "Choose a tool",
        list(LEVELS.keys()),
        label_visibility="collapsed"
    )
    level_code = LEVELS[selected][0]

    st.markdown("<hr style='border-color:#1e2d45; margin: 16px 0;'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.7rem; color:#334155; text-align:center;'>AIFLA Curriculum · All Levels</div>", unsafe_allow_html=True)

# ── TOOL ROUTER ──────────────────────────────────────────────────────────────

# ════════════════════════════════════════════════════════════
# L1 — Neural Network Playground
# ════════════════════════════════════════════════════════════
if level_code == "L1":
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use("Agg")

    st.markdown("""
    <div class='tool-header'>
        <span class='tool-badge'>LEVEL 1</span>
        <span style='font-size:1.5rem; font-weight:800; color:#e2e8f0;'>🧠 Neural Network Playground</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='concept-box'>
        <h4>What is a Neural Network?</h4>
        <p>A neural network learns a <b>decision boundary</b> — an invisible line that separates different classes.
        Adjust the settings below and watch how the network learns to tell two groups apart.
        More hidden neurons = more complex boundary it can draw.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("#### ⚙️ Network Config")
        dataset = st.selectbox("Dataset Shape", ["Circles", "Moons", "Blobs", "XOR"])
        hidden_neurons = st.slider("Hidden Neurons (Layer 1)", 2, 16, 4)
        hidden_layers = st.slider("Number of Hidden Layers", 1, 4, 2)
        activation = st.selectbox("Activation Function", ["ReLU", "Tanh", "Sigmoid"])
        noise = st.slider("Data Noise", 0.0, 0.5, 0.1)
        n_samples = st.slider("Data Points", 50, 300, 150)
        run_btn = st.button("▶ Train & Visualize")

        st.markdown("""
        <div class='concept-box' style='margin-top:16px;'>
            <h4>💡 Try This</h4>
            <p>Set dataset to <b>Circles</b> with only <b>2 neurons</b> — it can't separate them!
            Now increase to <b>8</b> and watch the boundary curve.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        from sklearn.datasets import make_circles, make_moons, make_blobs
        from sklearn.neural_network import MLPClassifier
        from sklearn.preprocessing import StandardScaler

        np.random.seed(42)
        if dataset == "Circles":
            X, y = make_circles(n_samples=n_samples, noise=noise, factor=0.4)
        elif dataset == "Moons":
            X, y = make_moons(n_samples=n_samples, noise=noise)
        elif dataset == "XOR":
            X = np.random.randn(n_samples, 2)
            y = (X[:, 0] * X[:, 1] > 0).astype(int)
            X += np.random.randn(*X.shape) * noise
        else:
            X, y = make_blobs(n_samples=n_samples, centers=2, cluster_std=noise * 5 + 0.5)

        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        act_map = {"ReLU": "relu", "Tanh": "tanh", "Sigmoid": "logistic"}
        layers = tuple([hidden_neurons] * hidden_layers)
        clf = MLPClassifier(hidden_layer_sizes=layers, activation=act_map[activation],
                            max_iter=500, random_state=42)
        clf.fit(X, y)
        acc = clf.score(X, y)

        # Decision boundary plot
        h = 0.03
        x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
        y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        fig, ax = plt.subplots(figsize=(7, 5))
        fig.patch.set_facecolor('#0d1220')
        ax.set_facecolor('#080c14')
        ax.contourf(xx, yy, Z, alpha=0.25, cmap='coolwarm')
        ax.contour(xx, yy, Z, colors=['#00d4ff'], linewidths=1.5, alpha=0.7)
        scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm',
                            edgecolors='white', linewidths=0.5, s=40, alpha=0.9)
        ax.set_title(f"Decision Boundary — {dataset} | Accuracy: {acc:.1%}",
                    color='#e2e8f0', fontsize=11, pad=12)
        ax.tick_params(colors='#475569')
        for spine in ax.spines.values():
            spine.set_edgecolor('#1e2d45')
        ax.set_xlabel("Feature 1", color='#475569')
        ax.set_ylabel("Feature 2", color='#475569')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

        # Network architecture diagram (text-based)
        st.markdown("#### 🏗️ Network Architecture")
        arch_html = "<div style='display:flex; align-items:center; gap:6px; flex-wrap:wrap; justify-content:center; padding:12px; background:#0d1220; border-radius:10px; border:1px solid #1e2d45;'>"
        arch_html += f"<div style='text-align:center'><div style='color:#64748b; font-size:0.7rem; margin-bottom:6px;'>INPUT</div>"
        for _ in range(2):
            arch_html += "<div style='width:28px;height:28px;border-radius:50%;background:#1e2d45;border:2px solid #334155;margin:3px auto;'></div>"
        arch_html += "</div><div style='color:#334155; font-size:1.5rem;'>→</div>"
        for l in range(hidden_layers):
            arch_html += f"<div style='text-align:center'><div style='color:#64748b; font-size:0.7rem; margin-bottom:6px;'>H{l+1}</div>"
            for _ in range(min(hidden_neurons, 8)):
                arch_html += "<div style='width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#0ea5e9,#6366f1);margin:3px auto;'></div>"
            if hidden_neurons > 8:
                arch_html += f"<div style='color:#64748b; font-size:0.7rem;'>+{hidden_neurons-8} more</div>"
            arch_html += "</div><div style='color:#334155; font-size:1.5rem;'>→</div>"
        arch_html += "<div style='text-align:center'><div style='color:#64748b; font-size:0.7rem; margin-bottom:6px;'>OUTPUT</div>"
        arch_html += "<div style='width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,#22c55e,#0ea5e9);margin:3px auto;'></div>"
        arch_html += "</div></div>"
        st.markdown(arch_html, unsafe_allow_html=True)

        cols = st.columns(3)
        cols[0].metric("Accuracy", f"{acc:.1%}")
        cols[1].metric("Total Layers", hidden_layers + 2)
        cols[2].metric("Activation", activation)


# ════════════════════════════════════════════════════════════
# L2 — Data & Bias Explorer
# ════════════════════════════════════════════════════════════
elif level_code == "L2":
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use("Agg")
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score

    st.markdown("""
    <div class='tool-header'>
        <span class='tool-badge'>LEVEL 2</span>
        <span style='font-size:1.5rem; font-weight:800; color:#e2e8f0;'>⚖️ Data & Bias Explorer</span>
    </div>
    <div class='concept-box'>
        <h4>Why Does Data Quality Matter?</h4>
        <p>AI models are only as good as the data they learn from. If training data is <b>imbalanced</b>,
        <b>noisy</b>, or <b>unrepresentative</b>, the model will be biased — even if accuracy looks high.
        Experiment below to see how bad data creates biased AI.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("#### 🎛️ Data Controls")
        class_ratio = st.slider("Class Imbalance (% Class A)", 10, 90, 50,
                                help="How many samples belong to Class A vs B")
        noise_level = st.slider("Label Noise (%)", 0, 40, 5,
                                help="Percentage of labels randomly flipped (bad labelling)")
        n_total = st.slider("Dataset Size", 100, 1000, 300)
        feature_bias = st.slider("Feature Bias", 0.0, 2.0, 0.0,
                                 help="Shift Class A features — simulates demographic skew")

        st.markdown("""
        <div class='concept-box' style='margin-top:16px;'>
            <h4>💡 Key Insight</h4>
            <p>Push <b>Class Imbalance to 90%</b>. The accuracy stays high but the model
            just predicts Class A for everything — Class B is completely ignored!</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        np.random.seed(0)
        n_a = int(n_total * class_ratio / 100)
        n_b = n_total - n_a

        X_a = np.random.randn(n_a, 2) + np.array([feature_bias, 0])
        X_b = np.random.randn(n_b, 2) + np.array([2, 2])
        X = np.vstack([X_a, X_b])
        y = np.array([0] * n_a + [1] * n_b)

        # Inject label noise
        flip_idx = np.random.choice(len(y), int(len(y) * noise_level / 100), replace=False)
        y_noisy = y.copy()
        y_noisy[flip_idx] = 1 - y_noisy[flip_idx]

        clf = LogisticRegression()
        clf.fit(X, y_noisy)
        preds = clf.predict(X)
        overall_acc = accuracy_score(y, preds)
        acc_a = accuracy_score(y[y == 0], preds[y == 0]) if n_a > 0 else 0
        acc_b = accuracy_score(y[y == 1], preds[y == 1]) if n_b > 0 else 0

        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        fig.patch.set_facecolor('#0d1220')

        for ax in axes:
            ax.set_facecolor('#080c14')
            ax.tick_params(colors='#475569')
            for spine in ax.spines.values():
                spine.set_edgecolor('#1e2d45')

        # Left: data distribution
        axes[0].scatter(X_a[:, 0], X_a[:, 1], c='#0ea5e9', alpha=0.5, s=20, label=f'Class A (n={n_a})')
        axes[0].scatter(X_b[:, 0], X_b[:, 1], c='#f472b6', alpha=0.5, s=20, label=f'Class B (n={n_b})')
        axes[0].set_title("Data Distribution", color='#e2e8f0', fontsize=10)
        axes[0].legend(fontsize=8, facecolor='#0d1220', labelcolor='#94a3b8', framealpha=0.8)

        # Right: per-class accuracy bar
        bars = axes[1].bar(['Class A', 'Class B', 'Overall'],
                           [acc_a, acc_b, overall_acc],
                           color=['#0ea5e9', '#f472b6', '#a78bfa'],
                           alpha=0.8, width=0.5)
        axes[1].set_ylim(0, 1.1)
        axes[1].axhline(y=0.5, color='#334155', linestyle='--', linewidth=1)
        axes[1].set_title("Per-Class Accuracy", color='#e2e8f0', fontsize=10)
        axes[1].set_ylabel("Accuracy", color='#475569')
        for bar, val in zip(bars, [acc_a, acc_b, overall_acc]):
            axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                        f'{val:.0%}', ha='center', color='#e2e8f0', fontsize=9)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

        bias_gap = abs(acc_a - acc_b)
        if bias_gap > 0.3:
            st.error(f"⚠️ High bias detected! Class accuracy gap: {bias_gap:.0%} — your model discriminates between groups.")
        elif bias_gap > 0.1:
            st.warning(f"⚠️ Moderate bias. Accuracy gap between classes: {bias_gap:.0%}")
        else:
            st.success(f"✅ Model is relatively fair. Accuracy gap: {bias_gap:.0%}")

        cols = st.columns(4)
        cols[0].metric("Overall Acc", f"{overall_acc:.0%}")
        cols[1].metric("Class A Acc", f"{acc_a:.0%}")
        cols[2].metric("Class B Acc", f"{acc_b:.0%}")
        cols[3].metric("Bias Gap", f"{bias_gap:.0%}", delta=None)


# ════════════════════════════════════════════════════════════
# L3 — CNN Feature Visualizer
# ════════════════════════════════════════════════════════════
elif level_code == "L3":
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use("Agg")
    from scipy.ndimage import convolve

    st.markdown("""
    <div class='tool-header'>
        <span class='tool-badge'>LEVEL 3</span>
        <span style='font-size:1.5rem; font-weight:800; color:#e2e8f0;'>🔬 CNN Filter Visualizer</span>
    </div>
    <div class='concept-box'>
        <h4>What Do CNN Filters Actually See?</h4>
        <p>Convolutional Neural Networks use <b>filters (kernels)</b> that slide across an image
        looking for specific patterns — edges, corners, textures. Each filter produces a
        <b>feature map</b> showing where that pattern appears. This is how CNNs "understand" images.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("#### 🎛️ Filter Controls")
        image_choice = st.selectbox("Test Image", ["Gradient Square", "Circle", "Grid Pattern", "Random Noise", "Checkerboard"])
        filter_type = st.selectbox("CNN Filter", [
            "Edge Detection (Sobel X)",
            "Edge Detection (Sobel Y)",
            "Sharpen",
            "Blur (Average)",
            "Emboss",
            "Corner Detector",
        ])
        img_size = st.slider("Image Size", 32, 128, 64)
        show_3d = st.checkbox("Show 3D Feature Map", value=False)

        st.markdown("""
        <div class='concept-box' style='margin-top:16px;'>
            <h4>💡 Try This</h4>
            <p>Switch between <b>Sobel X</b> and <b>Sobel Y</b>. One detects vertical edges,
            the other horizontal — together they form the full edge map used in early CNN layers.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Generate test image
        n = img_size
        if image_choice == "Gradient Square":
            img = np.zeros((n, n))
            img[n//4:3*n//4, n//4:3*n//4] = 1.0
            grad = np.linspace(0, 1, n)
            img = img * grad[np.newaxis, :]
        elif image_choice == "Circle":
            img = np.zeros((n, n))
            cx, cy = n // 2, n // 2
            for i in range(n):
                for j in range(n):
                    if (i - cx)**2 + (j - cy)**2 < (n//3)**2:
                        img[i, j] = 1.0
        elif image_choice == "Grid Pattern":
            img = np.zeros((n, n))
            img[::8, :] = 1.0
            img[:, ::8] = 1.0
        elif image_choice == "Checkerboard":
            img = np.indices((n, n)).sum(axis=0) % 2
            img = img.astype(float)
        else:
            np.random.seed(7)
            img = np.random.rand(n, n)

        # Define filters
        filters = {
            "Edge Detection (Sobel X)": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
            "Edge Detection (Sobel Y)": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
            "Sharpen":                  np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),
            "Blur (Average)":           np.ones((3, 3)) / 9,
            "Emboss":                   np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]),
            "Corner Detector":          np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]]),
        }
        kernel = filters[filter_type]
        feature_map = convolve(img, kernel)

        ncols = 3 if not show_3d else 2
        fig, axes = plt.subplots(1, ncols, figsize=(10, 3.5))
        fig.patch.set_facecolor('#0d1220')

        # Original
        axes[0].imshow(img, cmap='gray', interpolation='nearest')
        axes[0].set_title("Original Image", color='#e2e8f0', fontsize=10)
        axes[0].axis('off')

        # Kernel visualization
        if not show_3d:
            im = axes[1].imshow(kernel, cmap='RdBu', interpolation='nearest')
            axes[1].set_title("Filter Kernel (3×3)", color='#e2e8f0', fontsize=10)
            for i in range(kernel.shape[0]):
                for j in range(kernel.shape[1]):
                    axes[1].text(j, i, f'{kernel[i,j]:.0f}' if kernel[i,j] == int(kernel[i,j]) else f'{kernel[i,j]:.2f}',
                                ha='center', va='center', color='white', fontsize=9, fontweight='bold')
            axes[1].axis('off')
            ax_fm = axes[2]
        else:
            ax_fm = axes[1]

        # Feature map
        ax_fm.imshow(feature_map, cmap='plasma', interpolation='nearest')
        ax_fm.set_title("Feature Map (Output)", color='#e2e8f0', fontsize=10)
        ax_fm.axis('off')

        plt.tight_layout(pad=1.0)
        st.pyplot(fig)
        plt.close()

        if show_3d:
            fig2 = plt.figure(figsize=(7, 4))
            fig2.patch.set_facecolor('#0d1220')
            ax3d = fig2.add_subplot(111, projection='3d')
            ax3d.set_facecolor('#080c14')
            step = max(1, n // 32)
            X3, Y3 = np.meshgrid(range(0, n, step), range(0, n, step))
            Z3 = feature_map[::step, ::step]
            ax3d.plot_surface(X3, Y3, Z3, cmap='plasma', alpha=0.9)
            ax3d.set_title("3D Feature Activation", color='#e2e8f0')
            ax3d.tick_params(colors='#475569', labelsize=6)
            st.pyplot(fig2)
            plt.close()

        cols = st.columns(3)
        cols[0].metric("Max Activation", f"{feature_map.max():.2f}")
        cols[1].metric("Mean Activation", f"{feature_map.mean():.2f}")
        cols[2].metric("Active Pixels", f"{(np.abs(feature_map) > 0.1).sum()}")


# ════════════════════════════════════════════════════════════
# L4 — Prompt Engineering Lab
# ════════════════════════════════════════════════════════════
elif level_code == "L4":
    st.markdown("""
    <div class='tool-header'>
        <span class='tool-badge'>LEVEL 4</span>
        <span style='font-size:1.5rem; font-weight:800; color:#e2e8f0;'>✍️ Prompt Engineering Lab</span>
    </div>
    <div class='concept-box'>
        <h4>Why Does Prompt Design Matter?</h4>
        <p>Large Language Models are extremely sensitive to <b>how you phrase your instructions</b>.
        The same question asked differently can yield wildly different responses.
        This lab shows you the key prompt engineering techniques used by AI engineers.</p>
    </div>
    """, unsafe_allow_html=True)

    TECHNIQUES = {
        "Zero-Shot": {
            "desc": "No examples given — just a direct instruction. The model relies purely on its training.",
            "template": "Classify the sentiment of this text as Positive, Negative, or Neutral.\n\nText: {input}\n\nSentiment:",
            "tip": "Simple but unreliable for complex tasks. Works best with large, well-trained models."
        },
        "Few-Shot": {
            "desc": "Give the model 2–3 examples before your actual input. This 'shows' it the pattern.",
            "template": "Classify sentiment as Positive, Negative, or Neutral.\n\nText: I love this product!\nSentiment: Positive\n\nText: This is terrible quality.\nSentiment: Negative\n\nText: {input}\nSentiment:",
            "tip": "Dramatically improves accuracy on structured tasks. The examples act as in-context training data."
        },
        "Chain of Thought": {
            "desc": "Ask the model to reason step-by-step before answering. Improves logic and math tasks.",
            "template": "Analyze this text carefully. First, identify emotional keywords. Then consider overall tone. Finally, classify.\n\nText: {input}\n\nStep 1 - Keywords:\nStep 2 - Tone:\nStep 3 - Final Sentiment:",
            "tip": "Adds 'thinking time' before the answer. Reduces hallucinations on complex reasoning tasks."
        },
        "Role Prompting": {
            "desc": "Assign the model a specific role or persona before the task.",
            "template": "You are an expert linguistics researcher specializing in emotional analysis of text.\nApply your expertise to classify the following.\n\nText: {input}\n\nYour expert classification:",
            "tip": "Activates relevant 'knowledge clusters' in the model. Very effective for domain-specific tasks."
        },
        "Structured Output": {
            "desc": "Ask the model to return a specific format (JSON, table, etc.) for easier parsing.",
            "template": 'Analyze this text and return ONLY a JSON object with keys: "sentiment", "confidence" (0-1), "keywords" (list).\n\nText: {input}\n\nJSON:',
            "tip": "Critical for production AI systems where you need to parse and use the output programmatically."
        },
    }

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### 🎛️ Prompt Builder")
        technique = st.selectbox("Technique", list(TECHNIQUES.keys()))
        user_input = st.text_area("Your Input Text",
            value="The new update broke everything and now I can't even log in.",
            height=80)
        system_msg = st.text_area("System Message (Optional)",
            value="You are a helpful AI assistant.",
            height=60)

        info = TECHNIQUES[technique]
        st.markdown(f"""
        <div class='concept-box'>
            <h4>📖 {technique}</h4>
            <p>{info['desc']}</p>
            <p style='color:#fbbf24; font-size:0.85rem;'>💡 {info['tip']}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### 📋 Generated Prompt")
        prompt = info["template"].replace("{input}", user_input)
        full_prompt = f"[SYSTEM]\n{system_msg}\n\n[USER]\n{prompt}"

        st.code(full_prompt, language="markdown")

        st.markdown("#### 📊 Prompt Analysis")
        token_est = len(full_prompt.split()) * 1.3
        cols = st.columns(3)
        cols[0].metric("~Token Count", f"{int(token_est)}")
        cols[1].metric("Technique", technique)
        cols[2].metric("Has Examples", "Yes" if technique == "Few-Shot" else "No")

        st.markdown("#### 🔄 Technique Comparison")
        compare_data = []
        for name, t in TECHNIQUES.items():
            p = t["template"].replace("{input}", user_input)
            compare_data.append({"Technique": name, "~Tokens": int(len(p.split()) * 1.3)})

        import pandas as pd
        df = pd.DataFrame(compare_data)
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.info("💡 Copy the generated prompt above and test it in any LLM chat interface to see the difference!")


# ════════════════════════════════════════════════════════════
# L5 — RAG Pipeline Visualizer
# ════════════════════════════════════════════════════════════
elif level_code == "L5":
    import numpy as np

    st.markdown("""
    <div class='tool-header'>
        <span class='tool-badge'>LEVEL 5</span>
        <span style='font-size:1.5rem; font-weight:800; color:#e2e8f0;'>🔍 RAG Pipeline Visualizer</span>
    </div>
    <div class='concept-box'>
        <h4>What is Retrieval-Augmented Generation (RAG)?</h4>
        <p>RAG solves a core LLM problem: models don't know facts outside their training data.
        RAG adds a <b>retrieval step</b> — before generating, the system searches a knowledge base
        for relevant documents and adds them to the prompt. This grounds the model in real facts.</p>
    </div>
    """, unsafe_allow_html=True)

    KNOWLEDGE_BASE = {
        "AI History": [
            "The term 'Artificial Intelligence' was coined by John McCarthy in 1956 at the Dartmouth Conference.",
            "Alan Turing proposed the Turing Test in 1950 as a measure of machine intelligence.",
            "The first neural network, the Perceptron, was invented by Frank Rosenblatt in 1958.",
            "Deep learning became dominant after AlexNet won ImageNet in 2012 with a large margin.",
            "GPT-3 was released by OpenAI in 2020 with 175 billion parameters.",
        ],
        "Machine Learning": [
            "Supervised learning uses labeled data where each input has a known correct output.",
            "Unsupervised learning finds patterns in data without any labels.",
            "Reinforcement learning trains agents by rewarding correct actions and penalizing wrong ones.",
            "Overfitting occurs when a model memorizes training data but fails on new data.",
            "Cross-validation splits data into folds to give a more reliable estimate of model performance.",
        ],
        "Computer Vision": [
            "Convolutional Neural Networks (CNNs) use filters to detect spatial features in images.",
            "Object detection models like YOLO predict both class labels and bounding boxes simultaneously.",
            "Image segmentation assigns a class label to every single pixel in an image.",
            "Transfer learning reuses a pretrained model's weights as a starting point for a new task.",
            "Data augmentation artificially expands a dataset by flipping, rotating, and cropping images.",
        ],
        "NLP & LLMs": [
            "Transformers use self-attention to weigh the importance of each word relative to all others.",
            "BERT is a bidirectional transformer pretrained on masked language modeling.",
            "Tokenization converts raw text into numerical tokens that a model can process.",
            "Embeddings represent words or sentences as dense numerical vectors in high-dimensional space.",
            "Hallucination refers to when an LLM generates confident but factually incorrect statements.",
        ],
    }

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### 📝 User Query")
        topic = st.selectbox("Knowledge Base Topic", list(KNOWLEDGE_BASE.keys()))
        query = st.text_input("Ask a Question", value="How do neural networks learn from images?")
        top_k = st.slider("Top-K Documents to Retrieve", 1, 5, 3)
        chunking = st.selectbox("Chunking Strategy", ["Sentence-level", "Fixed-size", "Semantic"])

        st.markdown("""
        <div class='concept-box' style='margin-top:12px;'>
            <h4>💡 RAG vs Pure LLM</h4>
            <p><b>Pure LLM:</b> "I think neural networks use... something like gradients?"<br>
            <b>RAG:</b> Retrieves exact relevant docs → grounds answer in facts → no hallucination</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### 🔄 Pipeline Execution")

        docs = KNOWLEDGE_BASE[topic]

        def simple_similarity(query, doc):
            q_words = set(query.lower().split())
            d_words = set(doc.lower().split())
            return len(q_words & d_words) / (len(q_words | d_words) + 1e-9)

        scores = [(doc, simple_similarity(query, doc)) for doc in docs]
        scores.sort(key=lambda x: x[1], reverse=True)
        retrieved = scores[:top_k]

        # Step-by-step pipeline
        steps = [
            ("1. Query", "Received", True),
            ("2. Embed", "Vectorized", True),
            ("3. Retrieve", f"Top-{top_k} docs", True),
            ("4. Augment", "Prompt built", True),
            ("5. Generate", "LLM responds", True),
        ]

        pipeline_html = "<div class='pipeline'>"
        for label, status, done in steps:
            pipeline_html += f"<div class='pipe-step {'active' if done else ''}'>{label}<br><small style='color:#64748b'>{status}</small></div>"
            pipeline_html += "<div class='pipe-arrow'>→</div>"
        pipeline_html = pipeline_html.rstrip("<div class='pipe-arrow'>→</div>") + "</div>"
        st.markdown(pipeline_html, unsafe_allow_html=True)

        st.markdown("#### 📚 Retrieved Documents")
        for i, (doc, score) in enumerate(retrieved):
            color = "#22c55e" if score > 0.1 else "#f59e0b" if score > 0.05 else "#ef4444"
            st.markdown(f"""
            <div style='background:#0d1220; border:1px solid {color}33; border-left: 3px solid {color};
                        border-radius:8px; padding:12px; margin-bottom:8px;'>
                <div style='display:flex; justify-content:space-between; margin-bottom:6px;'>
                    <span style='color:#64748b; font-size:0.75rem;'>Document {i+1}</span>
                    <span style='color:{color}; font-size:0.75rem; font-weight:600;'>Score: {score:.3f}</span>
                </div>
                <div style='color:#e2e8f0; font-size:0.9rem; line-height:1.5;'>{doc}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("#### 🤖 Augmented Prompt Preview")
        context = "\n".join([f"- {doc}" for doc, _ in retrieved])
        augmented = f"""[CONTEXT]\n{context}\n\n[QUESTION]\n{query}\n\n[INSTRUCTION]\nAnswer using only the context above."""
        st.code(augmented, language="markdown")

        cols = st.columns(3)
        cols[0].metric("Docs Retrieved", top_k)
        cols[1].metric("Best Score", f"{retrieved[0][1]:.3f}")
        cols[2].metric("Context Tokens", f"~{int(len(context.split()) * 1.3)}")


# ════════════════════════════════════════════════════════════
# L6 — Agentic Workflow Sandbox
# ════════════════════════════════════════════════════════════
elif level_code == "L6":
    import json

    st.markdown("""
    <div class='tool-header'>
        <span class='tool-badge'>LEVEL 6</span>
        <span style='font-size:1.5rem; font-weight:800; color:#e2e8f0;'>🤖 Agentic Workflow Sandbox</span>
    </div>
    <div class='concept-box'>
        <h4>What Are Agentic AI Systems?</h4>
        <p>Agentic AI goes beyond single responses. An <b>agent</b> has a goal, a set of tools,
        and a loop: it <b>thinks → acts → observes → repeats</b> until the goal is complete.
        Systems like LangGraph and AutoGen build these as directed graphs of nodes and edges.</p>
    </div>
    """, unsafe_allow_html=True)

    AGENT_TEMPLATES = {
        "Research Agent": {
            "nodes": ["User Input", "Planner", "Web Search", "Summarizer", "Critic", "Final Answer"],
            "edges": [("User Input","Planner"), ("Planner","Web Search"), ("Web Search","Summarizer"),
                      ("Summarizer","Critic"), ("Critic","Planner"), ("Critic","Final Answer")],
            "desc": "Searches the web, summarizes findings, self-critiques, and loops until confident.",
            "tools": ["web_search", "summarize", "self_critique"],
        },
        "Code Agent": {
            "nodes": ["Task", "Code Generator", "Executor", "Error Handler", "Tester", "Done"],
            "edges": [("Task","Code Generator"), ("Code Generator","Executor"),
                      ("Executor","Error Handler"), ("Error Handler","Code Generator"),
                      ("Executor","Tester"), ("Tester","Done")],
            "desc": "Generates code, runs it, catches errors, fixes and retries automatically.",
            "tools": ["code_gen", "execute", "debug"],
        },
        "RAG Agent": {
            "nodes": ["Query", "Router", "Retriever", "Grader", "Generator", "Hallucination Check", "Output"],
            "edges": [("Query","Router"), ("Router","Retriever"), ("Retriever","Grader"),
                      ("Grader","Retriever"), ("Grader","Generator"),
                      ("Generator","Hallucination Check"), ("Hallucination Check","Generator"),
                      ("Hallucination Check","Output")],
            "desc": "Routes queries, retrieves docs, grades relevance, generates and self-checks for hallucinations.",
            "tools": ["embed", "retrieve", "grade", "generate", "hallucination_check"],
        },
        "Custom": {
            "nodes": ["Start", "Tool A", "Tool B", "Decision", "End"],
            "edges": [("Start","Tool A"), ("Tool A","Decision"), ("Tool B","Decision"), ("Decision","End")],
            "desc": "Build your own agent graph.",
            "tools": ["custom"],
        }
    }

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### 🏗️ Agent Builder")
        template = st.selectbox("Agent Template", list(AGENT_TEMPLATES.keys()))
        agent = AGENT_TEMPLATES[template]

        st.markdown(f"""
        <div class='concept-box'>
            <h4>📋 {template}</h4>
            <p>{agent['desc']}</p>
            <p style='color:#64748b; font-size:0.8rem;'>Tools: <span style='color:#00d4ff;'>{', '.join(agent['tools'])}</span></p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### ⚙️ Agent Config")
        max_iter = st.slider("Max Iterations", 1, 10, 5)
        has_memory = st.checkbox("Enable Memory", value=True)
        has_critique = st.checkbox("Self-Critique Loop", value=True)
        stream_output = st.checkbox("Stream Thought Process", value=True)

        st.markdown("#### 🔧 Available Tools")
        all_tools = ["web_search", "code_execute", "file_read", "summarize", "embed", "retrieve", "send_email"]
        selected_tools = st.multiselect("Add Tools to Agent", all_tools, default=agent['tools'][:2] if agent['tools'][0] != 'custom' else [])

    with col2:
        st.markdown("#### 🗺️ Agent Graph")

        import matplotlib
        import matplotlib.pyplot as plt
        matplotlib.use("Agg")

        nodes = agent["nodes"]
        edges = agent["edges"]

        n = len(nodes)
        angles = [2 * 3.14159 * i / n for i in range(n)]
        pos = {node: (0.85 * __import__('math').cos(a), 0.85 * __import__('math').sin(a))
               for node, a in zip(nodes, angles)}

        fig, ax = plt.subplots(figsize=(6, 5))
        fig.patch.set_facecolor('#0d1220')
        ax.set_facecolor('#080c14')
        ax.set_xlim(-1.4, 1.4)
        ax.set_ylim(-1.4, 1.4)
        ax.axis('off')

        node_colors = {
            nodes[0]: '#22c55e',
            nodes[-1]: '#f43f5e',
        }

        # Draw edges
        for src, dst in edges:
            x0, y0 = pos[src]
            x1, y1 = pos[dst]
            is_back = edges.index((src, dst)) > len(edges) // 2
            ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                        arrowprops=dict(
                            arrowstyle="->",
                            color='#f97316' if is_back else '#334155',
                            lw=1.5,
                            connectionstyle="arc3,rad=0.2" if is_back else "arc3,rad=0.05"
                        ))

        # Draw nodes
        for node in nodes:
            x, y = pos[node]
            color = node_colors.get(node, '#0ea5e9')
            circle = plt.Circle((x, y), 0.13, color=color, alpha=0.85, zorder=3)
            ax.add_patch(circle)
            ax.text(x, y, node, ha='center', va='center', color='white',
                   fontsize=6.5, fontweight='bold', zorder=4, wrap=True,
                   multialignment='center')

        # Legend
        ax.plot([], [], 'o', color='#22c55e', label='Start', markersize=8)
        ax.plot([], [], 'o', color='#0ea5e9', label='Node', markersize=8)
        ax.plot([], [], 'o', color='#f43f5e', label='End', markersize=8)
        ax.plot([], [], '-', color='#f97316', label='Feedback loop', linewidth=2)
        ax.legend(fontsize=7, facecolor='#0d1220', labelcolor='#94a3b8',
                 framealpha=0.8, loc='lower right')

        ax.set_title(f"{template} — {len(nodes)} nodes, {len(edges)} edges",
                    color='#e2e8f0', fontsize=9, pad=8)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

        st.markdown("#### 🔁 Simulated Agent Run")
        if st.button("▶ Run Agent Simulation"):
            import time
            log_placeholder = st.empty()
            log = []
            thought_patterns = [
                ("🧠 Thinking", f"Planning approach for task using {', '.join(selected_tools or ['base tools'])}"),
                ("🔧 Action", f"Calling tool: {(selected_tools or ['web_search'])[0]}"),
                ("👁️ Observation", "Tool returned relevant results. Analyzing..."),
                ("🧠 Thinking", "Do I have enough information? Checking criteria..."),
                ("🔧 Action", f"Calling tool: {(selected_tools or ['summarize'])[-1] if len(selected_tools or []) > 1 else 'summarize'}"),
                ("👁️ Observation", "Summary generated. Quality check passed."),
                ("✅ Done", "Goal achieved. Returning final answer."),
            ]
            for i, (tag, msg) in enumerate(thought_patterns[:max_iter + 2]):
                log.append(f"**Iter {i+1}** `[{tag}]` {msg}")
                log_placeholder.markdown("\n\n".join(log))
                time.sleep(0.4)

        cols = st.columns(3)
        cols[0].metric("Nodes", len(nodes))
        cols[1].metric("Edges", len(edges))
        feedback_loops = sum(1 for s, d in edges if nodes.index(d) < nodes.index(s))
        cols[2].metric("Feedback Loops", feedback_loops)


# ════════════════════════════════════════════════════════════
# L7 — HTML / CSS / JS Interactive Lab
# ════════════════════════════════════════════════════════════
elif level_code == "L7":

    st.markdown("""
    <div class='tool-header'>
        <span class='tool-badge'>LEVEL 7</span>
        <span style='font-size:1.5rem; font-weight:800; color:#e2e8f0;'>🌐 HTML / CSS / JS Lab</span>
    </div>
    <div class='concept-box'>
        <h4>Learn Web Technologies Interactively</h4>
        <p>Three hands-on tools to understand the building blocks of the web.
        See how <b>HTML</b> structures content, <b>CSS</b> styles it, and
        <b>JavaScript</b> makes it interactive — all live in your browser.</p>
    </div>
    """, unsafe_allow_html=True)

    sub_tool = st.selectbox(
        "Choose a topic",
        ["🏗️ HTML Structure Explorer", "🎨 CSS Properties Playground", "⚡ JS Concepts Visualizer"],
        label_visibility="visible"
    )

    # ── SUB-TOOL 1: HTML Structure Explorer ─────────────────
    if "HTML" in sub_tool:

        st.markdown("""
        <div class='concept-box'>
            <h4>What is HTML?</h4>
            <p>HTML (HyperText Markup Language) uses <b>tags</b> to give structure to content.
            Every webpage is a tree of nested elements — called the <b>DOM (Document Object Model)</b>.
            Pick an element below to see its tag, purpose, and live preview.</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])

        HTML_ELEMENTS = {
            "Headings (h1–h6)": {
                "tag": "<h1> to <h6>",
                "purpose": "Define titles and subheadings. h1 is the most important, h6 the least.",
                "category": "Text",
                "preview": """<div style='font-family:sans-serif; padding:12px; background:#111827; border-radius:8px;'>
<h1 style='color:#f8fafc;margin:4px 0;font-size:2rem'>Heading 1</h1>
<h2 style='color:#cbd5e1;margin:4px 0;font-size:1.5rem'>Heading 2</h2>
<h3 style='color:#94a3b8;margin:4px 0;font-size:1.25rem'>Heading 3</h3>
<h4 style='color:#64748b;margin:4px 0;font-size:1rem'>Heading 4</h4>
<h5 style='color:#475569;margin:4px 0;font-size:.85rem'>Heading 5</h5>
<h6 style='color:#334155;margin:4px 0;font-size:.75rem'>Heading 6</h6>
</div>""",
                "code": "<h1>Main Title</h1>\n<h2>Section Title</h2>\n<h3>Subsection</h3>",
                "dom_children": ["h1", "h2", "h3", "h4", "h5", "h6"],
            },
            "Paragraph & Text": {
                "tag": "<p>, <span>, <strong>, <em>",
                "purpose": "Paragraphs wrap blocks of text. Span wraps inline text. Strong = bold, em = italic.",
                "category": "Text",
                "preview": """<div style='font-family:sans-serif; padding:12px; background:#111827; border-radius:8px; color:#e2e8f0;'>
<p>This is a <strong>paragraph</strong> with <em>italic</em> and <span style='color:#00d4ff'>colored span</span>.</p>
<p style='color:#94a3b8;font-size:0.9rem'>A second paragraph — block-level, always starts on a new line.</p>
</div>""",
                "code": "<p>This is a <strong>bold</strong> and <em>italic</em> text.</p>\n<span style='color:red'>Inline span</span>",
                "dom_children": ["p", "span", "strong", "em", "b", "i"],
            },
            "Lists (ul / ol)": {
                "tag": "<ul>, <ol>, <li>",
                "purpose": "ul = unordered (bullet) list. ol = ordered (numbered) list. li = list item.",
                "category": "Structure",
                "preview": """<div style='font-family:sans-serif; padding:12px; background:#111827; border-radius:8px; color:#e2e8f0; display:flex; gap:32px;'>
<div><p style='color:#00d4ff;margin:0 0 6px'>Unordered</p><ul style='margin:0;padding-left:20px'><li>HTML</li><li>CSS</li><li>JavaScript</li></ul></div>
<div><p style='color:#a78bfa;margin:0 0 6px'>Ordered</p><ol style='margin:0;padding-left:20px'><li>Learn HTML</li><li>Learn CSS</li><li>Build!</li></ol></div>
</div>""",
                "code": "<ul>\n  <li>Unordered item</li>\n  <li>Another item</li>\n</ul>\n\n<ol>\n  <li>Step one</li>\n  <li>Step two</li>\n</ol>",
                "dom_children": ["ul", "ol", "li"],
            },
            "Links & Images": {
                "tag": "<a>, <img>",
                "purpose": "a creates clickable hyperlinks. img embeds images. Both use attributes (href, src, alt).",
                "category": "Media",
                "preview": """<div style='font-family:sans-serif; padding:12px; background:#111827; border-radius:8px; color:#e2e8f0;'>
<a href='#' style='color:#00d4ff;text-decoration:none;'>🔗 This is a hyperlink</a>
<br><br>
<div style='width:80px;height:50px;background:#1e2d45;border:2px dashed #334155;border-radius:4px;display:flex;align-items:center;justify-content:center;font-size:0.7rem;color:#64748b;'>img placeholder</div>
</div>""",
                "code": '<a href="https://example.com">Visit Example</a>\n\n<img src="photo.jpg" alt="Description" width="200">',
                "dom_children": ["a", "img"],
            },
            "Div & Semantic Tags": {
                "tag": "<div>, <header>, <main>, <section>, <footer>",
                "purpose": "div is a generic container. Semantic tags (header, main, footer) tell browsers AND developers what each section means.",
                "category": "Structure",
                "preview": """<div style='font-family:sans-serif; padding:8px; background:#111827; border-radius:8px; font-size:0.75rem;'>
<div style='background:#164e63;border:1px solid #0e7490;border-radius:4px;padding:6px;margin:3px;color:#67e8f9;'>&lt;header&gt; — Logo, nav bar</div>
<div style='background:#1e1b4b;border:1px solid #4338ca;border-radius:4px;padding:6px;margin:3px;color:#a5b4fc;'>&lt;main&gt;
  <div style='background:#14532d;border:1px solid #166534;border-radius:3px;padding:4px;margin:3px;color:#86efac;'>&lt;section&gt; Content</div>
</div>
<div style='background:#3b0764;border:1px solid #7c3aed;border-radius:4px;padding:6px;margin:3px;color:#c4b5fd;'>&lt;footer&gt; — Copyright, links</div>
</div>""",
                "code": "<header>Logo and nav here</header>\n<main>\n  <section>Content here</section>\n</main>\n<footer>Footer here</footer>",
                "dom_children": ["div", "header", "nav", "main", "section", "article", "aside", "footer"],
            },
            "Forms & Inputs": {
                "tag": "<form>, <input>, <button>, <label>",
                "purpose": "Forms collect user data. Inputs can be text, email, checkbox, radio. Always pair inputs with labels for accessibility.",
                "category": "Interactive",
                "preview": """<div style='font-family:sans-serif; padding:12px; background:#111827; border-radius:8px;'>
<form style='display:flex;flex-direction:column;gap:8px;'>
<label style='color:#94a3b8;font-size:0.8rem;'>Name</label>
<input type='text' placeholder='Enter name...' style='padding:6px 10px;border-radius:4px;border:1px solid #334155;background:#1e2d45;color:#e2e8f0;font-size:0.85rem;'>
<label style='color:#94a3b8;font-size:0.8rem;'>Email</label>
<input type='email' placeholder='you@email.com' style='padding:6px 10px;border-radius:4px;border:1px solid #334155;background:#1e2d45;color:#e2e8f0;font-size:0.85rem;'>
<button type='button' style='padding:7px;background:#0ea5e9;color:white;border:none;border-radius:4px;cursor:pointer;font-size:0.85rem;'>Submit</button>
</form></div>""",
                "code": '<form>\n  <label>Name:</label>\n  <input type="text" placeholder="Your name">\n  \n  <label>Email:</label>\n  <input type="email">\n  \n  <button type="submit">Send</button>\n</form>',
                "dom_children": ["form", "input", "textarea", "select", "button", "label"],
            },
            "Table": {
                "tag": "<table>, <tr>, <th>, <td>",
                "purpose": "Tables display data in rows and columns. thead = header rows, tbody = data rows, tr = row, th = header cell, td = data cell.",
                "category": "Data",
                "preview": """<div style='padding:12px; background:#111827; border-radius:8px;'>
<table style='border-collapse:collapse;width:100%;font-family:sans-serif;font-size:0.8rem;'>
<thead><tr style='background:#1e2d45;'><th style='padding:6px 10px;color:#00d4ff;text-align:left;border:1px solid #334155;'>Name</th><th style='padding:6px 10px;color:#00d4ff;text-align:left;border:1px solid #334155;'>Score</th></tr></thead>
<tbody>
<tr><td style='padding:6px 10px;color:#e2e8f0;border:1px solid #1e2d45;'>Alice</td><td style='padding:6px 10px;color:#86efac;border:1px solid #1e2d45;'>98</td></tr>
<tr style='background:#0d1220'><td style='padding:6px 10px;color:#e2e8f0;border:1px solid #1e2d45;'>Bob</td><td style='padding:6px 10px;color:#fcd34d;border:1px solid #1e2d45;'>74</td></tr>
</tbody></table></div>""",
                "code": "<table>\n  <thead>\n    <tr><th>Name</th><th>Score</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Alice</td><td>98</td></tr>\n    <tr><td>Bob</td><td>74</td></tr>\n  </tbody>\n</table>",
                "dom_children": ["table", "thead", "tbody", "tr", "th", "td"],
            },
        }

        with col1:
            element = st.selectbox("Select HTML Element", list(HTML_ELEMENTS.keys()))
            info = HTML_ELEMENTS[element]

            st.markdown(f"""
            <div class='concept-box'>
                <h4>🏷️ Tag: <code style='background:#0d1220;padding:2px 6px;border-radius:4px;font-size:0.85rem'>{info['tag']}</code></h4>
                <p>{info['purpose']}</p>
                <p style='margin-top:8px;'><span style='background:#1e2d45;color:#a78bfa;padding:2px 8px;border-radius:12px;font-size:0.75rem;font-weight:600;'>Category: {info['category']}</span></p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 📝 Code")
            st.code(info["code"], language="html")

            st.markdown("#### 🌳 Child Tags")
            tags_html = " ".join([
                f"<code style='background:#1e2d45;color:#7dd3fc;padding:3px 8px;border-radius:6px;font-size:0.8rem;margin:2px;display:inline-block'>&lt;{t}&gt;</code>"
                for t in info["dom_children"]
            ])
            st.markdown(tags_html, unsafe_allow_html=True)

        with col2:
            st.markdown("#### 👁️ Live Preview")
            st.markdown(info["preview"], unsafe_allow_html=True)

            st.markdown("#### 🌳 DOM Tree View")
            dom_items = info["dom_children"]
            tree_html = "<div style='background:#0d1220;border:1px solid #1e2d45;border-radius:10px;padding:14px;font-family:monospace;font-size:0.82rem;'>"
            tree_html += f"<div style='color:#f472b6;'>📄 document</div>"
            tree_html += f"<div style='color:#60a5fa;margin-left:16px;'>└─ &lt;html&gt;</div>"
            tree_html += f"<div style='color:#34d399;margin-left:32px;'>└─ &lt;body&gt;</div>"
            for i, tag in enumerate(dom_items[:5]):
                prefix = "├─" if i < len(dom_items[:5]) - 1 else "└─"
                tree_html += f"<div style='color:#fcd34d;margin-left:48px;'>{prefix} &lt;{tag}&gt;</div>"
            tree_html += "</div>"
            st.markdown(tree_html, unsafe_allow_html=True)

            st.markdown("#### 🧩 Quick Quiz")
            quiz_q = {
                "Headings (h1–h6)": ("Which heading tag has the LOWEST visual importance?", "h6"),
                "Paragraph & Text": ("Which tag makes text bold by default?", "strong"),
                "Lists (ul / ol)": ("Which tag do you use for a numbered list?", "ol"),
                "Links & Images": ("What attribute sets the URL for a link?", "href"),
                "Div & Semantic Tags": ("What semantic tag wraps the main page content?", "main"),
                "Forms & Inputs": ("What attribute makes a button submit the form?", "type='submit'"),
                "Table": ("What tag defines a header cell in a table?", "th"),
            }
            q, ans = quiz_q[element]
            st.markdown(f"<div style='color:#fcd34d;font-size:0.9rem;font-weight:600;margin-bottom:6px;'>❓ {q}</div>", unsafe_allow_html=True)
            user_ans = st.text_input("Your answer", key=f"quiz_{element}", placeholder="Type tag name...")
            if user_ans:
                if user_ans.strip().lower().replace("<","").replace(">","") in ans.replace("<","").replace(">","").lower():
                    st.success(f"✅ Correct! `<{ans}>` is right.")
                else:
                    st.error(f"❌ Not quite. The answer is `{ans}`.")

    # ── SUB-TOOL 2: CSS Properties Playground ───────────────
    elif "CSS" in sub_tool:

        st.markdown("""
        <div class='concept-box'>
            <h4>What is CSS?</h4>
            <p>CSS (Cascading Style Sheets) controls <b>how HTML elements look</b>. 
            Each CSS rule has a <b>selector</b> (what to target) and <b>declarations</b> (property: value).
            Use the sliders and pickers below to see CSS properties change in real time.</p>
        </div>
        """, unsafe_allow_html=True)

        css_topic = st.selectbox("CSS Topic", [
            "Box Model", "Typography", "Colors & Backgrounds",
            "Flexbox Layout", "CSS Selectors", "Transitions & Animation"
        ])

        col1, col2 = st.columns([1, 1])

        if css_topic == "Box Model":
            with col1:
                st.markdown("#### 🎛️ Box Model Controls")
                st.markdown("""<div class='concept-box'><h4>The Box Model</h4>
                <p>Every HTML element is a box. From outside in: <b>Margin</b> (space outside) → <b>Border</b> → <b>Padding</b> (space inside) → <b>Content</b>.</p></div>""", unsafe_allow_html=True)
                margin = st.slider("Margin (px)", 0, 40, 16)
                border = st.slider("Border width (px)", 0, 10, 2)
                padding = st.slider("Padding (px)", 0, 40, 16)
                border_radius = st.slider("Border radius (px)", 0, 50, 8)
                bg_color = st.color_picker("Background color", "#0ea5e9")
                border_color = st.color_picker("Border color", "#ffffff")
                st.code(f"""div {{
  margin: {margin}px;
  border: {border}px solid {border_color};
  padding: {padding}px;
  border-radius: {border_radius}px;
  background-color: {bg_color};
}}""", language="css")

            with col2:
                st.markdown("#### 👁️ Live Preview")
                box_html = f"""
                <div style='background:#0d1220;padding:30px;border-radius:12px;border:1px solid #1e2d45;display:flex;align-items:center;justify-content:center;min-height:260px;'>
                  <div style='background:#1e2d45;padding:20px;border-radius:8px;font-size:0.75rem;color:#64748b;font-family:monospace;text-align:center;'>
                    <span style='color:#f472b6'>MARGIN ({margin}px)</span>
                    <div style='margin:{margin}px;background:#0f2744;padding:4px;border-radius:4px;'>
                      <span style='color:#60a5fa'>BORDER ({border}px)</span>
                      <div style='border:{border}px solid {border_color};background:{bg_color};padding:{padding}px;border-radius:{border_radius}px;margin:4px;'>
                        <span style='color:#fff;font-weight:bold'>PADDING ({padding}px)</span>
                        <div style='background:rgba(0,0,0,0.3);padding:8px;border-radius:4px;margin-top:4px;'>
                          <span style='color:#fff;'>CONTENT</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>"""
                st.markdown(box_html, unsafe_allow_html=True)

        elif css_topic == "Typography":
            with col1:
                st.markdown("#### 🎛️ Typography Controls")
                font_size = st.slider("font-size (px)", 10, 48, 18)
                font_weight = st.select_slider("font-weight", options=[100,200,300,400,500,600,700,800,900], value=400)
                line_height = st.slider("line-height", 1.0, 3.0, 1.6)
                letter_spacing = st.slider("letter-spacing (px)", -2, 10, 0)
                text_color = st.color_picker("color", "#e2e8f0")
                text_align = st.selectbox("text-align", ["left","center","right","justify"])
                text_transform = st.selectbox("text-transform", ["none","uppercase","lowercase","capitalize"])
                st.code(f"""p {{
  font-size: {font_size}px;
  font-weight: {font_weight};
  line-height: {line_height};
  letter-spacing: {letter_spacing}px;
  color: {text_color};
  text-align: {text_align};
  text-transform: {text_transform};
}}""", language="css")

            with col2:
                st.markdown("#### 👁️ Live Preview")
                typo_html = f"""<div style='background:#0d1220;padding:24px;border-radius:12px;border:1px solid #1e2d45;'>
                <p style='font-size:{font_size}px;font-weight:{font_weight};line-height:{line_height};
                letter-spacing:{letter_spacing}px;color:{text_color};text-align:{text_align};
                text-transform:{text_transform};margin:0;'>
                The quick brown fox jumps over the lazy dog. CSS controls every visual aspect of how text appears on the web.
                </p></div>"""
                st.markdown(typo_html, unsafe_allow_html=True)
                st.markdown("""<div class='concept-box' style='margin-top:16px;'>
                <h4>💡 Key Tip</h4>
                <p>Use <b>line-height: 1.5–1.7</b> for body text — it dramatically improves readability.
                Font sizes below 14px are hard to read on most screens.</p></div>""", unsafe_allow_html=True)

        elif css_topic == "Colors & Backgrounds":
            with col1:
                st.markdown("#### 🎛️ Color Controls")
                bg = st.color_picker("background-color", "#0d1220")
                txt = st.color_picker("color (text)", "#e2e8f0")
                opacity_val = st.slider("opacity", 0.1, 1.0, 1.0)
                use_gradient = st.checkbox("Use gradient background")
                grad_c1 = st.color_picker("Gradient color 1", "#0ea5e9") if use_gradient else "#0ea5e9"
                grad_c2 = st.color_picker("Gradient color 2", "#a78bfa") if use_gradient else "#a78bfa"
                grad_dir = st.selectbox("Gradient direction", ["to right","to bottom","135deg","45deg"]) if use_gradient else "to right"
                bg_style = f"linear-gradient({grad_dir}, {grad_c1}, {grad_c2})" if use_gradient else bg
                st.code(f"""div {{
  background: {bg_style};
  color: {txt};
  opacity: {opacity_val};
}}""", language="css")

            with col2:
                st.markdown("#### 👁️ Live Preview")
                color_html = f"""<div style='background:{bg_style};color:{txt};opacity:{opacity_val};
                padding:24px;border-radius:12px;border:1px solid #1e2d45;'>
                <h3 style='color:{txt};margin:0 0 8px;'>Sample Card</h3>
                <p style='color:{txt};opacity:0.85;margin:0;line-height:1.6;'>
                This text shows how your color choices look together. Good contrast between
                background and text is essential for readability and accessibility.</p>
                <div style='margin-top:12px;background:rgba(255,255,255,0.1);padding:8px 12px;border-radius:6px;font-size:0.85rem;'>
                Nested element</div></div>"""
                st.markdown(color_html, unsafe_allow_html=True)

        elif css_topic == "Flexbox Layout":
            with col1:
                st.markdown("#### 🎛️ Flexbox Controls")
                st.markdown("""<div class='concept-box'><h4>Flexbox</h4>
                <p>Flexbox arranges items in a row or column. The parent gets <code>display:flex</code> and controls alignment. Children grow or shrink to fill space.</p></div>""", unsafe_allow_html=True)
                flex_dir = st.selectbox("flex-direction", ["row","column","row-reverse","column-reverse"])
                justify = st.selectbox("justify-content", ["flex-start","center","flex-end","space-between","space-around","space-evenly"])
                align = st.selectbox("align-items", ["stretch","flex-start","center","flex-end"])
                gap_val = st.slider("gap (px)", 0, 40, 12)
                n_items = st.slider("Number of items", 2, 6, 3)
                st.code(f""".container {{
  display: flex;
  flex-direction: {flex_dir};
  justify-content: {justify};
  align-items: {align};
  gap: {gap_val}px;
}}""", language="css")

            with col2:
                st.markdown("#### 👁️ Live Preview")
                items_html = "".join([
                    f"<div style='background:linear-gradient(135deg,#0ea5e9,#6366f1);color:white;padding:12px 16px;border-radius:8px;font-weight:600;font-size:0.85rem;'>Item {i+1}</div>"
                    for i in range(n_items)
                ])
                flex_html = f"""<div style='background:#0d1220;padding:20px;border-radius:12px;border:1px solid #1e2d45;min-height:180px;'>
                <div style='display:flex;flex-direction:{flex_dir};justify-content:{justify};align-items:{align};gap:{gap_val}px;min-height:140px;background:#080c14;border-radius:8px;padding:12px;'>
                {items_html}</div></div>"""
                st.markdown(flex_html, unsafe_allow_html=True)

        elif css_topic == "CSS Selectors":
            with col1:
                st.markdown("#### 🎯 Selector Types")
                st.markdown("""<div class='concept-box'><h4>How Selectors Work</h4>
                <p>Selectors tell CSS <b>which elements to style</b>. They range from simple (tag name) to powerful (combinations and pseudo-classes).</p></div>""", unsafe_allow_html=True)
                sel_type = st.radio("Selector type", [
                    "Element selector",
                    "Class selector (.class)",
                    "ID selector (#id)",
                    "Descendant selector",
                    "Pseudo-class (:hover)",
                    "Pseudo-element (::before)",
                ], label_visibility="collapsed")

                SEL_INFO = {
                    "Element selector": {
                        "syntax": "p { color: red; }",
                        "targets": "All <p> elements on the page",
                        "specificity": "0,0,1 — lowest priority",
                        "tip": "Avoid overusing element selectors — they affect everything globally."
                    },
                    "Class selector (.class)": {
                        "syntax": ".highlight { background: yellow; }",
                        "targets": 'All elements with class="highlight"',
                        "specificity": "0,1,0 — medium priority",
                        "tip": "Classes are reusable — the most common selector in real projects."
                    },
                    "ID selector (#id)": {
                        "syntax": "#header { font-size: 2rem; }",
                        "targets": 'Only the element with id="header"',
                        "specificity": "1,0,0 — high priority",
                        "tip": "IDs should be unique per page. Prefer classes for styling."
                    },
                    "Descendant selector": {
                        "syntax": "nav a { color: white; }",
                        "targets": "All <a> tags inside any <nav>",
                        "specificity": "0,0,2 — combined",
                        "tip": "Target elements based on their parent context without adding classes."
                    },
                    "Pseudo-class (:hover)": {
                        "syntax": "button:hover { background: blue; }",
                        "targets": "button when the mouse is over it",
                        "specificity": "0,1,1 — same as class+element",
                        "tip": "Also :focus, :active, :nth-child(n), :first-child, :last-child."
                    },
                    "Pseudo-element (::before)": {
                        "syntax": 'p::before { content: "→ "; }',
                        "targets": "A virtual element inserted before <p> content",
                        "specificity": "0,0,1 — same as element",
                        "tip": "::before and ::after require content: ''. Great for decorations without extra HTML."
                    },
                }
                info = SEL_INFO[sel_type]
                st.code(info["syntax"], language="css")
                st.markdown(f"""<div class='concept-box'>
                <h4>🎯 Targets</h4><p>{info['targets']}</p>
                <h4 style='margin-top:10px;'>📊 Specificity</h4><p>{info['specificity']}</p>
                <h4 style='margin-top:10px;'>💡 Tip</h4><p>{info['tip']}</p>
                </div>""", unsafe_allow_html=True)

            with col2:
                st.markdown("#### 📊 Specificity Calculator")
                st.markdown("""<div class='concept-box'><h4>The Specificity Hierarchy</h4>
                <p>When two rules target the same element, the one with higher specificity wins.
                <b>Inline styles</b> beat IDs, IDs beat classes, classes beat elements.</p></div>""", unsafe_allow_html=True)

                import matplotlib.pyplot as plt, matplotlib
                matplotlib.use("Agg")
                fig, ax = plt.subplots(figsize=(5, 3))
                fig.patch.set_facecolor('#0d1220')
                ax.set_facecolor('#080c14')
                categories = ['!important', 'Inline\nstyle', 'ID\n(#id)', 'Class\n(.class)', 'Element\n(p, div)']
                values = [10000, 1000, 100, 10, 1]
                colors = ['#f43f5e','#f97316','#fbbf24','#0ea5e9','#22c55e']
                bars = ax.barh(categories, values, color=colors, alpha=0.85)
                ax.set_xscale('log')
                ax.set_title("Specificity Weight (log scale)", color='#e2e8f0', fontsize=10)
                ax.tick_params(colors='#94a3b8', labelsize=9)
                for spine in ax.spines.values(): spine.set_edgecolor('#1e2d45')
                for bar, val in zip(bars, values):
                    ax.text(val * 1.3, bar.get_y() + bar.get_height()/2,
                            str(val), va='center', color='#e2e8f0', fontsize=8)
                plt.tight_layout()
                st.pyplot(fig)
                plt.close()

        elif css_topic == "Transitions & Animation":
            with col1:
                st.markdown("#### 🎛️ Animation Controls")
                st.markdown("""<div class='concept-box'><h4>CSS Transitions & Animations</h4>
                <p><b>Transitions</b> smoothly change a property when a state changes (like :hover).
                <b>Animations</b> run automatically using @keyframes.</p></div>""", unsafe_allow_html=True)
                anim_type = st.selectbox("Effect type", ["Fade In","Slide In","Pulse","Rotate","Bounce","Color Shift"])
                duration = st.slider("Duration (seconds)", 0.1, 3.0, 0.6)
                timing = st.selectbox("Timing function", ["ease","linear","ease-in","ease-out","ease-in-out"])

                ANIM_CODE = {
                    "Fade In":     f"@keyframes fadeIn {{\n  from {{ opacity: 0; }}\n  to {{ opacity: 1; }}\n}}\n.box {{\n  animation: fadeIn {duration}s {timing};\n}}",
                    "Slide In":    f"@keyframes slideIn {{\n  from {{ transform: translateX(-50px); opacity: 0; }}\n  to {{ transform: translateX(0); opacity: 1; }}\n}}\n.box {{\n  animation: slideIn {duration}s {timing};\n}}",
                    "Pulse":       f"@keyframes pulse {{\n  0%, 100% {{ transform: scale(1); }}\n  50% {{ transform: scale(1.15); }}\n}}\n.box {{\n  animation: pulse {duration}s {timing} infinite;\n}}",
                    "Rotate":      f"@keyframes rotate {{\n  from {{ transform: rotate(0deg); }}\n  to {{ transform: rotate(360deg); }}\n}}\n.box {{\n  animation: rotate {duration}s {timing} infinite;\n}}",
                    "Bounce":      f"@keyframes bounce {{\n  0%, 100% {{ transform: translateY(0); }}\n  50% {{ transform: translateY(-20px); }}\n}}\n.box {{\n  animation: bounce {duration}s {timing} infinite;\n}}",
                    "Color Shift": f"@keyframes colorShift {{\n  0% {{ background: #0ea5e9; }}\n  50% {{ background: #a78bfa; }}\n  100% {{ background: #f472b6; }}\n}}\n.box {{\n  animation: colorShift {duration}s {timing} infinite;\n}}",
                }
                st.code(ANIM_CODE[anim_type], language="css")

            with col2:
                st.markdown("#### 👁️ Live Preview")
                ANIM_STYLES = {
                    "Fade In":     f"animation:fadeIn {duration}s {timing};@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}",
                    "Slide In":    f"animation:slideIn {duration}s {timing};",
                    "Pulse":       f"animation:pulse {duration}s {timing} infinite;",
                    "Rotate":      f"animation:rotate {duration}s {timing} infinite;",
                    "Bounce":      f"animation:bounce {duration}s {timing} infinite;",
                    "Color Shift": f"animation:colorShift {duration}s {timing} infinite;",
                }
                anim_html = f"""
                <style>
                @keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
                @keyframes slideIn{{from{{transform:translateX(-50px);opacity:0}}to{{transform:translateX(0);opacity:1}}}}
                @keyframes pulse{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.15)}}}}
                @keyframes rotate{{from{{transform:rotate(0deg)}}to{{transform:rotate(360deg)}}}}
                @keyframes bounce{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-20px)}}}}
                @keyframes colorShift{{0%{{background:#0ea5e9}}50%{{background:#a78bfa}}100%{{background:#f472b6}}}}
                </style>
                <div style='background:#0d1220;padding:30px;border-radius:12px;border:1px solid #1e2d45;display:flex;align-items:center;justify-content:center;min-height:160px;'>
                  <div style='width:80px;height:80px;background:linear-gradient(135deg,#0ea5e9,#6366f1);border-radius:12px;
                  {ANIM_STYLES[anim_type]}'></div>
                </div>"""
                st.markdown(anim_html, unsafe_allow_html=True)
                st.markdown("""<div class='concept-box' style='margin-top:12px;'>
                <h4>💡 Performance Tip</h4>
                <p>Animate only <code>transform</code> and <code>opacity</code> for smooth 60fps animations.
                Animating <code>width</code>, <code>height</code>, or <code>margin</code> forces layout recalculations — very slow.</p>
                </div>""", unsafe_allow_html=True)

    # ── SUB-TOOL 3: JS Concepts Visualizer ──────────────────
    elif "JS" in sub_tool:

        st.markdown("""
        <div class='concept-box'>
            <h4>What is JavaScript?</h4>
            <p>JavaScript makes webpages <b>interactive and dynamic</b>. It runs in the browser and can
            respond to user actions, manipulate HTML, fetch data, and compute logic in real time.
            Pick a concept below to see it explained and visualized.</p>
        </div>
        """, unsafe_allow_html=True)

        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use("Agg")

        js_topic = st.selectbox("JS Topic", [
            "Variables & Data Types",
            "Functions & Scope",
            "Arrays & Methods",
            "DOM Manipulation",
            "Events & Callbacks",
            "Promises & Async/Await",
            "Objects & Classes",
        ])

        col1, col2 = st.columns([1, 1])

        JS_CONTENT = {
            "Variables & Data Types": {
                "concept": "JavaScript has 3 ways to declare variables: <b>var</b> (old, function-scoped), <b>let</b> (block-scoped, reassignable), and <b>const</b> (block-scoped, not reassignable). Data types include strings, numbers, booleans, null, undefined, objects, and arrays.",
                "code": """// Variable declarations
const name = "Alice";      // string
let age = 25;              // number
let isStudent = true;      // boolean
let nothing = null;        // null (intentionally empty)
let notDefined;            // undefined

// Type checking
console.log(typeof name);       // "string"
console.log(typeof age);        // "number"
console.log(typeof isStudent);  // "boolean"

// Template literals (modern string)
console.log(`Hi, I'm ${name}, age ${age}`);""",
                "quiz": ("What keyword declares a variable that CANNOT be reassigned?", "const"),
                "viz_type": "table"
            },
            "Functions & Scope": {
                "concept": "Functions are reusable blocks of code. <b>Scope</b> determines where variables are accessible. Variables declared inside a function are local to it — they can't be accessed outside.",
                "code": """// Function declaration
function greet(name) {
  const message = "Hello, " + name; // local scope
  return message;
}

// Arrow function (modern syntax)
const square = (n) => n * n;

// Scope example
let globalVar = "I'm global";

function test() {
  let localVar = "I'm local";
  console.log(globalVar); // ✅ works
  console.log(localVar);  // ✅ works
}
// console.log(localVar); // ❌ ReferenceError!""",
                "quiz": ("What is a variable that is only accessible inside the function that created it?", "local"),
                "viz_type": "scope"
            },
            "Arrays & Methods": {
                "concept": "Arrays store ordered lists of values. JavaScript provides powerful <b>higher-order array methods</b> like <code>map()</code>, <code>filter()</code>, and <code>reduce()</code> that transform arrays without loops.",
                "code": """const scores = [45, 82, 91, 37, 76, 88];

// .filter() — keep items matching condition
const passing = scores.filter(s => s >= 60);
// [82, 91, 76, 88]

// .map() — transform every item
const doubled = scores.map(s => s * 2);
// [90, 164, 182, 74, 152, 176]

// .reduce() — combine into single value
const total = scores.reduce((sum, s) => sum + s, 0);
// 419

// .sort() — sort in place
const sorted = [...scores].sort((a, b) => a - b);
// [37, 45, 76, 82, 88, 91]""",
                "quiz": ("Which array method returns a NEW array with only items that pass a test?", "filter"),
                "viz_type": "array"
            },
            "DOM Manipulation": {
                "concept": "The DOM (Document Object Model) is the browser's live tree of HTML elements. JavaScript can <b>select</b>, <b>modify</b>, <b>create</b>, and <b>delete</b> elements dynamically — without reloading the page.",
                "code": """// Select elements
const btn = document.getElementById("myBtn");
const items = document.querySelectorAll(".item");

// Change content & style
btn.textContent = "Click Me!";
btn.style.backgroundColor = "blue";

// Create & add new element
const newDiv = document.createElement("div");
newDiv.className = "card";
newDiv.textContent = "New card!";
document.body.appendChild(newDiv);

// Remove element
const old = document.querySelector(".old");
old.remove();

// Toggle CSS class
btn.classList.toggle("active");""",
                "quiz": ("Which method selects the first element matching a CSS selector?", "querySelector"),
                "viz_type": "dom"
            },
            "Events & Callbacks": {
                "concept": "Events are actions that happen in the browser — clicks, keypresses, form submissions. You <b>listen</b> for events with <code>addEventListener</code> and pass a <b>callback function</b> that runs when the event fires.",
                "code": """const button = document.getElementById("btn");

// Add event listener
button.addEventListener("click", function(event) {
  console.log("Button clicked!", event.target);
  event.target.style.color = "red";
});

// Arrow function callback
document.addEventListener("keydown", (e) => {
  console.log("Key pressed:", e.key);
});

// Common events:
// click, dblclick, mouseover, mouseout
// keydown, keyup, keypress
// submit, change, input, focus, blur
// scroll, resize, load""",
                "quiz": ("What method is used to attach an event listener to an element?", "addEventListener"),
                "viz_type": "events"
            },
            "Promises & Async/Await": {
                "concept": "JavaScript is <b>single-threaded</b> but handles async operations (fetching data, timers) using Promises. <code>async/await</code> is modern syntax that makes async code read like synchronous code.",
                "code": """// Old way — callback hell
fetch(url, function(data) {
  parse(data, function(parsed) {
    display(parsed);
  });
});

// Better — Promises
fetch("https://api.example.com/data")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));

// Best — async/await
async function loadData() {
  try {
    const response = await fetch("https://api.example.com/data");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Failed:", error);
  }
}""",
                "quiz": ("What keyword pauses async function execution until a Promise resolves?", "await"),
                "viz_type": "async"
            },
            "Objects & Classes": {
                "concept": "Objects group related data and functions together. <b>Classes</b> (ES6+) are blueprints for creating objects — they have <b>constructors</b>, <b>properties</b>, and <b>methods</b>, and support <b>inheritance</b>.",
                "code": """// Object literal
const student = {
  name: "Ali",
  grade: 90,
  greet() {
    return `Hi, I'm ${this.name}`;
  }
};

// Class
class Animal {
  constructor(name, sound) {
    this.name = name;
    this.sound = sound;
  }
  speak() {
    return `${this.name} says ${this.sound}!`;
  }
}

// Inheritance
class Dog extends Animal {
  constructor(name) {
    super(name, "Woof");
  }
  fetch() { return `${this.name} fetches the ball!`; }
}

const rex = new Dog("Rex");
rex.speak();  // "Rex says Woof!"
rex.fetch();  // "Rex fetches the ball!" """,
                "quiz": ("What keyword is used to inherit from a parent class?", "extends"),
                "viz_type": "class"
            }
        }

        content = JS_CONTENT[js_topic]

        with col1:
            st.markdown(f"""<div class='concept-box'>
            <h4>📖 {js_topic}</h4>
            <p>{content['concept']}</p></div>""", unsafe_allow_html=True)
            st.markdown("#### 📝 Code Example")
            st.code(content["code"], language="javascript")

        with col2:
            st.markdown("#### 📊 Visualization")

            if content["viz_type"] == "table":
                fig, ax = plt.subplots(figsize=(5, 3))
                fig.patch.set_facecolor('#0d1220')
                ax.set_facecolor('#0d1220')
                ax.axis('off')
                rows = [["const", "Block", "❌ No", "#f43f5e"],
                        ["let",   "Block", "✅ Yes", "#fbbf24"],
                        ["var",   "Function","✅ Yes","#64748b"]]
                headers = ["Keyword","Scope","Reassignable",""]
                for i, row in enumerate(rows):
                    for j, val in enumerate(row[:3]):
                        ax.text(j*0.33+0.05, 0.75 - i*0.25, val,
                               color=row[3], fontsize=11, va='center',
                               fontfamily='monospace' if j==0 else 'sans-serif')
                for j, h in enumerate(headers[:3]):
                    ax.text(j*0.33+0.05, 1.0, h, color='#94a3b8', fontsize=9,
                           va='center', fontweight='bold')
                ax.axhline(0.88, color='#1e2d45', linewidth=1)
                ax.set_xlim(0,1); ax.set_ylim(0,1.1)
                ax.set_title("Variable Keyword Comparison", color='#e2e8f0', fontsize=10)
                plt.tight_layout()
                st.pyplot(fig); plt.close()

            elif content["viz_type"] == "array":
                scores = [45, 82, 91, 37, 76, 88]
                passing = [s for s in scores if s >= 60]
                fig, axes = plt.subplots(1, 2, figsize=(6, 3))
                fig.patch.set_facecolor('#0d1220')
                colors_all = ['#f43f5e' if s < 60 else '#22c55e' for s in scores]
                for ax in axes: ax.set_facecolor('#0d1220'); ax.tick_params(colors='#94a3b8')
                for spine in axes[0].spines.values(): spine.set_edgecolor('#1e2d45')
                for spine in axes[1].spines.values(): spine.set_edgecolor('#1e2d45')
                axes[0].bar(range(len(scores)), scores, color=colors_all, alpha=0.85, width=0.6)
                axes[0].axhline(60, color='#fbbf24', linestyle='--', linewidth=1.5, label='Pass (60)')
                axes[0].set_title("Original scores", color='#e2e8f0', fontsize=9)
                axes[0].legend(fontsize=7, facecolor='#0d1220', labelcolor='#94a3b8')
                axes[1].bar(range(len(passing)), passing, color='#22c55e', alpha=0.85, width=0.6)
                axes[1].set_title("After .filter(s >= 60)", color='#e2e8f0', fontsize=9)
                plt.tight_layout()
                st.pyplot(fig); plt.close()

            elif content["viz_type"] == "async":
                fig, ax = plt.subplots(figsize=(5, 4))
                fig.patch.set_facecolor('#0d1220')
                ax.set_facecolor('#0d1220')
                ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
                ax.set_title("Async/Await Execution Flow", color='#e2e8f0', fontsize=10)
                steps = [
                    (1, 5.2, "Call async function", '#0ea5e9'),
                    (1, 4.0, "Hit await — pause here", '#fbbf24'),
                    (1, 2.8, "Other code runs...", '#94a3b8'),
                    (1, 1.6, "Promise resolves ✓", '#22c55e'),
                    (1, 0.4, "Resume after await", '#a78bfa'),
                ]
                for x, y, label, color in steps:
                    ax.add_patch(plt.Rectangle((x, y-0.35), 7, 0.7, color=color, alpha=0.2, zorder=1))
                    ax.add_patch(plt.Rectangle((x, y-0.35), 0.08, 0.7, color=color, alpha=0.9, zorder=2))
                    ax.text(x+0.3, y, label, color=color, fontsize=10, va='center')
                for i in range(len(steps)-1):
                    ax.annotate("", xy=(0.5, steps[i+1][1]+0.35),
                               xytext=(0.5, steps[i][1]-0.35),
                               arrowprops=dict(arrowstyle="->", color='#334155', lw=1.5))
                plt.tight_layout()
                st.pyplot(fig); plt.close()

            elif content["viz_type"] == "class":
                fig, ax = plt.subplots(figsize=(5, 4))
                fig.patch.set_facecolor('#0d1220')
                ax.set_facecolor('#0d1220')
                ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis('off')
                ax.set_title("Class Inheritance Chain", color='#e2e8f0', fontsize=10)
                boxes = [
                    (2, 5.5, 6, 1.0, "Animal (parent class)", '#0ea5e9'),
                    (2, 3.5, 6, 1.0, "Dog extends Animal", '#a78bfa'),
                    (1, 1.2, 3.5, 0.9, "rex = new Dog('Rex')", '#22c55e'),
                    (5.5, 1.2, 3.5, 0.9, "rex.speak()\nrex.fetch()", '#fbbf24'),
                ]
                for x, y, w, h, label, color in boxes:
                    ax.add_patch(plt.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                                facecolor=color+'33', edgecolor=color, linewidth=1.5))
                    ax.text(x+w/2, y+h/2, label, ha='center', va='center',
                           color=color, fontsize=8.5, fontweight='bold')
                ax.annotate("", xy=(5, 4.5), xytext=(5, 5.5),
                           arrowprops=dict(arrowstyle="->", color='#334155', lw=2))
                ax.text(5.1, 5.05, "extends", color='#64748b', fontsize=8)
                ax.annotate("", xy=(2.75, 2.1), xytext=(5, 3.5),
                           arrowprops=dict(arrowstyle="->", color='#334155', lw=1.5))
                ax.annotate("", xy=(7.25, 2.1), xytext=(5, 3.5),
                           arrowprops=dict(arrowstyle="->", color='#334155', lw=1.5))
                ax.text(4.5, 2.85, "new", color='#64748b', fontsize=8)
                plt.tight_layout()
                st.pyplot(fig); plt.close()

            else:
                event_flow = {
                    "scope": ["Global Scope", "Function Scope", "Block Scope (let/const)", "Closure"],
                    "dom":   ["document", "getElementById()", "querySelector()", "createElement()", "appendChild()"],
                    "events":["User Action", "Event Fires", "addEventListener()", "Callback Runs", "DOM Updates"],
                }
                key = content["viz_type"]
                items = event_flow.get(key, ["Step 1","Step 2","Step 3"])
                colors_map = ['#0ea5e9','#a78bfa','#22c55e','#fbbf24','#f472b6']
                fig, ax = plt.subplots(figsize=(5, 3.5))
                fig.patch.set_facecolor('#0d1220')
                ax.set_facecolor('#0d1220')
                ax.set_xlim(0,1); ax.set_ylim(-0.5, len(items))
                ax.axis('off')
                for i, item in enumerate(items):
                    y = len(items) - i - 1
                    c = colors_map[i % len(colors_map)]
                    ax.add_patch(plt.FancyBboxPatch((0.05, y-0.35), 0.9, 0.7,
                                boxstyle="round,pad=0.02", facecolor=c+'22', edgecolor=c, lw=1.5))
                    ax.text(0.5, y, item, ha='center', va='center', color=c, fontsize=10, fontweight='bold')
                    if i < len(items)-1:
                        ax.annotate("", xy=(0.5, y-0.35), xytext=(0.5, y-0.65),
                                   arrowprops=dict(arrowstyle="->", color='#334155', lw=1.5))
                ax.set_title(f"{js_topic} Flow", color='#e2e8f0', fontsize=10)
                plt.tight_layout()
                st.pyplot(fig); plt.close()

            st.markdown("#### 🧩 Quick Quiz")
            q, ans = content["quiz"]
            st.markdown(f"<div style='color:#fcd34d;font-size:0.9rem;font-weight:600;margin-bottom:6px;'>❓ {q}</div>", unsafe_allow_html=True)
            user_js = st.text_input("Your answer", key=f"jsquiz_{js_topic}", placeholder="Type keyword or method name...")
            if user_js:
                if user_js.strip().lower() in ans.lower() or ans.lower() in user_js.strip().lower():
                    st.success(f"✅ Correct! `{ans}` is right.")
                else:
                    st.error(f"❌ Not quite. The answer is `{ans}`.")

        # ── Score summary ──────────────────────────────────
        st.markdown("---")
        st.markdown("#### 📊 Topic Coverage")
        topics_covered = ["Variables & Data Types","Functions & Scope","Arrays & Methods",
                         "DOM Manipulation","Events & Callbacks","Promises & Async/Await","Objects & Classes"]
        html_topics = ["Headings (h1–h6)","Paragraph & Text","Lists (ul / ol)",
                      "Links & Images","Div & Semantic Tags","Forms & Inputs","Table"]
        css_topics = ["Box Model","Typography","Colors & Backgrounds",
                     "Flexbox Layout","CSS Selectors","Transitions & Animation"]
        total = len(topics_covered) + len(html_topics) + len(css_topics)
        cols = st.columns(3)
        cols[0].metric("HTML Topics", f"7")
        cols[1].metric("CSS Topics", f"6")
        cols[2].metric("JS Topics", f"7")
