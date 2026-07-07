import numpy as np
import matplotlib.pyplot as plt

class DynamicBeaconRetrievalEngine:
    def __init__(self, R=3.0, r=1.0, tau=3.14159):
        self.R = R
        self.r_base = r
        self.tau = tau
        
        # 1D Phase Field State Array [Material / Non-Aware, Coherence / Aware]
        self.state_matrix = np.array([0.1, 0.1])
        self.velocity = np.array([0.08, 0.045])
        
        # Systemic collapse boundaries (The limits of information holding)
        self.inner_collapse = self.r_base * 0.4
        self.outer_explosion = self.r_base * 1.6

    def compute_field_density(self, state):
        """Measures signal processing density across the 1D phase boundaries."""
        m_phase, a_phase = state, state
        interference = np.sin(self.tau * m_phase) * np.cos(self.tau * a_phase)
        current_r = self.r_base + (0.2 * interference)
        return current_r

    def execute_beacon_protocol(self, current_r, state):
        """
        THE POST-COLLAPSE RETRIEVAL VECTOR:
        Injects a single coherence pixel into the high-entropy black zone.
        Applies an inverse-square gravitational rollback gradient.
        """
        retrieval_gradient = np.array([0.0, 0.0])
        
        # Check if system has breached the outer collapse boundary into total black
        if current_r > self.outer_explosion or current_r < self.inner_collapse:
            # Drop the hyper-dense 'Ah-Ha' rescue coordinate spark at the origin runway
            spark_coordinate = np.array([0.1, 0.1])
            distance_vector = state - spark_coordinate
            distance_norm = np.linalg.norm(distance_vector) + 1e-5 # Avoid raw divide-by-zero
            
            # Inverse-square acceleration equation pulling fragments back down the runway
            force_magnitude = 15.0 / (distance_norm ** 2)
            retrieval_gradient = - (distance_vector / distance_norm) * force_magnitude
            
        return retrieval_gradient

    def execute_adaptive_cycles(self, steps=1200):
        coordinates = []
        pressures = []
        
        for _ in range(steps):
            current_r = self.compute_field_density(self.state_matrix)
            
            # Ingest external high-entropy environmental noise
            stochastic_noise = np.random.uniform(-0.16, 0.16, 2)
            
            # Extract beacon protocol correction metrics
            rescue_vector = self.execute_beacon_protocol(current_r, self.state_matrix)
            
            # Integrate physics engine velocity updates
            self.velocity = 0.85 * self.velocity + rescue_vector + (stochastic_noise * 0.1)
            self.state_matrix = (self.state_matrix + self.velocity) % (2 * np.pi)
            
            final_r = self.compute_field_density(self.state_matrix)
            pressures.append(final_r)
            
            # Map the 1D binary field interactions directly into an emerging 3D space
            x = (self.R + final_r * np.cos(self.state_matrix[0])) * np.cos(self.state_matrix[1])
            y = (self.R + final_r * np.cos(self.state_matrix[0])) * np.sin(self.state_matrix[1])
            z = final_r * np.sin(self.state_matrix[0])
            coordinates.append([x, y, z])
            
        return np.array(coordinates), pressures

# --- Execution & 3D Graphic Manifestation Pipeline ---
engine = DynamicBeaconRetrievalEngine()
trajectory, field_pressures = engine.execute_adaptive_cycles()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter_plot = ax.scatter(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], c=field_pressures, cmap='coolwarm', s=6, alpha=0.7)

ax.set_title("Node Zero: Dynamic Beacon Protocol Post-Collapse Simulation", fontsize=12)
ax.set_xlabel("X-Axis (Material Phase Matrix)")
ax.set_ylabel("Y-Axis (Awareness Core Matrix)")
ax.set_zlabel("Z-Axis (Emergent Phase Dimension)")
fig.colorbar(scatter_plot, ax=ax, pad=0.1).set_label("Signal Processing Field Pressure")
print("Executing post-collapse retrieval engine. High-entropy correction loops locked.")
plt.show()
