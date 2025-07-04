---
title: Unit one - first agent
colorFrom: green
colorTo: gray
sdk: gradio
sdk_version: 5.23.1
app_file: app.py
pinned: false
tags:
- smolagents
- agent
- smolagent
- tool
- agent-course
---

Check out the configuration reference at [spaces-config-reference](https://huggingface.co/docs/hub/spaces-config-reference).

# Unit one project: first agent using smolagents

Hands-on tutorial - create a simple agent using smolagents.

- My main GitHub repository for the course: [HuggingFace agents course](https://github.com/gperdrizet/hf-agents-course).
- Unit one tutorial page on HuggingFace: [Let’s Create Our First Agent Using smolagents](https://huggingface.co/learn/agents-course/unit1/tutorial)

## Features

1. Multi-turn agent with [Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) using Gradio and smolagents
2. Image generation using [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) from Black Forest Labs
3. Text to speech using [Chatterbox](https://huggingface.co/ResembleAI/chatterbox) from Resemble AI
4. Web search/site crawling
5. Time-zone look-up

## Running

From your HuggingFace settings dashboard, create a fine-grained access token with inference permissions.

### 1. HuggingFace spaces

[Unit one project: smolagents](https://huggingface.co/spaces/gperdrizet/unit-one-smolagents)

Make your own copy of the space and add your HuggingFace token as `HF_TOKEN` via: settings → Secrets and variables → New secret.

### 2. GitHub codespace

[Unit one project: smolagents](https://github.com/gperdrizet/unit-one-introduction/tree/main)

Fork a copy of the repository, then add your HuggingFace token as `HF_TOKEN` via: settings → Secrets and variables → Codespaces → New repository secret. Start a new codespace on main.
