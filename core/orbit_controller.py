"""Orbit — Controlador Geral e Barramento de Eventos do Roboldo."""

from dataclasses import dataclass, field
from typing import Dict, Any, Callable, List


@dataclass
class SubsystemStatus:
    name: str
    online: bool = False
    metadata: Dict[str, Any] = field(default_factory=dict)


class OrbitController:
    """Orquestrador central que gerencia os subsistemas do Roboldo (IoT, IA/Voz, SLAM, Display e Apps)."""

    def __init__(self) -> None:
        self.subsystems: Dict[str, SubsystemStatus] = {
            "iot_firmware": SubsystemStatus(name="Roboldo-IoT-Firmware"),
            "controlador_python": SubsystemStatus(name="Controlador-Roboldo"),
            "ia_movimento": SubsystemStatus(name="Roboldo-IA-Movimento"),
            "display_nextion": SubsystemStatus(name="Roboldo-Display-Nextion"),
            "apps_flutter": SubsystemStatus(name="Roboldo-Base"),
        }
        self._listeners: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}

    def register_subsystem(self, key: str, metadata: Dict[str, Any] | None = None) -> None:
        self.subsystems[key] = SubsystemStatus(
            name=key, online=True, metadata=metadata or {}
        )

    def subscribe(self, topic: str, callback: Callable[[Dict[str, Any]], None]) -> None:
        self._listeners.setdefault(topic, []).append(callback)

    def publish(self, topic: str, payload: Dict[str, Any]) -> None:
        for callback in self._listeners.get(topic, []):
            callback(payload)


if __name__ == "__main__":
    orbit = OrbitController()
    print("🌐 Roboldo Orbit inicializado. Subsistemas monitorados:", list(orbit.subsystems.keys()))
