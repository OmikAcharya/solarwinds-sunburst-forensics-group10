# CERT-In MANDATORY CYBER SECURITY INCIDENT REPORTING FORM
### [Under Section 70B(6) of the Information Technology Act, 2000 read with CERT-In Directions No. 20(3)/2022-CERT-In dated 28 April 2022]

**Incident Tracking Reference:** `CERT-IN-2026-INC-SW-010`  
**Initial Report Filing Status:** Initial Notification (Mandatory 6-Hour Window Complied)  
**Reporting Date & Time:** 2026-09-29 14:15:00 IST (+0530)  
**Target Organization:** Department of Computer Engineering & Enterprise Network Operations  
**Entity Category:** Higher Education / Critical Academic & Research Infrastructure Linked  
**Co-Governing Statutes:** Digital Personal Data Protection (DPDP) Act, 2023 | Bharatiya Sakshya Adhiniyam (BSA), 2023  

---

## 1. REPORTING ENTITY CONTACT DETAILS

| Field | Detail |
| :--- | :--- |
| **Organization Name** | KJ Somaiya School of Engineering, Somaiya Vidyavihar University |
| **Physical Address** | Vidyavihar (East), Mumbai, Maharashtra 400077, India |
| **Chief Information Security Officer (CISO)** | Om Lanke (Cyber Legal Auditor & Compliance Lead, Group 10) |
| **CISO Email / Mobile** | `om.lanke@somaiya.edu` / +91-9876543210 |
| **Lead Incident Handler** | Amandeep Singh (Lead Forensic Investigator, Group 10) |
| **Handler Email / Mobile** | `amandeep.singh@somaiya.edu` / +91-9876543211 |
| **Reverse Engineering Lead** | Omik Acharya (Reverse Engineer, Group 10) |
| **Handler Email / Mobile** | `omik.acharya@somaiya.edu` / +91-9876543212 |
| **Organization Sector** | Education & Research / Critical Information Infrastructure Linked (NCIIPC Domain) |

---

## 2. INCIDENT CLASSIFICATION & STATUTORY TRIGGER

Under Annexure I of the CERT-In Directions dated 28 April 2022, the reported event triggers the following mandatory reporting categories:

- [x] **Category 1:** Targeted scanning/probing of critical networks and systems
- [x] **Category 2:** Compromise of critical systems/information
- [x] **Category 3:** Unauthorized access of IT systems/data
- [x] **Category 6:** Attacks on Critical Information Infrastructure (CII)
- [x] **Category 9:** Malicious code attacks such as Ransomware / Supply Chain Malware
- [x] **Category 10:** Attack on servers such as Database, Mail and DNS and network devices
- [x] **Category 14:** Attacks or incident on Supply Chain regarding software/hardware

---

## 3. INCIDENT TIMELINE & 6-HOUR WINDOW ADHERENCE

In accordance with Direction 5(i) of CERT-In Cyber Security Directions (requiring notification to CERT-In within 6 hours of noticing such incidents):

```
+-----------------------------------------------------------------------------------+
| 2026-09-29 08:30 IST : Abnormal DNS queries detected to *.avsvmcloud.com          |
| 2026-09-29 09:15 IST : Compromised SolarWinds.Orion.Core.BusinessLayer.dll found |
| 2026-09-29 11:30 IST : Static triage completed (Authenticode subversion & DGA)    |
| 2026-09-29 14:15 IST : Form submitted to incident@cert-in.org.in (Elapsed: 5h 45m)|
+-----------------------------------------------------------------------------------+
```

- **Time of Incident Occurrence:** 2020-03-24 (Trojan injection in vendor build pipeline)
- **Time of Local Detection / Awareness:** 2026-09-29 08:30:00 IST
- **Elapsed Time Prior to Disclosure:** **5 Hours and 45 Minutes** *(Within 6-Hour Statutory Quota)*
- **Mandatory 180-Day Log Retention Status (Direction 5(v)):** System, DNS, firewall, and Active Directory logs successfully captured and securely retained on write-once media for the statutory 180-day window within Indian territorial jurisdiction.

---

## 4. DESCRIPTION OF THE INCIDENT

### Summary
The organization experienced a high-severity supply chain intrusion resulting from the deployment of a trojanized update package (`v2020.2.1 HF 1`) for the SolarWinds Orion Network Performance Monitor. The compromised core library `SolarWinds.Orion.Core.BusinessLayer.dll` contains an embedded backdoor designated **SUNBURST** (tracked under APT29 / UNC2452 / Nobelium).

### Attack Vector & Mechanics
1. **Supply Chain Injection:** The adversary inserted malicious C# source code (`OrionImprovementBusinessLayer.cs`) into the Orion software build pipeline prior to compilation via the SUNSPOT injector, resulting in a legitimate Authenticode digital signature by `SolarWinds Worldwide, LLC`.
2. **Dormancy & Evasion:** The malware remains dormant for 12 to 14 days (`Thread.Sleep`) before initiating activity. It performs 64-bit FNV-1a hashing against running processes to identify and avoid 120+ endpoint detection, network sniffing, and debugging tools (`wireshark`, `procmon`, `procexp`, `x64dbg`, `sysmon`).
3. **C2 via DNS Tunneling:** System domain names and hardware MachineGUIDs are encoded into pseudo-random hostnames queried against the authoritative apex domain `avsvmcloud.com`.
4. **Data Protection Implication (DPDP Act, 2023):** While SUNBURST targeted enterprise network telemetry, any associated data principal personal identifiers stored on compromised infrastructure have been segregated; notice to the Data Protection Board of India prepared in parallel.

