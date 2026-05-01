# Ho Chi Minh City Opera House LoD 3 Result

## Overview

This folder contains an assignment-scale **LoD 3 style ArcGIS SceneView model** of the **Ho Chi Minh City Opera House / Nhà hát Thành phố Hồ Chí Minh** at:

- `10.776783598907993, 106.70317240490061`

The implementation is based on the ArcGIS JavaScript 3D extrusion workflow, but the result is not a single simple extrusion. It adds visible architectural detail so the building reads as **LoD 3-like** from normal viewing angles.

## Files

- `index.html`: the ArcGIS 3D scene
- `README.md`: explanation and research notes

## What Was Modeled

The model includes these visible components:

- Raised plinth and front stairs
- Main entrance pavilion
- Main theatre block
- Taller rear stage block
- Symmetrical front and rear annex masses
- Stepped roof tiers and a roof lantern
- Main doors and annex doors
- Front, side, and rear window bands
- Front balconies and simplified railings
- Cornice / molding bands (`gờ nổi`)
- Pilasters and low-detail ornament proxies on the facade
- Roof dormers

## Why This Qualifies as LoD 3 Style for the Assignment

The assignment asked for:

- roofs
- windows
- doors
- balconies
- moldings / raised details
- annex volumes
- geometry that clearly looks more advanced than a basic extrusion

This result satisfies that by separating the building into multiple architectural layers instead of one footprint with one height. The facade has repeated openings, a projecting entrance block, balcony slabs, balcony rails, cornice bands, and facade articulation. The roofline is also broken into multiple masses so the silhouette is closer to a real theatre than a plain box.

This is still a **lightweight academic model**, not a survey-grade BIM or full heritage reconstruction. Very small sculptural details were simplified on purpose to keep rendering smooth.

## Performance Strategy

To keep the scene responsive:

- I used **procedural polygon extrusions** instead of importing a dense mesh.
- Repeated details such as windows and rails are modeled as small, simple boxes.
- Sculptures and reliefs are represented by a few **ornament proxy masses** rather than high-polygon statues.
- The number of facade elements is high enough to read as LoD 3, but still limited enough for smooth rendering in the browser.

## Research Basis

The modeling choices were guided by web research about the real building:

- The building is at Lam Son Square and the coordinate in the scene matches the opera house location.
- It is a French colonial / French Third Republic era municipal theatre completed in 1900.
- The facade is highly ornamented and was influenced by the Petit Palais in Paris.
- The opera house sits on a raised plinth with a double-door arrangement.
- The building has a central main block plus smaller symmetrical side masses.
- The facade uses arched windows, railings / balconies, columns or pilaster-like vertical articulation, and relief decoration.

## Main Sources

- Wikipedia: Ho Chi Minh City Opera House
  - https://en.wikipedia.org/wiki/Ho_Chi_Minh_City_Opera_House
- Wikidata coordinate record
  - https://www.wikidata.org/wiki/Q1949129
- Augustus in Saigon: Overall layout of Saigon Opera House
  - https://augustusinsaigon.uni-trier.de/exhibits/show/architecture/item/31
- Augustus in Saigon / Classical Reception World Wide: Reliefs on the facade
  - https://crww.hypotheses.org/reliefs-on-the-facade-of-saigon-opera-house
- Vietnam Travel summary of architecture and area
  - https://vietnamtravel.com/saigon-opera-house/
- Anywhere travel note about the raised plinth and double doors
  - https://www.anywhere.com/vietnam/attractions/saigon-opera-house-iconic
- Wikimedia Commons facade photos used as visual reference
  - https://commons.wikimedia.org/wiki/File:Municipal_Theatre_of_Ho_Chi_Minh_City,_2023_(01).jpg
  - https://commons.wikimedia.org/wiki/File:Municipal_Theatre_of_Ho_Chi_Minh_City,_2023_(03).jpg
  - https://commons.wikimedia.org/wiki/File:Municipal_Theatre_of_Ho_Chi_Minh_City,_2023_(04).jpg

## How to Run

Open `index.html` through a local static server so the ArcGIS SDK loads normally. Example:

```bash
cd BTTH2/LAB02
python3 -m http.server 8080
```

Then open:

- `http://localhost:8080`

## Notes About Accuracy

The scene is **research-informed but simplified**:

- The placement is tied to the real coordinate.
- The overall composition follows the documented central mass + side annex layout.
- The facade vocabulary follows published photos and descriptions.
- Small sculptural and relief elements are intentionally abstracted for performance.

That tradeoff is deliberate so the model reads clearly as **LoD 3** while staying practical for a browser-based ArcGIS assignment.
