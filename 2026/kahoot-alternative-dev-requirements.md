# Kahoot Alternative - Dev Requirements

## Features

**University Engagement Platform**
(combining Kahoot, Google Classroom, and Interactive Slides).

### **1. Real-Time Engagement**

* Join via 6-digit PIN or QR Code.
* **Screen Synchronization**
* Points based on speed and accuracy.
* **Live Leaderboard:** Top players displayed after every question.
* **Instant Polls:** Rapid-fire "True/False" or "A/B/C/D" checks without pre-made questions.

### **2. Presentation Funtionality**

* Google Slides / PowerPoint/ PDF import with formatting intact.
* **Embedded Questions:** Insert polls or quizzes directly between slides.

### **3. AI & Automation**

* **AI Quiz Generator:** Upload lecture slides  AI generates 10 questions automatically.
* **Automated Attendance:** Marking students "Present" based on quiz participation.
* **Auto-Grading:** Instant scores for quizzes; manual grading UI for assignments.

### **4. Learning Management (The "Classroom" Layer)**

* **Class Feeds**
* **Assignment Submission:** File uploads (Zip/PDF) with strict deadline enforcement.
* **Course Materials**
* **Unified Gradebook**

### **5. Question Types**

* **Multiple Choice:** Standard 4-option questions.
* **True / False:** Binary choice.
* **Type Answer:** Short text input (fuzzy match).
* **Code Blocks:** Syntax highlighting for C++, Python, Java.
* **Math Equations:** LaTeX support for formulas.

### **6. Administration & System**

* **Self-Hosted:** Deployed entirely on university servers (Intranet).
* **Single Sign-On (SSO):** Log in via University Email / Workspace.
* **Student ID Validation**
* **Role-Based Access:** Admin, Teacher, Student, and Guest modes.
* **Analytics Export:** Download class performance reports as CSV/Excel.

## Preferred Tech Stack

| Component | Preferred Technology |
|-----------|----------------------|
| Frontend  | Next.js (typescript language) |
| Backend   | Express.js (typescript language) |
| Styling   | Tailwind CSS + Shadcn/UI |
| Runtime   | Bun (fastest js runtime) |
| Database  | PostgreSQL |
| ORM       | Drizzle/ Prisma |
| State Management | Redux/ Zustand |
| CDN/ Storage | S3 compatible (MinIO/ Supabase) |
| Websocket  | Socket.IO |

## Server Requirements

### **Recommended Production Setup**

| Component | Specifications |
|-----------|---|
| **Processor** | Intel Xeon E-2436 (6 Core / 12 Thread) |
| **Memory** | 32 GB DDR5 RAM |
| **Storage** | 3x 2.4TB SAS HDD (7.2TB Total) |
| **Network** | Onboard Dual 1GbE |

### **Service Allocation (Single Server)**

| Service | CPU Cores | RAM | Storage |
|---------|-----------|-----|---------|
| Frontend Server (Next.js) | 2 | 4 GB | 50 GB |
| Backend Server (Express.js + Bun) | 2 | 8 GB | 50 GB |
| Database (PostgreSQL) | 1 | 12 GB | 2000+ GB |
| Object Storage (MinIO) | 1 | 4 GB | 3000+ GB |
| Cache (Redis - Optional) | 0.5 | 2 GB | 20 GB |
| OS & Utilities | 0.5 | 2 GB | 50 GB |
| **Total** | **6+ Cores** | **32 GB** | **5000+ GB** |

> **Note:** Redis (cache server) is optional for caching but can be added later if needed for performance optimization.

## Architecture Overview

### Offline-first is preferred, but real-time features will require WebSockets

