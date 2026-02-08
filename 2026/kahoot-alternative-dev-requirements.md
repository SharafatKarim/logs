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

| Component | Min CPU | Min RAM | Storage |
|-----------|----------------------|----------------------|----------------------|
| Frontend Server | 1 vCPU | 1 GB | 1 GB SSD |
| Backend Server | 2 vCPU | 2 GB | 1 GB SSD |
| Database (PostgreSQL) | 1 vCPU | 1 GB | 1 GB SSD |
| Object Storage (MinIO) | 1 vCPU | 512 MB | 50 GB SSD |
| ---- | --- | --- | --- |
| Overall | 2 vCPU | 2 GB | 55+ GB SSD |

> Redis (cache server) is optional for caching but can be added later if needed.

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

Average 9000 BDT to 15000 BDT per whole project. References,

* <https://www.fiverr.com/search/gigs?query=classroom%20management%20website%20nextjs&search_in=everywhere&search-autocomplete-original-term=classroom%20management%20website%20nextjs>

## References

* Fastest benchmark report,
  * <https://sharkbench.dev/web>
  * <https://github.com/rolldown/benchmarks>

* Resouce calculations,
  * <https://calculator.aws/#/createCalculator/ec2-enhancement>
