# 🌱 KisanDirect (కిసాన్ డైరెక్ట్)
> **Hyper-Local Agricultural Marketplace, Live Corridor Intelligence & 40/60 Split-Escrow Platform**  
> *Engineered for smallholder farmers, FPOs, wholesale buyers, and logistics operators across the Rayalaseema & Chittoor agricultural belt.*

---

## 📌 Executive Summary

**KisanDirect** is a full-stack, mobile-first agricultural ecosystem built to eliminate middleman commission leakage, distress selling, and opaque weighment manipulation for farmers in Southern Andhra Pradesh (Madanapalle, Tirupati, Pileru, Chittoor) and border consumption centers (Chennai, Bengaluru, Kolar, Guntur).

The platform bridges real-time electronic mandi benchmarks with digital smart contracting, Google OR-Tools vehicle routing (CVRP), automated freight & net-profit calculation, and a vernacular-first voice assistant (**KisanMitra AI**) tailored for busy, non-technical farmers.

---

## 🏗️ System Architecture & Workflow
[ 👨‍🌾 Farmer Portal (PWA) ] 
      │  ├── Voice / Tanglish AI (KisanMitra)
      │  ├── Multi-Crop Corridor Benchmark Scanner
      │  ├── Camera AI Crate Inspection & Cert Stamping
      │  └── Net Take-Home Freight Calculator
      ▼
      [ ⚡ FastAPI Core Application (REST Engine) ]
│  ├── SQLite / SQLAlchemy Persistent Data Layer
│  ├── Logistics Optimization (Google OR-Tools CVRP)
│  └── In-App WhatsApp / SMS Notification Engine
▼
┌───────────────────────────┴───────────────────────────┐
▼                                                       ▼
[ 🏢 Wholesale Buyer Hub ]                       [ 🚚 Driver Manifest ]
├── 40% Farmgate Advance Lock                    ├── Dynamic Cluster Pickup Stops
├── 60% Terminal Settlement Vault                ├── Real-Time GPS Terminal Navigation
└── APMC Compliant Digital Weighment Slips       └── Return-Logistics Input Delivery
---

## ✨ Core Modules & Functionality

### 1. 🌾 Real-Time Multi-Crop & Multi-Mandi Intelligence
* **Regional Cash Crops Covered:**
  * **Tomato** (Hybrid & Naati varieties)
  * **Green Chilli** (Teja & G4 grades)
  * **Dry Red Chilli** (Guntur export & commercial standards)
  * **Onion** (Bellary & Nasik lines)
  * **Mango** (Totapuri pulp & Banginapalli table varieties)
* **Live Corridors Synced:** Madanapalle APMC, Tirupati Wholesale Hub, Kolar Gold APMC, Chennai Koyambedu, Bengaluru Yeshwanthpur, and Guntur Mirchi Yard.
* **72-Hour Hold vs. Sell Engine:** Ingests local mandi arrival volumes and regional terminal demand curves to issue actionable harvest advisories.

### 2. 🤖 "KisanMitra AI" Vernacular Voice Assistant
* **Native Dialect Understanding:** Processes native Telugu script (`te-IN`), English (`en-IN`), and Romanized Tanglish (*"kotha eppudu koyyali"*, *"tomato rate entha"*).
* **Hands-Free Speech Loop:** Powered by the browser Web Speech API for voice dictation and SpeechSynthesis for audio playback in field conditions.
* **Domain Knowledge:** Real-time commodity rates, pest diagnostics (leaf curl, fruit borer, early blight), harvest advisories, and micro-cold storage checks.

### 3. 🔒 40/60 Split Smart Escrow & Digital Weighment Slips
* **Split Settlement Protocol:**
  * **40% Farmgate Advance:** Locked into escrow upon digital match and disbursed immediately via UPI upon farmgate truck check-in and crate loading.
  * **60% Final Settlement:** Disbursed directly to farmer UPI accounts once physical weighment and quality checks are verified at the terminal.
* **Official Digital Weighment Slip:** Printable/PDF-exportable APMC-standard bill including tare weight deductions (4% crate standard) and 100% direct-channel market cess waiver verification.

### 4. 🚚 Interactive Freight & Net Profit Calculator
* **Accurate Logistics Cost Breakdown:** Evaluates vehicle fuel allocation (₹11/km shared mini-truck tariff), crate handling/loading charges (₹6/crate), and state highway toll tariffs from the Chennayyagunta/Chittoor cluster to target city mandis.
* **Net Take-Home Metric (తల్లి లాభం):** Displays the exact realized price per kg after transport deductions before dispatching freight.

