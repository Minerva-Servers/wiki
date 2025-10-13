---
title: Parallax Framework
description: What Parallax is and how it powers Minerva servers
---

# Parallax

Parallax is Minerva Servers’ custom game framework for Garry’s Mod. It’s the foundation that powers gameplay, UI, networking, and schema content across our servers. While most players don’t see it directly, everything from character systems to in-game interfaces runs on Parallax.

!!! note "Player-focused overview"
    You don’t need to know how Parallax is coded to enjoy the server. This page explains what it is at a high level, why it exists, and where it lives—without deep technical detail.

## What it is

- A custom-built framework maintained by Minerva Servers
- Structured around clear entry points (`gamemode/init.lua` for server, `gamemode/cl_init.lua` for client)
- Organizes functionality into directories that auto-load on boot: `libraries/`, `meta/`, `core/`, `hooks/`, `networking/`, `interface/`
- Uses a single top-level namespace `ax` (e.g., `ax.util`, `ax.config`, `ax.item`) to keep systems consistent and modular

## Why we use a custom framework

- Reliability: unified systems reduce bugs and inconsistencies across servers
- Modularity: features can be added, updated, and hot-reloaded without disrupting gameplay
- Performance & consistency: shared patterns for config, options, networking, and persistence keep things fast and stable

## Where it lives

Parallax is part of the server’s gamemode files and loads automatically when the server starts.

??? details "Technical layout (for the curious)"
    - Entry points include the framework boot sequence and utility helpers:
        - `gamemode/init.lua` (server) and `gamemode/cl_init.lua` (client)
        - `framework/boot.lua` orchestrates loading
        - `framework/util.lua` provides include/realm helpers
    - Auto-load order (handled by `boot.lua`):
        1. `libraries/`
        2. `meta/`
        3. `core/`
        4. `hooks/`
        5. `networking/`
        6. `interface/`
    - Schemas (like HL2RP) extend Parallax with their own content under `schema/`

## Key points

- Parallax is custom-made for Minerva Servers
- It keeps gameplay systems organized and consistent
- Schemas build on top of Parallax to deliver specific game modes and content

## Summary

Parallax is the invisible backbone of Minerva Servers, keeping everything running smoothly for players. You don’t need to manage or update anything—just play and enjoy the features, menus, and systems built on Parallax.

**How does Parallax compare to other frameworks?**

- Parallax uses a weight-based inventory system, similar to Clockwork and impulse. This means your character’s carrying capacity is based on item weight, not a grid or slots like Helix or Nutscript.
- Parallax is modular and hot-reloadable, allowing developers to update features and fix bugs without restarting the server. This keeps gameplay stable and responsive.
- Parallax is schema-driven: it’s designed to support custom roleplay experiences (like HL2RP) by letting schemas extend the framework with their own content and rules.
- Parallax avoids legacy bloat and is built with modern code practices, making it easier to maintain and expand.
- Unlike DarkRP, which is a sandbox gamemode, Parallax is a true framework for building custom roleplay gamemodes.

**Technical highlights:**

- Unified namespace (`ax`) and clear file prefixes (`cl_`, `sv_`, `sh_`) for consistency
- Store pattern for config and options syncing
- Hot-reload hooks for safe updates
- Schemas extend Parallax for unique game modes
