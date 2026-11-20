# 🌐 Roboldo-Orbit — Controlador Geral & Orquestrador Central

Repositório oficial do **Orbit**, o controlador geral, orquestrador de módulos (Core / Shell / HAL) e SDK de integração do robô social **Roboldo** (**LAR / UERN**).

---

## 🎯 Papel no Ecossistema

O **Orbit** atua como o núcleo central que coordena a comunicação entre todos os subsistemas do Roboldo:
- **HAL (Hardware Abstraction Layer)**: Ponte unificada com o [`Roboldo-IoT-Firmware`](https://github.com/ROBOLDO-UERN/Roboldo-IoT-Firmware) e [`Controlador-Roboldo`](https://github.com/ROBOLDO-UERN/Controlador-Roboldo).
- **Orquestração de IA, Voz & SLAM**: Integração de eventos com [`Roboldo-IA-Movimento`](https://github.com/ROBOLDO-UERN/Roboldo-IA-Movimento) e [`Roboldo-Display-Nextion`](https://github.com/ROBOLDO-UERN/Roboldo-Display-Nextion).
- **Gerenciador de Ciclo de Vida & SDK**: Shell, Launcher e API para execução dos jogos e aplicativos em Flutter do [`Roboldo-Base`](https://github.com/ROBOLDO-UERN/Roboldo-Base).

---

## 👥 Equipes Responsáveis (`CODEOWNERS`)

- **Zonas Vinculadas**: `@ROBOLDO-UERN/zona-gamificacao-apps` & `@ROBOLDO-UERN/zona-mecanica-hardware`
- **Coordenação & Revisão**: `@ROBOLDO-UERN/professores` & `@ROBOLDO-UERN/bolsistas`
- **Acompanhamento de Tasks**: [📋 Painel Geral da Organização (Project #6)](https://github.com/orgs/ROBOLDO-UERN/projects/6) | [📋 Project Zona 5](https://github.com/orgs/ROBOLDO-UERN/projects/5)

---

## 📂 Estrutura de Diretórios

```text
Roboldo-Orbit/
├── core/              # Orquestrador central, barramento de eventos e gerenciamento de estado
├── hal/               # Camada de Abstração de Hardware (Serial, WebSocket, MQTT, Bluetooth)
├── sdk/               # Especificação e cliente do Roboldo SDK para Apps e Jogos
├── docs/              # Diagramas arquiteturais e contratos de API
└── tests/             # Testes integrados do controlador geral
```
