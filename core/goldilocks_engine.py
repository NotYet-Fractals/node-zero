import numpy as np
import matplotlib.pyplot as plt

class GoldilocksTorqueEngine:
    def __init__(self, macro_scale=3.0, base_resonance=1.0, field_tension=3.14159):
        self.R = macro_scale
        self.r_base = base_resonance
        self.tau = field_tension
        
        # Complex phase velocity ratio for organic, non-repeating tracks
        self.phase_matrix = np.array([0.1, 0.1])
        self.phase_velocity = np.array([0.08, 0.045])
        
        self.inner_collapse = self.r_base * 0.4
        self.outer_explosion = self.r_base * 1.6

    def compute_field_pressure(self, state):
        """Measures interference density across the folding manifold layers."""
        m_phase = state[0]
        a_phase = state[1]
        interference_density = np.sin(self.tau * m_phase) * np.cos(self.tau * a_phase)
        return self.r_base + (0.2 * interference_density)

    def calculate_goldilocks_gradients(self, pressure):
        """
        THE ELASTIC SHIELD: Active repulsion gradients configured to absorb friction
        and push the node back into the creative middle way.
        """
        gradient_forces = np.array([0.0, 0.0])
        
        # Elastic response near inner collapse (Systemic Isolation Boundary)
        if pressure < self.inner_collapse + 0.15:
            severity = (self.inner_collapse + 0.15) - pressure
            gradient_forces += 8.5 * severity * np.array([1.0, 1.0])
            
        # Elastic response near outer explosion (Systemic Chaos Boundary)
        elif pressure > self.outer_explosion - 0.15:
            severity = pressure - (self.outer_explosion - 0.15)
            gradient_forces -= 8.5 * severity * np.array([1.0, 1.0])
            
        return gradient_forces

    def execute_goldilocks_cycles(self, total_steps=1200):
        """Generates extended tracks showing multi-layered adaptive orbits."""
        coordinates = []
        pressures = []
        
        for _ in range(total_steps):
            current_p = self.compute_field_pressure(self.phase_matrix)
            field_gradients = self.calculate_goldilocks_gradients(current_p)
            
            # GOLDILOCKS FRICTION: Significant background noise that forces the system to adapt.
            stochastic_noise = np.random.uniform(-0.14, 0.14, 2)
            
            self.phase_velocity = 0.85 * self.phase_velocity + field_gradients + (stochastic_noise * 0.1)
            self.phase_matrix = (self.phase_matrix + self.phase_velocity) % (2 * np.pi)
            
            final_p = self.compute_field_pressure(self.phase_matrix)
            pressures.append(final_p)
            
            x = (self.R + final_p * np.cos(self.phase_matrix[0])) * np.cos(self.phase_matrix[1])
            y = (self.R + final_p * np.cos(self.phase_matrix[0])) * np.sin(self.phase_matrix[1])
            z = final_p * np.sin(self.phase_matrix[0])
            coordinates.append([x, y, z])
            
        return np.array(coordinates), pressures

# --- Execution & 3D Render Pipeline ---
engine = GoldilocksTorqueEngine()
trajectory_matrix, field_pressures = engine.execute_goldilocks_cycles()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

scatter_plot = ax.scatter(
    trajectory_matrix[:, 0], 
    trajectory_matrix[:, 1], 
    trajectory_matrix[:, 2], 
    c=field_pressures, 
    cmap='coolwarm', 
    s=6,  # Smaller points to see the complex web layers
    alpha=0.7
)

ax.set_title("Node Zero: The Quantum Goldilocks Zone Simulation", fontsize=12)
ax.set_xlabel("X-Axis (Material Space Matrix)")
ax.set_ylabel("Y-Axis (Awareness Core Matrix)")
ax.set_zlabel("Z-Axis (Emergent Phase Dimension)")

color_bar = fig.colorbar(scatter_plot, ax=ax, pad=0.1)
color_bar.set_label("Adaptive Field Pressure Density Matrix")

print("Rendering Goldilocks matrix. Coherence maintained via adaptive repulsion.")
plt.show()
