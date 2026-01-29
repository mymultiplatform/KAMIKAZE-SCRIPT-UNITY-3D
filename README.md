# Kamikaze Environment Control for Unity

A direct, code-driven approach to overwriting Unity scene environment and lighting settings at runtime.

This project treats `RenderSettings` as engine-level data instead of editor-only configuration.

Designed for procedural worlds, runtime lighting systems, environment experiments, and scene mutation tools.

---

## What This Does

This system permanently modifies scene lighting by writing directly to Unity’s environment settings.

It can:

* Force ambient lighting values
* Reset fog and skybox configuration
* Normalize directional lighting
* Persist changes even after script deletion
* Rewrite lighting data into the scene itself

The scene becomes the new environment state.

---

## Why This Approach

Unity normally expects lighting to be edited through the Lighting window.

These scripts bypass the editor and inject values directly into scene data.

This is the same concept used by:

* Sky systems
* Day/night cycles
* Atmosphere controllers
* Procedural lighting tools

---

## Usage

1. Create an empty GameObject
2. Attach the environment script
3. Press Play once
4. Scene lighting is permanently overwritten

The script can be removed afterward.

---

## Included Example

`KamikazeEnvironmentReset.cs`
Hard resets a scene back to Unity-style default lighting.

---

## Important Warning

These scripts modify global scene lighting.

Changes are not temporary.

Recommended practices:

* Test in a backup scene
* Use version control
* Avoid running in production scenes without backups

---

## Best Use Cases

* Procedural environments
* Runtime atmosphere systems
* Custom lighting tools
* Engine experiments
* Automated scene setup

---

## License

Free to use, modify, and experiment.

No warranty provided.

---

## Future Expansion Ideas

* Procedural sky color systems
* Runtime fog simulation
* Atmospheric scattering math
* Dynamic sun and moon cycles

---

Engine-level control comes with engine-level responsibility.



MYMULTIPLATFORM.COM


