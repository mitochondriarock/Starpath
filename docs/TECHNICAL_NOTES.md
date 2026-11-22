# Technical notes — STARPATH 0.2

## Astronomy

The prototype uses approximate right ascension and declination for a set of prominent navigational stars. For an observer at geographic latitude φ and longitude λ at a UTC date/time, approximate local sidereal time determines each star's hour angle H. The chart computes geometric altitude h and azimuth A via a standard equatorial-to-horizontal conversion.

- `sin(h) = sin(φ)sin(δ) + cos(φ)cos(δ)cos(H)`.
- The chart uses an azimuth convention of 0° north, 90° east, 180° south and 270° west.
- Polaris is **close to** celestial north, not coincident with it. Its observed altitude is a first approximation to geographic latitude, not an exact position fix.
- Current coordinates are approximately epoch J2000. The simulation omits precession, nutation, stellar proper motion, topographic obstruction, atmospheric bending, weather and light pollution. A future upgrade should use a maintained star catalog and high-precision algorithms.
- The chart's flat projection is a teaching visualization, not a calibrated sextant or full-sphere optical projection.

Reference: U.S. Naval Observatory, [Computing Altitude and Azimuth](https://aa.usno.navy.mil/faq/alt_az) and [Approximate Sidereal Time](https://aa.usno.navy.mil/faq/GAST).

## Expedition

The simulated expedition is set near Fort Collins, Colorado (40.5853° N, 105.0844° W) for 2027-05-21 03:30 UTC, corresponding to 2027-05-20 at 9:30 p.m. local daylight time. The rescue location, map grid and travel route are entirely fictional. Mission feedback includes numeric tolerances; scoring and success do not imply actual navigational reliability.

## Water refraction

The optical exercise considers a flat air-water interface and uses n_air≈1.000 and n_water≈1.333. A ray is traced with Snell's law to illustrate why submerged objects appear displaced when observed obliquely from air. Water motion, scattering, fish motion, and projectile dynamics are excluded; diagrams are schematic, not field-calibrated.

Reference: [Iowa PBS, Science of Spearfishing](https://www.iowapbs.org/education/initiatives/iowasciencephenomena/12390/science-spearfishing).

## Wildlife identification — safety rules

The field guide is designed around uncertainty, morphological comparison and 'do not consume' decisions. A future photographic specimen module should pair features with ecological context, source provenance and multiple look-alikes. It must never assert that a mushroom or wild plant is safe to eat based on a photograph or identification confidence score. Explicit warnings must persist even when users succeed in the game.

## Privacy and offline behavior

Version 0.2 requires no accounts, no user data storage, no geolocation permissions, no third-party scripts and no analytics. The entire app is bundled in `index.html`. A hosted page can be loaded without installing software; local/offline use on iOS is subject to browser restrictions.
