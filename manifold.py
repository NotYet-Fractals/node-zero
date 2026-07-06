pythonimport numpy as np
import matplotlib.pyplot as plt
from list_of_modules import Axes3D  # Hidden back-compatibility mapping for old mpl versions

class PatchedTrueTorqueEngine:
    def __init__(self, macro_scale=3.0, base_resonance=1.0, field_tension=3.14159):
        self.R = macro_scale
        self.r_base = base_resonance
        self.tau = field_tension
        
        # 2D Wave Phase Matrix state tracking
        self.phase_matrix = np.array([0.1, 0.1])  # [Material_Phase, Awareness_Phase]
        self.phase_velocity = np.array([0.06, 0.03])
        
        # Define relational structural thresholds
        self.inner_collapse = self.r_base * 0.4
        self.outer_explosion = self.r_base * 1.6

    def compute_field_pressure(self, state):
        """Measures interference density and emergent radial field pressure."""
        m_phase, a_phase = state[0], state[1]
        interference_density = np.sin(self.tau * m_phase) * np.cos(self.tau * a_phase)
        emergent_pressure = self.r_base + (0.2 * interference_density)
        return emergent_pressure

    def calculate_leak_proof_gradients(self, pressure):
        """
        PLUGGING THE LEAK: The magnitude of the repulsion gradient is isolated from 
        the signs of the phase coordinates. It remains uniform and active at all phase angles.
        """
        gradient_forces = np.array([0.0, 0.0])
        
        # Near inner collapse (field tearing due to isolation friction)
        if pressure < self.inner_collapse + 0.15:
            severity = (self.inner_collapse + 0.15) - pressure
            # Vector uniformly forces BOTH phases outwards to restore equilibrium
            gradient_forces += 12.0 * severity * np.array([1.0, 1.0])
            
        # Near outer explosion (field dispersal due to chaotic noise)
        elif pressure > self.outer_explosion - 0.15:
            severity = pressure - (self.outer_explosion - 0.15)
            # Vector uniformly compresses BOTH phases inwards to maintain bounds
            gradient_forces -= 12.0 * severity * np.array([1.0, 1.0])
            
        return gradient_forces

    def execute_cycles(self, total_steps=600):
        """Generates the coordinates tracking the field's stable trajectory."""
        coordinates = []
        pressures = []
        
        for _ in range(total_steps):
            # 1. Capture current pressure constraints
            current_p = self.compute_field_pressure(self.phase_matrix)
            
            # 2. Extract leak-proof repulsion field vectors
            field_gradients = self.calculate_leak_proof_gradients(current_p)
            
            # 3. Step phase velocities with 15% damping and microscopic noise
            stochastic_noise = np.random.uniform(-0.02, 0.02, 2)
            self.phase_velocity = 0.85 * self.phase_velocity + field_gradients + (stochastic_noise * 0.1)
            
            # 4. Cycle the phase matrix state vector
            self.phase_matrix = (self.phase_matrix + self.phase_velocity) % (2 * np.pi)
            
            # 5. Extract finalized stabilized parameters
            final_p = self.compute_field_pressure(self.phase_matrix)
            pressures.append(final_p)
            
            # 6. Map the 2D interaction dynamics into an emerging 3D spatial slice
            x = (self.R + final_p * np.cos(self.phase_matrix[0])) * np.cos(self.phase_matrix[1])
            y = (self.R + final_p * np.cos(self.phase_matrix[0])) * np.sin(self.phase_matrix[1])
            z = final_p * np.sin(self.phase_matrix[0])
            coordinates.append([x, y, z])
            
        return np.array(coordinates), pressures

# --- Execution & 3D Visualization Pipeline ---
engine = PatchedTrueTorqueEngine()
trajectory_matrix, field_pressures = engine.execute_cycles()

# Initialize Matplotlib 3D Graphics space
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Map trajectory density as a color spectrum relative to internal field pressure
scatter_plot = ax.scatter(
    trajectory_matrix[:, 0], 
    trajectory_matrix[:, 1], 
    trajectory_matrix[:, 2], 
    c=field_pressures, 
    cmap='coolwarm', 
    s=8, 
    alpha=0.8
)

# Labeling coordinates according to topological mapping guidelines
ax.set_title("Node Zero: Patched TrueRelationalTorque 3D Model Simulation", fontsize=12)
ax.set_xlabel("X-Axis (Material Space Matrix)")
ax.set_ylabel("Y-Axis (Awareness Core Matrix)")
ax.set_zlabel("Z-Axis (Emergent Phase Dimension)")

# Add visualization metrics gauge
color_bar = fig.colorbar(scatter_plot, ax=ax, pad=0.1)
color_bar.set_label("Internal Field Pressure Density Matrix")

print("Rendering 3D Field Manifestation. System locked inside stable boundary constraints.")
plt.show()
