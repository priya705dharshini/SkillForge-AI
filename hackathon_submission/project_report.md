# SkillForge AI - Project Report

## Project Background

SkillForge AI was created to support learners who need personalized career direction. Many students and recent graduates lack clear guidance on which skills to build, how to structure learning, and which projects will make them more competitive.

## Target Users

- Students exploring technology careers
- Early career professionals seeking direction
- Bootcamp learners building a portfolio
- Anyone looking for personalized skill and project guidance

## Application Scenario

A learner logs into SkillForge AI, creates or updates their profile, and shares their goals. The application analyzes the profile data and provides career insights, skill gap detection, customized roadmaps, and project recommendations. The user can continue the conversation with an AI assistant that remembers past chat history.

## Agent Architecture

The system is organized into agent modules:

- Profile Module: Collects user profile data such as skills, interests, and career goals.
- Career Analysis Agent: Evaluates the user profile and recommends relevant career directions.
- Roadmap Generation Agent: Creates personalized learning roadmaps and milestones.
- Project Recommendation Agent: Suggests portfolio projects aligned with the user's target career.
- Memory Agent: Stores conversation history and supports context-aware responses.
- AI Career Assistant: Delivers chat-based coaching.

## Core AI Capabilities

- Profile-aware response generation
- Skill gap detection and career alignment
- Roadmap generation for learning steps
- Project recommendation for portfolio building
- Persistent chat memory via stored conversation history

## Model/Algorithm Explanation

The current prototype uses a rule-based AI response generator with SQLite-backed user and chat memory. This design demonstrates the architecture for private local deployment, and it is ready to evolve into a stronger agentic system with LLM-based reasoning.

## AMD Radeon GPU and ROCm Optimization Plan

The next phase of SkillForge AI is to support local model inference on AMD Radeon GPUs using ROCm. The optimization plan includes:

- Running local AI models on ROCm-compatible PyTorch
- Adapting the application to use local LLM inference for private agent behavior
- Accelerating vector embeddings and agent reasoning with ROCm GPU support
- Benchmarking the system on AMD Radeon GPU hardware for responsiveness

## Innovation

SkillForge AI combines career coaching with agent-based personalization. The innovation lies in treating career guidance as a chain of specialized agents, with a memory-backed chat assistant that keeps context from earlier conversations.

## Future Improvements

- Upgrade the backend to use local LLMs for richer career analysis
- Add a dedicated profile dashboard and career path visualization
- Expand roadmap and project recommendation capabilities
- Integrate ROCm-accelerated inference for AMD GPU deployment
- Add user authentication and multi-profile support

## Team Member Contribution

- Single developer: Designed the SkillForge AI prototype, implemented the Flask application, created the AI chat assistant, and prepared the hackathon submission materials.
