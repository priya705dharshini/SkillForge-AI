# SkillForge AI - Agentic AI Career Assistant

## Project Overview

SkillForge AI is an AI career assistant that analyzes user profiles, detects skill gaps, creates personalized learning roadmaps, recommends projects, and provides conversational career guidance. The project is designed as a local private AI agent system that helps learners choose career paths, build skills, and prepare portfolio work.

## Problem Statement

Many students and early-career professionals struggle to choose a clear career path and identify the skills they need to reach their goals. They often do not know which projects to build, what learning steps to follow, or how to connect their interests with real-world job requirements.

## Solution

SkillForge AI solves this problem by using multiple AI agents to analyze user profiles, compare user skills against career goals, and provide actionable guidance. The system supports profile management, gap detection, roadmap generation, project recommendations, and an AI chat assistant that remembers past conversations.

## Features

- Profile Management
- Career Analysis Agent
- Skill Gap Detection
- Roadmap Generation Agent
- Project Recommendation Agent
- AI Chat Assistant
- Memory-based Conversation System

## System Architecture

User
 |
Profile Module
 |
Career Analysis Agent
 |
Roadmap Agent
 |
Project Recommendation Agent
 |
Memory Agent
 |
AI Career Assistant

This architecture describes the agentic flow of data from profile intake through specialized guidance and chat memory.

## Technology Stack

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- AI Agents
- Git/GitHub

## AMD Radeon GPU / ROCm Adaptation

SkillForge AI is designed for local AI agent deployment and can be optimized for AMD Radeon GPU acceleration. Future development can leverage ROCm-supported PyTorch and local LLM inference so the application can run efficiently on AMD GPU hardware.

Potential optimization steps:
- Deploy the AI agents locally on a private machine
- Use ROCm-compatible PyTorch builds for AMD GPUs
- Run local LLM inference with ROCm acceleration for fast, private career guidance

## Installation Guide

1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - Windows:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```

## Usage Instructions

- Create a profile or use the demo user
- View the chat dashboard at `/chat`
- Chat with the AI assistant to get career guidance
- Ask for roadmap recommendations and project ideas
- Review chat history at `/chat-history`

## Project Demo

This submission includes a local Flask demo of SkillForge AI, with an AI chat assistant and conversation history. The demo highlights profile-aware responses and showcases the system's career guidance workflow.