![](https://res.cloudinary.com/sharafat/image/upload/v1770564471/imagebin/tojokog2oob9takwutzw.png)

### Real-time Engagement Flow (kahoot-like)

![](https://res.cloudinary.com/sharafat/image/upload/v1770555826/imagebin/ynm0xmjzbyeyp7taetyj.jpg)

## Estimated Development Timeline

> 4 months

Example timeline,

| Feature | Week 1 | Week 2 | Week 3 | Week 4 | Week 5-6 | Week 7-8 | Week 9-10 | Week 11-12 | Week 13-14 | Week 15-16 |
|---------|--------|--------|--------|--------|-----------|-----------|------------|-------------|-------------|-------------|
| Real-Time Engagement | X | X | X | X |  |  |  ||  |  |  |  |
| Presentation Functionality |  |  | X || X | X |  |  |  |  |  |  |
| AI & Automation |  |  |  |  | X | X | X |  |  ||  |  |  |  |
| Learning Management |  |  |  | |  |  |  | X | X | X |  |  |  |
| Question Types |  |  |  |  |  | X | X | X | |  |  |  |  |
| Administration & System | X | X |  |  |  |  |  |  | X | X | X | X |  |

## Estimated Costs

| Sr. No. | Particulars / Details | Est. Hrs. | Rate (BDT) | Amount (BDT) |
| --- | --- | --- | --- | --- |
| **A** | **Phase 1: Architecture & Backend Core (Critical)** |  |  |  |
| 1 | Server Setup (Dell PowerEdge R360 Configuration, Ubuntu, RAID) | 15 | 500 | 7,500 |
| 2 | Database Schema Design (PostgreSQL + Drizzle ORM) | 15 | 500 | 7,500 |
| 3 | WebSocket Engine Architecture (Socket.IO + Performance Tuning) | 25 | 500 | 12,500 |
| 4 | Authentication & Security (SSO, Role-Based Access Control) | 20 | 500 | 10,000 |
| **B** | **Phase 2: Frontend & Real-Time UI** |  |  |  |
| 5 | UI Layout & Design (Shadcn/UI + Tailwind CSS) | 30 | 250 | 7,500 |
| 6 | Host Dashboard Dev (Quiz Creation, Lobby Management) | 40 | 250 | 10,000 |
| 7 | Player Interface Dev (Mobile Responsiveness, Join Logic) | 25 | 250 | 6,250 |
| 8 | **Real-time State Synchronization** (Redux/Zustand Complexity) | 35 | 500 | 17,500 |
| **C** | **Phase 3: Advanced Features** |  |  |  |
| 9 | **Slide/PDF Conversion Engine** (Backend File Processing) | 40 | 500 | 20,000 |
| 10 | **AI Quiz Generator** (External API Integration & Prompt Eng.) | 20 | 500 | 10,000 |
| 11 | Grading System & Analytics Export (CSV/Excel) | 15 | 250 | 3,750 |
| **D** | **Phase 4: Testing & Deployment** |  |  |  |
| 12 | **Load Testing** (Simulating 50+ Concurrent Users) | 15 | 500 | 7,500 |
| 13 | Final Deployment (Intranet DNS, Firewall Config) | 10 | 500 | 5,000 |
| 14 | Documentation (Admin Manual, User Guide, API Docs) | 10 | 250 | 2,500 |
|  |  |  |  |  |
| **E** | **Infrastructure Costs (Hardware & Capital)** | **Qty** | **Unit Cost** | **Total** |
| 15 | **Dell PowerEdge R360 Rack Server** | 1 | 430,000 | 430,000 |
|  | *Specs: Intel Xeon E-2436 (6 Core), 32GB DDR5 RAM, 3x2.4TB SAS HDD* |  |  |  |
| 16 | Domain Name / Static IP Allocation (Estimated) | 1 | 1,000 | 1,000 |
| 17 | API Credits (OpenAI/Gemini for AI Generator - 1 Year) | 1 | 2,000 | 2,000 |
|  |  |  |  |  |
|  | **Sub-Total (Labor Component)** | **315** |  | **127,500** |
|  | **Sub-Total (Hardware Component)** |  |  | **433,000** |
|  | **Grand Total** |  |  | **560,500** |
|  | **Contingency (5% for price fluctuations)** |  |  | **28,025** |
|  | **TOTAL PROJECT ESTIMATE** |  |  | **588,525 BDT** |

## References

* Fastest benchmark report,
  * <https://sharkbench.dev/web>
  * <https://github.com/rolldown/benchmarks>

* Resouce calculations,
  * <https://calculator.aws/#/createCalculator/ec2-enhancement>