### 5. ❄️ Solar Micro-Cold Storage & Pooled Agri-Inputs
* **Distress-Sale Buffer:** On-demand booking for decentralized solar cold chambers at ₹6/crate/day for up to 14 days.
* **Reverse Logistics Purchasing:** Up to 25% bulk savings on certified seeds and bio-fertilizers using empty return-haul trucks with zero freight fees.

---

## 🛠️ Technology Stack

| Layer | Technologies Used |
|---|---|
| **Backend Framework** | FastAPI (Python 3.10+), Uvicorn ASGI Server |
| **ORM & Database** | SQLAlchemy 2.0, SQLite (Zero-config embedded relational store) |
| **Logistics & Routing** | Google OR-Tools (Capacitated Vehicle Routing Problem - CVRP) |
| **Frontend Clients** | Mobile-First Progressive Web App (HTML5, Vanilla ES6+, CSS3, FontAwesome) |
| **Voice & Audio** | Browser Native Web Speech API (`SpeechRecognition` & `SpeechSynthesis`) |
| **Network & Feeds** | HTTPX Async Client, Python-Dotenv, Pydantic v2 |

---

## 📁 Repository Directory Structure

```text
agri-marketplace/
├── .gitignore                      # Git exclusions (venv, db, pycache)
├── requirements.txt                # Production Python dependencies
├── README.md                       # Comprehensive system documentation
├── app/
│   ├── __init__.py
│   ├── main.py                     # FastAPI app bootstrap & static mount
│   ├── database.py                 # SQLite engine & database sessions
│   ├── models.py                   # SQLAlchemy schema definitions
│   ├── schemas.py                  # Pydantic request/response models
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints.py            # REST endpoints (Auth, Mandi, Escrow, AI)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── live_integrations.py    # Mandi pricing models & notification dispatch
│   │   ├── freight_weighment.py    # Freight cost model & weighment generator
│   │   ├── route_optimizer.py      # Google OR-Tools CVRP solver
│   │   ├── assisted_bot.py         # Vernacular fallback parsing routines
│   │   ├── mandi_api.py            # External data connectors
│   │   └── pricing_forecasting.py  # Arrival analytics & price projections
│   └── static/
│       ├── index.html              # Farmer Portal PWA (Bilingual UI, AI Voice)
│       ├── buyer.html              # Wholesale Buyer Hub & Escrow Management
│       ├── driver.html             # Driver Route Manifest & Loading Tracker
│       ├── manifest.json           # Web App Manifest for mobile installation
│       ├── sw.js                   # Service Worker cache layer
│       └── icon.svg                # Brand icon asset
   🚀 Step-by-Step Setup & Installation1. PrerequisitesPython 3.10 or higherGit installed2. Clone the RepositoryBashgit clone [https://github.com/2025csdr129-cyber/KisanDirect.git](https://github.com/2025csdr129-cyber/KisanDirect.git)
cd KisanDirect
3. Create & Activate Virtual EnvironmentWindows (PowerShell):PowerShellpython -m venv venv
.\venv\Scripts\Activate.ps1
Linux / macOS:Bashpython3 -m venv venv
source venv/bin/activate
4. Install DependenciesBashpip install -r requirements.txt
5. Configure Environment VariablesCreate a .env file in the project root:Ini, TOML# Production Secret Configuration
JWT_SECRET_KEY=kisan_direct_production_key_2026
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# External Mandi Agmarknet API (Optional)
DATA_GOV_IN_API_KEY=
6. Initialize Database TablesBashpython -c "from app.database import engine, Base; from app.models import *; Base.metadata.create_all(bind=engine); print('Database initialized successfully!')"
7. Run the ApplicationBashpython -m uvicorn app.main:app --reload --port 8000
🌐 Portal Navigation LinksOnce the application is running, open your browser to access the specialized interfaces:PortalURLTarget Audience & FeaturesFarmer PWAhttp://127.0.0.1:8000/Harvest publishing, KisanMitra AI Voice, mandi arbitrage, freight calculatorWholesale Buyer Hubhttp://127.0.0.1:8000/buyerVerified produce catalog, 40/60 split escrow locking & releaseDriver Manifesthttp://127.0.0.1:8000/driverCollection route stops, payload balance tracking, GPS navigationInteractive API Docshttp://127.0.0.1:8000/docsSwagger UI for all backend API endpointsAlternative API Docshttp://127.0.0.1:8000/redocReDoc API specifications📄 License & AttributionBuilt as an open-source agri-tech initiative for regional empowerment and fair agricultural trade in Rayalaseema, Andhra Pradesh.

