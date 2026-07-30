# 🎵 Applied AI Music Recommender

## Base Project
This project extends the **Music Recommender Simulation** from Module 3.
The original system used content-based filtering to score and rank songs 
against a manually defined user profile. It loaded songs from a CSV file 
and returned ranked recommendations with explanations.

## What This System Does
This applied AI system extends the original recommender by adding natural 
language mood interpretation. Instead of manually setting preferences, users 
can describe how they feel in plain English and the AI automatically generates 
a personalized music profile and recommends matching songs.

## Architecture Overview
The system has three main components:
- **ai_profile.py** — interprets natural language mood descriptions into structured profiles
- **recommender.py** — scores and ranks songs against the profile
- **main.py** — connects everything with logging and error handling

See diagrams/architecture.mmd for the full system diagram.

## Setup Instructions