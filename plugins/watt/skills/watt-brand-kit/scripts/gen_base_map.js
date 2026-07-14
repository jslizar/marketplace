// Dev/build script: generate a base US states SVG (Albers USA, AK/HI insets)
// from the us-atlas package. Output: assets/us-states.svg with <path id="XX">
// per state (USPS code). Coordinates are pre-projected to a 975x610 canvas.
//
//   npm install us-atlas@3 topojson-client@3
//   node gen_base_map.js > ../assets/us-states.svg
//
// The runtime choropleth (choropleth.py) only sets fill per id; it never
// regenerates geometry, so this script runs once at authoring time.

const topo = require("us-atlas/states-albers-10m.json");
const { feature } = require("topojson-client");

const FIPS = {
  "01":"AL","02":"AK","04":"AZ","05":"AR","06":"CA","08":"CO","09":"CT","10":"DE",
  "11":"DC","12":"FL","13":"GA","15":"HI","16":"ID","17":"IL","18":"IN","19":"IA",
  "20":"KS","21":"KY","22":"LA","23":"ME","24":"MD","25":"MA","26":"MI","27":"MN",
  "28":"MS","29":"MO","30":"MT","31":"NE","32":"NV","33":"NH","34":"NJ","35":"NM",
  "36":"NY","37":"NC","38":"ND","39":"OH","40":"OK","41":"OR","42":"PA","44":"RI",
  "45":"SC","46":"SD","47":"TN","48":"TX","49":"UT","50":"VT","51":"VA","53":"WA",
  "54":"WV","55":"WI","56":"WY","72":"PR"
};

const fc = feature(topo, topo.objects.states);
const r = (n) => Math.round(n * 10) / 10;

function ringsToPath(coords, depth) {
  // Polygon: array of rings. MultiPolygon: array of polygons.
  if (depth === 1) {
    let d = "";
    for (const ring of coords) {
      d += "M" + ring.map((p) => `${r(p[0])},${r(p[1])}`).join("L") + "Z";
    }
    return d;
  }
  return coords.map((poly) => ringsToPath(poly, depth - 1)).join("");
}

const paths = [];
for (const f of fc.features) {
  const abbr = FIPS[String(f.id).padStart(2, "0")];
  if (!abbr) continue;
  const g = f.geometry;
  if (!g) continue;
  const d =
    g.type === "Polygon" ? ringsToPath(g.coordinates, 1) :
    g.type === "MultiPolygon" ? ringsToPath(g.coordinates, 2) : "";
  if (d) paths.push(`  <path id="${abbr}" d="${d}"/>`);
}
paths.sort();

process.stdout.write(
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 975 610" class="us-map">\n` +
  `<g fill="var(--map-low, #cdc4a5)" stroke="#ffffff" stroke-width="1" stroke-linejoin="round">\n` +
  paths.join("\n") +
  `\n</g>\n</svg>\n`
);
