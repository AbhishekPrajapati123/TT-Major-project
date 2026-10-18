# Project AstraNode: TryHackMe Ignite Penetration Test & Exploitation Tool

![Target](https://img.shields.io/badge/Target-TryHackMe%20Ignite-red)
![Vulnerability](https://img.shields.io/badge/CVE-2018--16763-orange)
![Language](https://img.shields.io/badge/Language-Python%203-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Overview

**Project AstraNode** is a comprehensive penetration testing repository documenting the full system compromise of the **TryHackMe: Ignite** machine. This repository contains the custom exploitation script (`fuelcms.py`), reconnaissance output, post-exploitation artifacts, and an enterprise-grade penetration testing report.

The primary entry vector targets **CVE-2018-16763** (Remote Code Execution in Fuel CMS 1.4.1) via improper input handling in the `pages/select` parameter, followed by vertical privilege escalation through hardcoded credential reuse and permissive `sudo` policies.

---

## 🛠️ Attack Kill Chain
