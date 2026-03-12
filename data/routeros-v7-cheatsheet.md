# RouterOS v7 Cheat Sheet & Troubleshooting

## 1. Interface Management
- **Set MTU:**
  To change MTU on an interface (e.g., ether1), use the `/interface` menu directly. OSPF uses interface MTU.
  ` /interface ethernet set [find name=ether1] mtu=1500 `
  ` /interface vlan set [find name=vlan10] mtu=1450 `

## 2. OSPF v7 Configuration (Backbone Area 0)
RouterOS v7 uses a hierarchical structure: Instance -> Area -> Interface-Template.
Do NOT use `network` command under `routing ospf`.

- **Basic Config:**
  ```bash
  /routing/ospf/instance/add name=default-v2 version=2 router-id=10.0.0.1
  /routing/ospf/area/add name=backbone-v2 instance=default-v2 area-id=0.0.0.0
  /routing/ospf/interface-template/add area=backbone-v2 networks=10.0.0.0/30
  ```

- **Check Neighbor Status:**
  ` /routing/ospf/neighbor/print `
  If state is `ExStart` or `Exchange` then `Down`, check **MTU Mismatch**.

- **Troubleshooting MTU Mismatch:**
  Error: `MTU mismatch (received: 1500, configured: 1450)`
  Solution: Match the interface MTU on both sides.
  ` /interface ethernet set [find name=ether1] mtu=1500 `
  (Do NOT use `ip ospf mtu-ignore` unless absolutely necessary, as it breaks topology database exchange).

## 3. BGP v7 Configuration
RouterOS v7 uses `connection` instead of `peer`.

- **Basic eBGP Session:**
  ```bash
  /routing/bgp/connection/add name=peer1 remote.address=192.168.1.2 .as=65002 local.role=ebgp templates=default
  ```
- **Check BGP Sessions:**
  ` /routing/bgp/session/print `

## 4. System & Logging
- **Check Logs:**
  ` /log print where topics~"ospf" `
  ` /log print follow `
