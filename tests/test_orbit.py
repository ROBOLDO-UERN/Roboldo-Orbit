from core.orbit_controller import OrbitController


def test_orbit_initialization():
    orbit = OrbitController()
    assert "iot_firmware" in orbit.subsystems
    assert "ia_movimento" in orbit.subsystems
