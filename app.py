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

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}
code, pre, .stCode {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Dark base */
.stApp { background-color: #080c14; }
section[data-testid="stSidebar"] { background-color: #0d1220; border-right: 1px solid #1e2d45; }

/* Hide default streamlit elements */
#MainMenu, footer, header { visibility: hidden; }

/* Sidebar level cards */
.level-card {
    padding: 10px 14px;
    border-radius: 8px;
    margin-bottom: 8px;
    cursor: pointer;
    border: 1px solid transparent;
    transition: all 0.2s;
}
.level-card:hover { border-color: #00d4ff33; }

/* Page title */
.page-hero {
    text-align: center;
    padding: 40px 0 20px 0;
}
.page-hero h1 {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #00d4ff, #a78bfa, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.3rem;
}
.page-hero p {
    color: #64748b;
    font-size: 1.1rem;
}

/* Tool containers */
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
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.05em;
}
.concept-box {
    background: #0d1220;
    border: 1px solid #1e2d45;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
}
.concept-box h4 { color: #00d4ff; margin-top: 0; }
.concept-box p { color: #94a3b8; line-height: 1.6; }

/* Neuron styles for L1 */
.neuron-row { display: flex; justify-content: center; gap: 20px; margin: 10px 0; }

/* Metric cards */
.metric-row { display: flex; gap: 12px; margin: 16px 0; }
.metric-card {
    flex: 1;
    background: #0d1220;
    border: 1px solid #1e2d45;
    border-radius: 10px;
    padding: 16px;
    text-align: center;
}
.metric-card .val { font-size: 1.8rem; font-weight: 800; color: #00d4ff; }
.metric-card .lbl { font-size: 0.75rem; color: #64748b; margin-top: 4px; }

/* Step pipeline */
.pipeline { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin: 16px 0; }
.pipe-step {
    background: #0d1220;
    border: 1px solid #1e2d45;
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 0.85rem;
    color: #e2e8f0;
    position: relative;
}
.pipe-step.active { border-color: #00d4ff; color: #00d4ff; box-shadow: 0 0 12px #00d4ff22; }
.pipe-arrow { color: #334155; font-size: 1.2rem; }

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #0ea5e9, #6366f1) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.85 !important; }

/* Sliders */
.stSlider > div > div > div { background: #00d4ff !important; }

/* Selectbox */
.stSelectbox > div > div { background: #0d1220 !important; border-color: #1e2d45 !important; color: #e2e8f0 !important; }

/* Info boxes */
.stInfo { background: #0d1a2e !important; border-color: #0ea5e933 !important; }
.stSuccess { background: #0d2e1a !important; border-color: #22c55e33 !important; }
.stWarning { background: #2e1f0d !important; border-color: #f59e0b33 !important; }
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
