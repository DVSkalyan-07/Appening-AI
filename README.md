# Multi-Agent Architectural Workflow (CrewAI & Gemini)

This repository contains a sequential multi-agent execution pipeline built using **CrewAI** and **Google Gemini (1.5-flash)**.

## Architecture & Agents
1. **Agentic AI Specialist (`research_agent`)**: Extracts core requirements, metrics, and multi-agent design patterns.
2. **Senior AI Systems Engineer (`developer_agent`)**: Synthesizes specifications into production-ready workflow logic.
3. **Verification & Compliance Evaluator (`verifier_agent`)**: Audits output code for edge cases and operational quality.

## Quick Start Instructions

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/](https://github.com/)<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
   cd <YOUR_REPO_NAME>
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Google Gemini API Key**:
   * **Linux/macOS**:
     ```bash
     export GEMINI_API_KEY="your_api_key_here"
     ```
   * **Windows (Command Prompt)**:
     ```cmd
     set GEMINI_API_KEY=your_api_key_here
     ```
   * **Windows (PowerShell)**:
     ```powershell
     $env:GEMINI_API_KEY="your_api_key_here"
     ```

4. **Run the script**:
   ```bash
   python main.py
   ```