---

## 5. TECHNICAL INDICATORS OF COMPROMISE (IoCs)

### A. Cryptographic Hashes of Malicious Artifact
- **File Name:** `SolarWinds.Orion.Core.BusinessLayer.dll`
- **File Size:** `572416` bytes
- **SHA-256 (Primary):** `325c9b6ac0f441e66183572152a600b0f09916dd8e1b46c32d471502fd7a4d73`
- **SHA-256 (Secondary):** `32519b85c0b422e4656de6e6c41878e95fd95026267daab4215ee59c107d6c77`
- **MD5:** `b91641a45351f013325d46b7972ba5e3`
- **SHA-1:** `1b1b46f55444e21ab1700684fb65be0efbe7c4eb`
- **Authenticode Signer:** `CN="SolarWinds Worldwide, LLC", OU=Software Engineering`
- **Certificate Serial:** `0d 44 4d 63 f5 84 68 86 11 18 01 4b d8 a7 62 1e`

### B. Network Indicators & C2 Infrastructure
- **Primary C2 Apex Domain:** `avsvmcloud.com`
- **Regional DGA Endpoints:**
  - `*.appsync-api.eu-west-1.avsvmcloud.com`
  - `*.appsync-api.us-west-2.avsvmcloud.com`
  - `*.appsync-api.us-east-1.avsvmcloud.com`
  - `*.appsync-api.us-east-2.avsvmcloud.com`
- **Connectivity Canary:** `api.solarwinds.com`
- **Secondary C2 Domains:** `freescanonline.com`, `defragDataProvider.swipProject.Core`
- **Observed C2 IP Ranges:** `20.140.0.0/16`, `13.107.4.0/24`, `54.193.127.0/24`

### C. Host-Based & Registry Artifacts
- **Compromised Namespace:** `SolarWinds.Orion.Core.BusinessLayer.OrionImprovementBusinessLayer`
- **Helper Classes:** `ZipHelper`, `CryptoHelper`, `ProcessTracker`
- **Registry Key Modified:** `HKLM\SOFTWARE\SolarWinds\Orion\Core\ReportWatcherRetry`
- **Registry Key Read:** `HKLM\SOFTWARE\Microsoft\Cryptography\MachineGuid`
- **Targeted Security Drivers:** `SysmonDrv`, `SentinelAgent`, `CylanceSvc`, `FeAgent`
- **FNV-1a 64-bit XOR Key:** `0x5BAC903BA7D81967` (6605813339339102567)

---

## 6. AFFECTED SYSTEMS & INFRASTRUCTURE IMPACT

- **Total Host Systems Assessed:** 4 Enterprise Network Management Consoles
- **Directly Impacted Systems:** 1 Server (`SRV-ORION-NMS-01`)
- **Compromise of Sensitive Data / PII:** Under active audit; no outward data exfiltration observed beyond initial DNS beacon queries prior to firewall isolation.
- **Service Disruption:** SolarWinds Orion monitoring services stopped; internal network visibility maintained via secondary out-of-band monitoring.

---

## 7. CONTAINMENT & MITIGATION ACTIONS TAKEN

1. **Network Quarantine:** Isolated host `SRV-ORION-NMS-01` into a segregated VLAN with zero internet egress routing.
2. **DNS Sinkholing:** Configured internal BIND and Active Directory DNS forwarders to null-route (`0.0.0.0`) all requests matching `*.avsvmcloud.com`.
3. **Process & Service Termination:** Disabled the `SolarWindsOrionInformationService` and revoked local administrative service tokens.
4. **Certificate Revocation Check:** Enforced strict CRL and OCSP checking across enterprise endpoints to block the compromised DigiCert signing certificate (`Serial: 0d444d63f58468861118014bd8a7621e`).
5. **Static Forensics & Evidence Preservation:** Generated bitstream images and ISO/IEC 27037 chain-of-custody documentation under Section 63 BSA 2023 and Section 105 BNSS 2023.
6. **Log Archival (180 Days):** All DHCP, DNS, authentication, and endpoint activity logs mirrored to tamper-evident WORM (Write Once Read Many) storage in accordance with CERT-In Direction 5(v).

---

## 8. STATUTORY DECLARATION

I hereby declare that the particulars furnished in this notification are true and correct to the best of our knowledge, information, and belief, and are submitted in faithful adherence to Section 70B(6) of the Information Technology Act, 2000 and CERT-In Direction No. 20(3)/2022-CERT-In.

**Authorized Signatory:**  
**Om Lanke** (Roll No: 16010123216)  
Cyber Legal Auditor & Incident Response Lead  
Department of Computer Engineering, KJ Somaiya School of Engineering  
Somaiya Vidyavihar University, Mumbai, India  
*Submitted via secure communication to:* `incident@cert-in.org.in`
