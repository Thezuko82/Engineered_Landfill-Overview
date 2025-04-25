import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set Page Config
st.set_page_config(page_title="Engineered Landfill Simulator", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", [
    "Introduction",
    "Landfill Layers",
    "Design Guidelines",
    "Output Effluents",
    "Solute Transport Models",
    "Graphs and Figures"
])

# Introduction Section
if section == "Introduction":
    st.title("Engineered Landfill: Overview")
    st.markdown("""
        Engineered landfills are specially designed sites for the safe disposal of solid waste. They are constructed using multiple layers 
        of protective materials to minimize environmental impact. Key functions include:
        - Containment of waste
        - Control of leachate and gas
        - Prevention of groundwater contamination
        - Monitoring and long-term stability
    """)
    st.markdown("Paper Link - https://link.springer.com/chapter/10.1007/978-981-97-3823-6_10")

# Layers Section
elif section == "Landfill Layers":
    st.title("Landfill Layers and Properties")

    layers = {
        "Cover Layer": "Prevents water infiltration and controls gas emissions.",
        "Drainage Layer": "Facilitates leachate removal.",
        "Solid Waste": "Decomposing municipal solid waste.",
        "Geosynthetic Layer": "Includes geomembranes for impermeability.",
        "Geosynthetic Clay Liner (GCL)": "Provides low permeability using bentonite clay.",
        "Liner System": "Composite barrier to prevent leachate migration."
    }

    for layer, desc in layers.items():
        st.subheader(layer)
        st.markdown(f"**Function**: {desc}")
        st.markdown(f"**Typical Thickness**: {np.random.uniform(0.2, 1.0):.2f} m")
        st.markdown(f"**Permeability (k)**: {10**-np.random.randint(7, 10)} m/s")
        st.markdown("---")

# Design Guidelines Section
elif section == "Design Guidelines":
    st.title("Design Guidelines for Engineered Landfill")
    st.markdown("""
    Design considerations:
    - Minimum slope for drainage: 3%-5%
    - Leachate collection: Must maintain < 30 cm head over liner
    - Liner permeability: < 1 x 10⁻⁹ m/s
    - Stability: Analysis for slope stability, settlement
    - Gas management: Passive or active systems
    """)

# Output Effluents Section
elif section == "Output Effluents":
    st.title("Output Effluents")

    st.markdown("""
        The main outputs from a landfill include:
        - **Leachate**: A liquid that extracts dissolved and suspended materials from the waste.
        - **Landfill Gas (LFG)**: Contains methane, CO₂, and trace gases.
    """)
    
    leachate_data = pd.DataFrame({
        'Constituent': ['BOD', 'COD', 'Ammonia', 'Heavy Metals'],
        'Typical Concentration (mg/L)': [3000, 8000, 1200, 5]
    })
    st.dataframe(leachate_data)

# Solute Transport Models Section
elif section == "Solute Transport Models":
    st.title("Solute Transport Models")
    st.markdown(r"""
        Several models describe the transport of contaminants through landfill liners:

        - **Advection-Dispersion Equation (ADE)**:  
        $$ \frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2} - v \frac{\partial C}{\partial x} $$

        - **First-Order Decay**:  
        $$ \frac{dC}{dt} = -kC $$

        - **Sorption Isotherms**:  
        $$ q = K_d C $$ (Linear),  
        $$ q = K_f C^n $$ (Freundlich)

        - **Barrier Diffusion (Through GCL)**:  
        $$ J = -D \frac{\partial C}{\partial x} $$
        """, unsafe_allow_html=True)


# Graphs and Figures Section
elif section == "Graphs and Figures":
    st.title("Graphs and Figures")
    st.markdown("### 1. Concentration vs Distance (ADE Model)")
    
    # User inputs
    v = st.sidebar.slider("Velocity (m/day)", 0.1, 10.0, 1.0)
    D = st.sidebar.slider("Dispersion Coefficient (m²/day)", 0.1, 5.0, 1.0)
    L = st.sidebar.slider("Distance (m)", 1, 50, 10)
    t = st.sidebar.slider("Time (days)", 1, 100, 10)

    x = np.linspace(0, L, 200)
    C = (1 / (2 * np.sqrt(np.pi * D * t))) * np.exp(-((x - v*t)**2) / (4 * D * t))

    fig, ax = plt.subplots()
    ax.plot(x, C)
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Concentration (mg/L)")
    ax.set_title("Contaminant Concentration over Distance")
    st.pyplot(fig)

    st.markdown("### 2. External Resources")
    st.markdown("![Landfill Structure](https://www.geoengineer.org/storage/wcp_assignment/177/editor_photos/4273/Fig1.jpg)")
    st.markdown("![Liner System](https://ars.els-cdn.com/content/image/3-s2.0-B9780750679633500114-f09-01-9780750679633.jpg)")

st.sidebar.markdown("---")
st.sidebar.markdown("**Developed by:** Rohit Maurya")
