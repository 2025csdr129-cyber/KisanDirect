# 🌱 KisanDirect (కిసాన్ డైరెక్ట్)
> **Direct Regional Agricultural Marketplace, Mandi Intelligence & Split-Escrow Portal**  
> *Engineered for smallholder farmers and FPO clusters in the Rayalaseema / Chittoor agricultural corridor.*

---

## 📌 Overview

**KisanDirect** is a hyper-local, bilingual farmgate-to-buyer agri-commerce engine designed to eliminate commission agent leakage, distress selling, and opaque weighment fraud for farmers in Southern Andhra Pradesh (Madanapalle, Tirupati, Pileru, Chittoor) and border consumption hubs (Chennai, Bengaluru, Kolar, Guntur).

The platform bridges real-time physical mandi auction data with digital contracting, vehicle route optimization (CVRP), automated freight estimation, and a vernacular-first voice AI assistant.

---

## ✨ Key Features

### 1. 🌾 Real-Time Multi-Crop & Multi-Mandi Price Intelligence
- Ground benchmarks calibrated for regional cash crops: **Tomato (Hybrid/Naati)**, **Green Chilli (Teja/G4)**, **Dry Red Chilli**, **Onion (Bellary)**, and **Mango (Totapuri)**.
- Live corridor comparison matrix across **Madanapalle APMC**, **Tirupati Wholesale**, **Kolar APMC**, **Koyambedu Wholesale (Chennai)**, **Bengaluru (Yeshwanthpur)**, and **Guntur Mirchi Yard**.
- **72-Hour Hold vs. Sell Predictive Advisory** based on regional mandi arrivals and destination consumption pull.

### 2. 🤖 "KisanMitra AI" Vernacular Voice Assistant
- Floating voice microphone accessible across mobile screens.
- Supports **Telugu (`te-IN`)**, **English (`en-IN`)**, and **Tanglish/phonetic Telugu** queries.
- Powered by Web Speech Recognition and dual-text/audio SpeechSynthesis (TTS) playback for hands-free advisory in the field.
- Answers queries on real-time commodity prices, pest management, harvest timing, and cold storage availability.

### 3. 🔒 40/60 Split Smart Escrow & Digital Weighment Slips
- **40% Farmgate Advance:** Instantly locked and disbursed via UPI upon vehicle check-in and farmgate crate loading.
- **60% Final Settlement:** Released automatically upon destination terminal weighment verification.
- **Official Bilingual APMC Weighment Slip:** Printable/PDF-exportable receipts compliant with AP Agricultural Market rules, featuring tare crate deductions and 100% direct-channel cess exemptions.

### 4. 🚚 Interactive Freight & Net Profit Calculator
- Computes vehicle fuel allocation (₹11/km pooled commercial tariff), crate handling charges (₹6/crate), and toll fees from the origin cluster (Chennayyagunta/Chittoor) to any destination terminal.
- Calculates the **Real Net Take-Home Margin (తల్లి లాభం)** per kilogram before dispatching produce.

### 5. ❄️ Micro-Cold Storage & Collective Input Pooling
- On-demand booking for solar micro-cold rooms at ₹6/crate/day to prevent post-harvest perishability loss.
- Reverse-logistics bulk buying for seeds and bio-fertilizers leveraging empty backhaul trucks.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python 3.10+), SQLAlchemy, Uvicorn
- **Database:** SQLite (lightweight zero-config persistence)
- **Logistics Engine:** Google OR-Tools (Capacitated Vehicle Routing Problem - CVRP)
- **Frontend:** Responsive Mobile-First PWA (HTML5, Vanilla JavaScript, CSS3, FontAwesome)
- **Voice Engine:** Web Speech API (`SpeechRecognition` & `SpeechSynthesisUtterance`)
- **HTTP Client & External Feeds:** HTTPX (async Agmarknet / Data.gov.in integration)

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.10 or higher installed:
```bash
python --version
