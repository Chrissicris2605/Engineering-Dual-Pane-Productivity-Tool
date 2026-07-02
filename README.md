# 🖥️ Engineering Dual-Pane Productivity Tool

**Public demo – Desktop Productivity / Engineering Workflows / Python UI**

This repository contains a **safe public demo** of a dual-pane desktop productivity tool designed to connect visual technical context with structured data.

The professional work that inspired this project was developed in an engineering environment. This public repository is **not** the production tool. It is a simplified, rebuilt-from-scratch implementation using fictional components, generic terminology, and non-proprietary behavior.

---

## 📌 Why this project exists

Engineering workflows often require users to analyze visual artifacts and structured data at the same time. When this information lives in separate windows, files, or systems, the work becomes slower and more cognitively demanding.

This demo shows how a dual-pane interface can help users:

- 🖼️ view a simplified technical diagram;
- 📋 inspect structured component data;
- 🔗 connect visual and tabular context;
- 🎯 highlight a selected component across both views;
- ➕ add fictional components during the demo session;
- 🧠 reduce context switching and interpretation effort.

---

## 🧪 Public demo concept

The demo uses a fictional **Technical Assembly Review** scenario.

The left pane displays a simplified visual diagram. The right pane displays structured data for fictional components. When a user selects a row in the table, the corresponding component is highlighted in the diagram and its details are shown in the status panel.

Users can also add a new fictional component through a small form. The new item appears in the structured table and is automatically positioned in the visual diagram. Data created during the session is kept in memory only and is not persisted to disk.

No real drawings, real datasets, company templates, or internal business rules are included.

---

## 🖼️ Screenshots

Screenshots will be added after the public demo is tested locally.

---

## 📂 Repository structure

```text
.
├── src/
│   ├── main.py                 # Application entry point
│   ├── app.py                  # Dual-pane desktop interface
│   ├── sample_data.py          # Fictional demo component data
│   └── styles.py               # UI constants
├── docs/
│   ├── confidentiality.md
│   └── public-demo-scope.md
├── screenshots/
│   └── .gitkeep
├── requirements.txt
└── README.md
```

---

## 🚀 How to run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the desktop demo

```bash
python src/main.py
```

---

## 💼 Professional relevance

This project demonstrates skills in:

- desktop application development;
- workflow-oriented UI design;
- structured data presentation;
- visual-to-data context mapping;
- lightweight interaction design;
- engineering productivity tooling;
- usability-focused automation;
- safe public documentation of confidential professional work.

It reflects the kind of product I enjoy building: practical desktop tools that reduce cognitive effort, improve clarity, and make complex technical workflows easier to execute.

---

## 📈 Original case study impact

The professional tool that inspired this public demo helped reduce repetitive task execution time by approximately **50%** and enabled new users to become productive after approximately **1 hour of training**.

This public repository demonstrates the concept in a safe, fictional, and simplified way.

---

## 🔒 Confidentiality notice

This repository does **not** include:

- production source code;
- proprietary algorithms;
- real datasets;
- internal company files;
- client information;
- confidential business rules;
- private naming conventions;
- real technical drawings.

All sample data and visual elements are fictional. All logic was rebuilt from scratch for public demonstration purposes.
